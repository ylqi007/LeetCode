In Java both `ArrayList` and `LinkedList` inherit their `equals(Object)` implementation from `AbstractList`, so the behavior is **identical** for both.  Here’s roughly what the code in `AbstractList` does (Java 8+):

```java
@Override
public boolean equals(Object o) {
    if (o == this)
        return true;
    if (!(o instanceof List))
        return false;
    List<?> other = (List<?>) o;
    Iterator<E> it1 = this.iterator();
    Iterator<?> it2 = other.iterator();
    while (it1.hasNext() && it2.hasNext()) {
        E  e1 = it1.next();
        Object e2 = it2.next();
        if (!(e1 == null ? e2 == null : e1.equals(e2)))
            return false;
    }
    // only equal if both iterators are exhausted simultaneously
    return !it1.hasNext() && !it2.hasNext();
}
```

---

### Key points

1. **Cross‐implementations compare equal**

   ```java
   List<Integer> a = new ArrayList<>(Arrays.asList(1,2,3));
   List<Integer> b = new LinkedList<>(Arrays.asList(1,2,3));
   a.equals(b);  // true
   b.equals(a);  // true
   ```

   Because it just checks for `instanceof List`, not for the *same* implementation class.

2. **Order‐sensitive, null‐safe element‐wise compare**

    * Walks both lists’ iterators in lock‐step.
    * For each pair `(e1,e2)`, returns false if `e1==null ? e2!=null : !e1.equals(e2)`.

3. **Length check is implicit**
   After the loop returns, it only returns true if *both* iterators have no remaining elements.  That ensures `size()` must match as well.

4. **Time complexity**

    * **O(n)** where *n* is the smaller of the two lists’ lengths (and they must match length to be equal).
    * An `ArrayList`’s iterator and a `LinkedList`’s iterator both support `next()` in amortized O(1), so cross‐comparison is linear.

5. **Why no override in each class?**
   Since the logic is *exactly* the same, it lives once in `AbstractList`.  Neither `ArrayList` nor `LinkedList` needs to re‐implement it.

---

### Takeaway

* **Behavior:** `list1.equals(list2)` is true iff both are `List` instances, same length, and contain pairwise‐equal elements in the same order—regardless of whether they’re `ArrayList`, `LinkedList`, or any other `List` implementation.
* **Performance:** Always linear time in the number of elements.
* **Implementation:** Shared in `AbstractList`, so you don’t see an `equals` in either concrete class.



## Reference
* https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/AbstractList.html#equals(java.lang.Object)