
## ArrayDeque: `java.util.ArrayDeque<E>`
* Java11: https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/ArrayDeque.html
  > * Array deques have no capacity restrictions; they grow as necessary to support usage.
  > *  They are not thread-safe; in the absence of external synchronization, they do not support concurrent access by multiple threads
  > * Null elements are prohibited. 不能添加`null` object
  > * This class is likely to be faster than Stack when used as a stack, and faster than LinkedList when used as a queue.
    * Stack: push/pop/peek, 可以用`push
* ArrayDeque (Stack, Queue)
    * 🟩🌟二哥的Java进阶之路: [Java集合框架全面解析](https://javabetter.cn/collection/gailan.html)
    * [ArrayDeque介绍&&不推荐使用Stack类](https://blog.csdn.net/weixin_45713992/article/details/127574159)
    * [为什么JDK建议使用ArrayDeque而不是Stack和LinkedList实现栈和队列](https://www.cnblogs.com/jiading/articles/12452830.html)
    * [详解 Java 中的双端队列（ArrayDeque附源码分析）](https://javabetter.cn/collection/arraydeque.html)
    * [Java中的栈Stack、Deque、ArrayDeque、LinkedList](https://blog.csdn.net/linysuccess/article/details/109038453)


## PriorityQueue: `java.util.PriorityQueue<E>` (i.e. Heap)
* https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/PriorityQueue.html
    * An unbounded priority queue based on a priority heap. The elements of the priority queue are ordered according to their natural ordering, or by a Comparator provided at queue construction time, depending on which constructor is used.
        * 基于queue，自然排序(即从小到大)
    * A priority queue does not permit null elements.
        * 不能存放null
    * `boolean add(E e) 	Inserts the specified element into this priority queue.`
    * `boolean remove(Object o) 	Removes a single instance of the specified element from this queue, if it is present.`
* `PriorityQueue`和`Queue`的区别在于，它的出队顺序与元素的优先级有关，对`PriorityQueue`调用`remove()`或`poll()`方法，返回的总是优先级最高的元素。
* [10 张手绘图详解Java 优先级队列PriorityQueue](https://javabetter.cn/collection/PriorityQueue.html)

```java
// PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
// PriorityQueue<Integer> minHeap = new PriorityQueue<>();

import java.util.PriorityQueue;

public class PriorityQueueExample {

    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();  // default, minHeap, the min number will be polled out first

        pq.add(5);
        pq.add(2);
        pq.add(8);
        pq.add(1);

        while (!pq.isEmpty()) {
            System.out.println(pq.poll()); // Output: 1, 2, 5, 8
        }
    }
}
```