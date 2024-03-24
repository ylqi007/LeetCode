[toc]


### Lowest Common Ancestor
* https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/editorial/
```Java
private TreeNode LCA(TreeNode node, TreeNode p, TreeNode q) {
    if (node == null || node == p || node == q)
        return node;
    TreeNode left = LCA(node.left, p, q);
    TreeNode right = LCA(node.right, p, q);
    if (left != null && right != null)
        return node;
    else if (left != null)
        return left;
    else
        return right;
}
```
* This solution doesn't account for the cases where `p` or `q` are not in the binary tree. 这个解法无法解决`p` or `q`不存在的特殊情况。
    * The stop condition for the recusion is `if(node == null || node == p || node == q) return node;`. This means that if we encounter `p`, we won't explore the subtree as we immediately return.
    * If `q` does not exist in the subtree of `p`, we will never know. 


### Top k frequency, Top k largest 问题
1. 如果input是offline的，即不会再添加新的member，那么可以使用Max-Heap
2. 如果是dynamically add elements，we often solve them by maintaining a `Min-Heap` of size k to store the largest k elements so far. Every time we enumerate a new element, just compare it with the top of the min heap and check if it is one of the largest k elements.
    * 因为对于Min-Heap而言，每次都是最小的element先被取出。

#### K-th问题
如果elements是逐步加入的，那么前N个elements中的k-th largest，是否就是所有elements中的k-th largests。**YES!**
Refer to [692. Top K Frequent Words -- Editorial](https://leetcode.com/problems/top-k-frequent-words/editorial/)


## Lowest Common Multiple(LCM) & Greatest Common Divisor(GCD)
```java
// Greatest Common Divisor, 最大公因数
private int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

// Lowest Common Multiple
long lcm = ((long) divisor1 * (long) divisor2) / gcd(divisor1, divisor2);   // 此处必须为(long)divisor1 * (long)divisor2,否则会有溢出问题
```


## Important Classes In Java
在刷LeetCode的过程中，有一些class是常用的，但是不同的它们的method可能还有一些区别。因此，列出来，要重点掌握
* [java.lang.Character](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Character.html)
* [java.lang.String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)
* [Interface java.util.Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)
* [Interface java.util.Comparator<T>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)
* [Interface java.lang.Comparable<T>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
* [Interface java.util.Deque<E>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Deque.html) [念做dai ke]
* [Class java.util.Random](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Random.html)
* [Class java.util.Arrays](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Arrays.html)
* [java.util.ArrayDeque<E>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayDeque.html) [`implement Deque`]
* [java.util.LinkedList<E>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedList.html)  [`implement Deque`, 以后尽量用 `Deque<E> deque = new LinkedList<>()`]
* [java.util.PriorityQueue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/PriorityQueue.html)
* [java.util.stream.Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)
* [Summary of regular-expression constructs](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html#sum)

**Note:**
* Removed from JDK11: [Class javafx.util.Pair<K,V>](https://docs.oracle.com/javase%2F9%2Fdocs%2Fapi%2F%2F/javafx/util/Pair.html)
* [Removed from JDK 11, JavaFX 11 arrives as a standalone module](https://www.infoworld.com/article/3308400/removed-from-jdk-11-javafx-11-arrives-as-a-standalone-module.html)
* [Five Alternatives To Pair Class In Java](https://xperti.io/blogs/java-pair-class-alternatives/)


**Reference**
* https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html
* [Convert Stream to an array in Java](https://www.techiedelight.com/convert-stream-array-java/#2)
* [Convert Integer List to an int array in Java](https://www.techiedelight.com/convert-list-integer-array-int/)
* [How can I convert List<Integer> to int[] in Java? [duplicate]](https://stackoverflow.com/questions/960431/how-can-i-convert-listinteger-to-int-in-java)
* [How to convert an ArrayList containing Integers to primitive int array?](https://stackoverflow.com/questions/718554/how-to-convert-an-arraylist-containing-integers-to-primitive-int-array?noredirect=1&lq=1)
