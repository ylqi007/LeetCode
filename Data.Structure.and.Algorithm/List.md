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


## Reference
* [【链表】Leetcode前400链表题目总结](https://blog.nowcoder.net/n/bcabe8d160ee4eefb394f2774de9bcfc)
* [【算法面试通关40讲】05 - 理论讲解：数组&链表](https://blog.nowcoder.net/n/1011b661e6374557b48f0b0550f51bb9)