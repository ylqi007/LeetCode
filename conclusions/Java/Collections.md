

## Collections.binarySearch()
### 1. What does `binarySearch` return?
The contract for `Collections.binarySearch(list, key)` is:
* **If** `key` **is found at index** `k`: returns `k` (a non-negative index).
* **If not found**, returns `–(insertionPoint) – 1`, where `insertionPoint` is the index **where** `key` *would* be inserted to keep the list sorted.

For example, given a sorted list `[2, 4, 6, 8]`:

| key | return value | meaning            |
| --- | ------------ | ------------------ |
| `6` | `2`          | found at index 2   |
| `5` | `-3`         | not found, `ins=2` |
| `1` | `-1`         | not found, `ins=0` |
| `9` | `-5`         | not found, `ins=4` |


### 2. Recovering the insertion point

If `i = Collections.binarySearch(...)` is **negative**, it encodes the insertion point:

```
i = -(insertionPoint) - 1
```

Solve that for `insertionPoint`:

```
i = -ins - 1
⇒ i + 1 = -ins
⇒ ins = -(i + 1)
⇒ ins = -i - 1
```

So:

```java
int i = Collections.binarySearch(list, idx);
if (i >= 0) {
    // exact match at position i
} else {
    int insertionPoint = -i - 1;   // this is the correct insertion point
    // ins is now the smallest index where list.get(ins) > idx
}
```


### 3. Why it matters here

Once you have `ins`:

* **`ins`** is the index of the first element **greater than** `idx` (if any).
* The predecessor is at `ins - 1` (if `ins > 0`).

You then check those two neighbors to find which is closer:

```java
int dist = Integer.MAX_VALUE;
if (ins < list.size()) {
    dist = Math.min(dist, list.get(ins) - idx);
}
if (ins - 1 >= 0) {
    dist = Math.min(dist, idx - list.get(ins - 1));
}
```

That gives you the minimum distance from `idx` to the nearest occurrence of the target color.

---

### Shortcut

You may also see this written with bitwise complement:

```java
int ins = i >= 0 ? i : ~i;   // ~i == -i - 1
```

Both `-i - 1` and `~i` recover the insertion point when `i` is negative.
