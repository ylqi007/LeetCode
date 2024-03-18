# Stack
## `Stack` (First-In-First-Out, FIFO)
> The `Stack` class represents a last-in-first-out (LIFO) stack of objects. It extends class `Vector` with five operations that allow a vector to be treated as a stack.
> When a stack is first created, it contains no items. 
> A more complete and consistent set of LIFO stack operations is provided by the Deque interface and its implementations, which should be used in preference to this class. For example: 
> 
> `Deque<Integer> stack = new ArrayDeque<Integer>();`

`Stack`是一种只能在一端进行插入or删除操作的线性表。

Java里有一个叫做`Stack`的类，却没有叫做`Queue`的类(它是个接口名字)。**当需要使用栈时，Java已不推荐使用Stack，而是推荐使用更高效的ArrayDeque**；既然Queue只是一个接口，当需要使用队列时也就首选ArrayDeque了(次选是LinkedList)。

```bash
# Tests if this stack is empty.
boolean empty()

# Looks at the object at the top of this stack without removing it from the stack.
E peek()

# Removes the object at the top of this stack and returns that object as the value of this function.
E pop()

# Pushes an item onto the top of this stack.
E push(E item)

# Returns the 1-based position where an object is on this stack.
int search(Object o)
```


## Stack的实现方式
遗留类`java.util.Stack`为了复用`Vector`中的方法，来实现进栈(push)、出栈(pop)等操作，所以继承了`java.util.Vector`。这就是`java.util.Stack`设计不好的地方，为了复用简单的方法而迫使它继承`Vector`。

后来Java修正了这个不良好的设计，提出了用`java.util.Deque`代替`java.util.Stack`的建议。
```Java
Deque<Integer> stack = new ArrayDeque<Integer>();
```
操作`Deque`的方法有：
* 把元素压栈：`push(E)`
* 把栈顶的元素“弹出”：`pop()`
* 取栈顶元素但不弹出：`peek()`
* 把栈**顶**元素”弹出”：`remove()`
* 把栈**底**元素”弹出”：`removeLast()`


## `Deque` and `ArrayDeque`
> A linear collection that supports element insertion and removal at both ends. The name deque is short for "double ended queue" and is usually pronounced "deck".
> 
> This interface defines methods to access the elements at both ends of the deque. Methods are provided to insert, remove, and examine the element. Each of these methods exists in two forms: one throws an exception if the operation fails, the other returns a special value (either null or false, depending on the operation). The latter form of the insert operation is designed specifically for use with capacity-restricted Deque implementations; in most implementations, insert operations cannot fail. 
```Java
public void main{
    Deque<Integer> stack = new ArrayDeque<Integer>();

    // Returns true if this deque contains no elements.
    boolean isEmpty()

    // add and get
    // Inserts the specified element at the front of this deque.
    void addFirst(E e)
    // Inserts the specified element at the end of this deque.
    void addLast(E e)

    // Retrieves, but does not remove, the first element of this deque.
    E getFirst()
    // Retrieves, but does not remove, the last element of this deque.
    E getLast()

    // Retrieves, but does not remove, the head of the queue represented by this deque, or returns null if this deque is empty.
    E peek()
    // Retrieves, but does not remove, the first element of this deque, or returns null if this deque is empty.
    E peekFirst()
    // Retrieves, but does not remove, the last element of this deque, or returns null if this deque is empty.
    E peekLast()

    // Retrieves and removes the head of the queue represented by this deque (in other words, the first element of this deque), or returns null if this deque is empty.
    E poll()
    // Retrieves and removes the first element of this deque, or returns null if this deque is empty.
    E pollFirst()
    // Retrieves and removes the last element of this deque, or returns null if this deque is empty.
    E pollLast()

    // Pops an element from the stack represented by this deque.
    E pop()
    // Pushes an element onto the stack represented by this deque.
    void push(E e)
}
```


### Stack
- [x] [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)    **DP**
- [x] [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)     **Stack**
- [x] [1249. Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)
- [x] [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)    **DP, Stack**
- [x] [394.Decode String](https://leetcode.com/problems/decode-string/)    **Stack**
- [x] [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/)
- [x] [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/)
- [x] [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/)
- [ ] [770. Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv/)
- [x] [155. Min Stack](https://leetcode.com/problems/min-stack/)  **Stack, Stack + One Integer**
- [x] [716. Max Stack](https://leetcode.com/problems/max-stack/)  **Stack, Doubly Linked List + TreeMap**
- [x] [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)   **Stack**
- [x] [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)   **Arrays, base on LC84**
- [x] [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
- [x] [1209. Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)


#### 题目类型
* Basic Calculators
    1. [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) [`+, -, *, /`]
    2. [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/) [非常好的Stack题目, with parenthesis, `+, -` and `(, )`]
    3. [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) [With parenthesis, `+, -, *, /` and `(, )`]
    4. [Basic Calculator Template](https://leetcode.com/problems/basic-calculator-iii/solutions/344371/Java-Common-template-for-Basic-Calculator-I-II-and-III-using-Stack/)
* Decode string
    1. [394. Decode String](https://leetcode.com/problems/decode-string/)
    2. [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)
    3. [71. Simplify Path](https://leetcode.com/problems/simplify-path/description/)

#### Monotonic Stack
1. [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)
2. [901. Online Stock Span](https://leetcode.com/problems/online-stock-span/description/)


## Problem
LC 20, 71都是比较直接的Stack problem；LC 42，84，85需要额外的思考再用Stack解决，不过这三题都有相同的思路，可以使用同一个template解决。
* [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
* [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
* [71. Simplify Path](https://leetcode.com/problems/simplify-path/)
* [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
* [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
* ""
* [456. 132 Pattern](https://leetcode.com/problems/132-pattern/)
* [735. Asteroid Collision](https://leetcode.com/problems/asteroid-collision/)
* [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
* [155. Min Stack](https://leetcode.com/problems/min-stack/)
* [1472. Design Browser History](https://leetcode.com/problems/design-browser-history/)


## Monotonic Stack (单调栈)
1. A monotonic stack is simply a stack where the elements are always in sorted order. Monotonic **decreasing** means that the stack will always be sorted in descending order.
单调栈是一个维持单调递增or递减的Stack。
2. 所谓**单调栈**，没有现成的方法和类，需要自己去实现。其思想就是每次进行入栈操作(push)时，如果要入栈的元素大于(or小于)栈顶元素，那么就将其弹出，直到栈顶元素大于(or小于)即将入栈的元素。
[Ref](https://www.zhihu.com/tardis/zm/art/518743572?source_id=1003)


### Problems 1: 维护一个单调递减的栈
1. LC 42
2. LC 496
3. LC 503, 
4. LC 739
5. LC 901,
6. LC 239

### Problems 2: 维护一个单调递增的栈
1. 84


### Reference
* [Editorial of 739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/editorial/)
* [Editorial of 901. Online Stock Span](https://leetcode.com/problems/online-stock-span/description/)
* [907. Sum of Subarray Minimums. Stack solution with very detailed explanation step by step](https://leetcode.com/problems/sum-of-subarray-minimums/solutions/178876/stack-solution-with-very-detailed-explanation-step-by-step/)
* [907. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/description/)
* [LeetCode 单调栈/单调队列 总结](https://www.zhihu.com/tardis/zm/art/518743572?source_id=1003)
* [LeeCode 栈与队列专题总结](https://blog.csdn.net/weixin_40910614/article/details/120378512)
* [java.util.Vector<E>](https://docs.oracle.com/javase/8/docs/api/java/util/Vector.html)
* [java.util.Stack<E>](https://docs.oracle.com/javase/8/docs/api/java/util/Stack.html)
* [Interface java.util.Deque<E>](https://docs.oracle.com/javase/8/docs/api/java/util/Deque.html)
* [java.util.ArrayDeque<E>](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html)
* [Java 全栈知识体系: Collection - Stack & Queue 源码解析](https://pdai.tech/md/java/collection/java-collection-Queue&Stack.html)
* [Java中Stack栈用foreach,迭代器访问的坑](https://blog.csdn.net/qq_43778308/article/details/108483525)
* [Java里的堆(heap)栈(stack)和方法区(method)](https://www.cnblogs.com/fmgao-technology/p/11095873.html) --> JVM, 与此处的`Stack`相关性不大