1. 链表知识：数据结构，复杂度
2. 链表题目
3. 总结

# Java List

## 1. `ArrayList`
The `ArrayList class` is a **resizable** array, which can be found in the `java.util` package.

The difference between a built-in array and an ArrayList in Java, is that the size of an array cannot be modified (if you want to add or remove elements to/from an array, you have to create a new one). While elements can be added and removed from an ArrayList whenever you want.
```java
import java.util.ArrayList; // import the ArrayList class

ArrayList<String> cars = new ArrayList<String>(); // Create an ArrayList object
```

### Reference
* https://www.w3schools.com/java/java_arraylist.asp
* https://docs.oracle.com/javase/8/docs/api/


## 2. `LinkedList`
The `LinkedList` class is almost identical to the ArrayList.

### 2.1 `ArrayList` vs. `LinkedList`
The `LinkedList` class is a collection which can contain many objects of the same type, just like the `ArrayList`.

The `LinkedList` class has all of the same methods as the `ArrayList` class because they both implement the `List` interface. This means that you can add items, change items, remove items and clear the list in the same way.

However, while the `ArrayList` class and the `LinkedList` class can be used in the same way, they are built very differently.

When To Use: Use an `ArrayList` for storing and accessing data, and `LinkedList` to manipulate data.

### 2.2 How the `ArrayList` works?
The `ArrayList` class has a regular array inside it. When an element is added, it is placed into the array. If the array is not big enough, a new, larger array is created to replace the old one and the old one is removed.

### 2.3 How the `LinkedList` works?
The `LinkedList` stores its items in "containers." The list has a link to the first container and each container has a link to the next container in the list. To add an element to the list, the element is placed into a new container and that container is linked to one of the other containers in the list.


## 链表 (Linked List)
* 基础知识：链表如何实现，如何遍历链表。链表可以保证头部尾部插入删除操作都是`O(1)`，查找任意元素位置`O(N)`
* 基础题目：
    * Leetcode 206. Reverse Linked ListLeetcode 
    * 876. Middle of the Linked List 
* 进阶题目：
    * Leetcode 160. Intersection of Two Linked Lists
    * Leetcode 141. Linked List Cycle (Linked List Cycle II)
    * Leetcode 92. Reverse Linked List II
    * Leetcode 328. Odd Even Linked List 
* 注意：快慢指针和链表反转几乎是所有链表类问题的基础，尤其是反转链表，代码很短，建议直接背熟。

## `LinkedHashMap`
`HashMap`是一种比较常用的，也比较好用的集合，但是`HashMap`有一个顺序的问题，就是在对`HashMap`进行迭代访问时，添加的顺序和访问的顺序可能就不一样的，这个时候我们可以选择`LinkedHashMap`，`LinkedHashMap`继承了`HashMap`，所以拥有和`HashMap`一样的功能；而且在此基础上有增加了一个双向链表来实现元素迭代的顺序，但是肯定会增加时间和空间的消耗。`LinkedHashMap`和`HashMap`一样，也是非线程安全的。

`Entry`就是`LinkedHashMap`基本数据结构，`Entry`是`LinkedHashMap`定义的一个内部类，继承了`HaspMap.Entry`，在此基础上添加了新添加了两个属性。`before`、`after`是用于维护链表中Entry的前一个元素和后一个元素。

`LinkedHashMap`提供了两种key的顺序：
* 访问顺序（access order）。非常实用，可以使用这种顺序实现LRU（Least Recently Used）缓存
* 插入顺序（insertion orde）。同一key的多次插入，并不会影响其顺序

总结：从以上可以判断LinkedHashMap的实现就是 HashMap+LinkedList 的实现方式，用HashMap维护数据结构，用LinkList的方式维护数据插入顺序。

* [java.util.LinkedHashMap<K,V>](https://docs.oracle.com/javase/8/docs/api/java/util/LinkedHashMap.html)
* [java之LinkedHashMap讲解](https://www.cnblogs.com/benwu/articles/7751640.html)
* [Java-LinkedHashMap原理探究](https://jiayi797.github.io/2018/01/29/Java-LinkedHashMap%E5%8E%9F%E7%90%86%E6%8E%A2%E7%A9%B6/)
* [Java LinkedHashMap源码解析](https://liujiacai.net/blog/2015/09/12/java-linkedhashmap/)
    * [Why exactly do we need a "Circular Linked List" (singly or doubly) data structure?](https://stackoverflow.com/questions/3589772/why-exactly-do-we-need-a-circular-linked-list-singly-or-doubly-data-structur)


## Problems
1. [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
2. [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
3. [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)


# 链表题目
带着问题去做下面的题目：

    在什么情况下，要用到哨兵节点（dummy node）？
    在什么情况下，循环条件要写 while (node != null)？什么情况下要写 while (node.next != null)？



## 1. 遍历链表


## 2. 删除节点
* [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/description/)
* [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description)
* [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)
* [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description)
* [2095. Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/)


### 3. 插入节点
* [2807. Insert Greatest Common Divisors in Linked List](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/)
* [147. Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/description/)
* [708. Insert into a Sorted Circular Linked List](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/)
* [2046. Sort Linked List Already Sorted Using Absolute Values](https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/description/)


### 4. 反转链表
* ✅[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
  * Iterative(空间上更优)
  * Recursive
* ✅[92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/description/)
* ✅[25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)
* [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/)
* [2074. Reverse Nodes in Even Length Groups](https://leetcode.com/problems/reverse-nodes-in-even-length-groups/description/)


### 5. 前后指针
* [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
* [61. Rotate List](https://leetcode.com/problems/rotate-list/description/)
* [1721. Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/)
* [1474. Delete N Nodes After M Nodes of a Linked List](https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/description/)


### 6. 快慢指针
* [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
* [2095. Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/)
* [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
* [2130. Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/)
* [143. Reorder List](https://leetcode.com/problems/reorder-list/description/)
* [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)
* [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
* ❌✅[457. Circular Array Loop](https://leetcode.com/problems/circular-array-loop/description/)
* ❌[2674. Split a Circular Linked List](https://leetcode.com/problems/split-a-circular-linked-list/description/)


### 7.双指针
* [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/description/)
* [86. Partition List](https://leetcode.com/problems/partition-list/description/)
* [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)


### 8. 合并链表
* [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
* [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/description/)
* [2816. Double a Number Represented as a Linked List](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/)
* [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
* [369. Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/description/)
* [1634. Add Two Polynomials Represented as Linked Lists](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/description/)


### 9. 分治
* [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
* [148. Sort List](https://leetcode.com/problems/sort-list/description/)


## 10. 综合应用
1019. 链表中的下一个更大节点
1171. 从链表中删去总和值为零的连续节点
707. 设计链表
* [146. LRU Cache](https://leetcode.com/problems/lru-cache/)
460. LFU 缓存
432. 全 O(1) 的数据结构
1206. 设计跳表


## Reference
* [【链表】Leetcode前400链表题目总结](https://blog.nowcoder.net/n/bcabe8d160ee4eefb394f2774de9bcfc)
* [【算法面试通关40讲】05 - 理论讲解：数组&链表](https://blog.nowcoder.net/n/1011b661e6374557b48f0b0550f51bb9)
* ✅灵茶山艾府: [分享丨【题单】链表、二叉树与回溯（前后指针/快慢指针/DFS/BFS/直径/LCA/一般树）](https://leetcode.cn/discuss/post/K0n2gO/)