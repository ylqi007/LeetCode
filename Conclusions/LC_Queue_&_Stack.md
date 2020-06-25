# Queue & Stack

## 0. Introduction
> We may access a *random* element by index in **Array**. However, we might want to **restrict the processing order** in some cases.            
> [在某些情况中，我们需要随机访问一个元素，此时可以用 Array。在另一些情况下，我们需要按照特定的顺序访问元素，比如 `FIFO` or `LIFO`，相应的就有两种数据结构 `Queue` and `Stack`。]


## 1. Queue: First-In-First-Out Data Structure

### 1.1 First-In-First-Out
* **First-In-First-Out** (FIFO) + **Queue**
* Goal:
    * Understand the *definition* of FIFO and queue;
    * Be able to implement a queue by yourself;
    * Be familiar with the built-in queue structure;
    * Use queue to solve the simple problems.
* In a FIFO data structure, **the first element added to the queue will be processed first**:
    * **enqueue:** The new element is always added at the end of the queue.
    * **dequeue:** The delete operation is called dequeue. You are only allowed to remove the first element.   


### 1.2 Queue Implementation
* To implement a queue, we may use a dynamic array and an index pointing to the head of the queue. For example, the `ArrayList`.
* Two operation:
    * `enqueue`
    * `dequeue`: We need an index to indicate the starting point.

Drawback:
* With the movement of the start pointer, more and more space is wasted. And it will be unacceptable when we only have a space limitation.


### 1.3 Circular Queue
* A more efficient way is to use a circular queue. Specifically, we may use `a fixed-size array` and `two pointers` to indicate the starting and ending position.
* And the goal is to **reuse the waster storage**.
* Need to check if a queue is `empty` or `full`.


### 1.4 Design Circular Queue
[622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)

> The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. 
> It is also called **Ring Buffer**.
> The implementation should support the following operations:
> * `MyCircularQueue(k)`
> * `Front`
> * `Rear`
> * `enQueue(x)`
> * `deQueue()`
> * `isEmpty()`
> * `isFull()`


### 1.5 Circular Queue -- Implementation
> An `array` with two pointers, `head` and `tail`.


### 1.6 Moving Average from Data Stream
[346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)


## 2. Queue and BFS
[286. Walls and Gates]()        
[200. Number of Islands]()        
[752. Open the Lock](https://leetcode.com/problems/open-the-lock/)        
[Perfect Squares]()        

### 2.1 Queue and BFS
> One common application of Breadth-First Search (BFS) is to find the shortest path from the root node to the target node.

1). What is the processing order of the nodes?
Similar to tree's level-order traversal, the nodes closer to the root node will be traversed earlier.

2). What is the enqueue and dequeue order of the queue?

### 2.2 BFS -- Template
> It will be important to determine the nodes and the edges before doing BFS in a specific question.
> Typically, the node will be an actual node or a status while the edge will be an actual edge or a possible transition.

* Template I:
```java 
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    // BFS
    while (queue is not empty) {
        step = step + 1;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                add next to queue;
            }
            remove the first node from queue;
        }
    }
    return -1;          // there is no path from root to target
}
```

* Template II:
> Sometimes, it is important to make sure that we never visit a node twice. Otherwise, we might get stuck in an infinite loop, e.g. in graph with cycle.
```java 
/**
 * Return the length of the shortest path between root and target node.
 */
int BFS(Node root, Node target) {
    Queue<Node> queue;  // store all nodes which are waiting to be processed
    Set<Node> visited;  // store all the nodes that we've visited
    int step = 0;       // number of steps neeeded from root to current node
    // initialize
    add root to queue;
    add root to visited;
    // BFS
    while (queue is not empty) {
        step = step + 1;
        // iterate the nodes which are already in the queue
        int size = queue.size();
        for (int i = 0; i < size; ++i) {
            Node cur = the first node in queue;
            return step if cur is target;
            for (Node next : the neighbors of cur) {
                if (next is not in visited) {
                    add next to queue;
                    add next to visited;
                }
                remove the first node from queue;   
            }
        }
    }
    return -1;          // there is no path from root to target
}
```

There are some cases where one does not need to keep the `visited` hash set:
1. You are absolutely sure there is no cycle, for example, in tree traversal;
2. You do want to add the node to the queue multiple times.

