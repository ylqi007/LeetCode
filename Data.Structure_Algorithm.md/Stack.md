# Stack
## `Stack`
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


* [java.util.Vector<E>](https://docs.oracle.com/javase/8/docs/api/java/util/Vector.html)
* [java.util.Stack<E>](https://docs.oracle.com/javase/8/docs/api/java/util/Stack.html)
* [Interface java.util.Deque<E>](https://docs.oracle.com/javase/8/docs/api/java/util/Deque.html)
* [java.util.ArrayDeque<E>](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayDeque.html)
* [Java 全栈知识体系: Collection - Stack & Queue 源码解析](https://pdai.tech/md/java/collection/java-collection-Queue&Stack.html)
* [Java中Stack栈用foreach,迭代器访问的坑](https://blog.csdn.net/qq_43778308/article/details/108483525)


* [Java里的堆(heap)栈(stack)和方法区(method)](https://www.cnblogs.com/fmgao-technology/p/11095873.html) --> JVM, 与此处的`Stack`相关性不大


## Problem
* [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
