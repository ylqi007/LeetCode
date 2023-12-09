# Stack
## Knowledge
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



* [java.util.Vector<E>](https://docs.oracle.com/javase/8/docs/api/java/util/Vector.html)
* [java.util.Stack<E>](https://docs.oracle.com/javase/8/docs/api/java/util/Stack.html)
* [Java 全栈知识体系: Collection - Stack & Queue 源码解析](https://pdai.tech/md/java/collection/java-collection-Queue&Stack.html)
* [Java中Stack栈用foreach,迭代器访问的坑](https://blog.csdn.net/qq_43778308/article/details/108483525)


* [Java里的堆(heap)栈(stack)和方法区(method)](https://www.cnblogs.com/fmgao-technology/p/11095873.html) --> JVM, 与此处的`Stack`相关性不大





## Problem
* [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
