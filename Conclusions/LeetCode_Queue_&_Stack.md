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


## 3. Stack: Last-in-first-out Data Structure

### 3.1 LIFO structure
> In a LIFO data structure, **the newest element added to the queue will be processed first**.
> Operation:
> * push()
> * pop()

### 3.2 Stack usage
> Most popular languages provide built-in stack library so you don't have to reinvent the wheel.

[Min Stack]()
[Valid Parentheses]()
[Daily Temperatures]()
[Evaluate Reverse Polish Notation]()


## 4. Stack and DFS
### 4.1 Stack and DFS
> Similar to BFS, `Depth-First Search(DFS)` can also be used to find the path from the root node to the target node.
>
> Insights:
> 1. What is the processing order of the nodes? Overall, we **only** track-back and try another path after we reach the **deepest** node.
> 2. What is the push and pop order of the stack? The processing order of the nodes is the **exact opposite order** as how they were **added* to the stack, 
> which is **Last-In-First-Out(LIFO)**. That's why we use a stack in DFS.

### 4.2 DFS - Template 1 (Recursion)
> In most cases, we can also use `DFS` when using `BFS`. But there is an important difference: `the traversal order`.
> 
> Different from `BFS`, **the nodes you visit earlier might not be the nodes which are closer to the root node**.
> As a result, the first path you found in `DFS` might not be the shortest path.

* Template - Recursion
```java 
/*
 * Return true if there is a path from cur to target.
 */
boolean DFS(Node cur, Node target, Set<Node> visited) {
    return true if cur is target;
    for (next : each neighbor of cur) {
        if (next is not in visited) {
            add next to visted;
            return true if DFS(next, target, visited) == true;
        }
    }
    return false;
}
```
> It seems like we don't have to use any stacks when we implement `DFS` recursively.
> But actually, we are using the **implicit stack** provided by the system, also known as teh [Call Stack](https://en.wikipedia.org/wiki/Call_stack).
>
> **Each element costs constant space. And the size of the stack is exactly the depth of the DFS**.
> So in the worst case, it costs `O(h)` to maintain the system stack, where `h` is the maximum depth of DFS.
> You should never forget to take the system stack into consideration when calculating the space complexity.        
> 1. 每个 element node 所占的空间是一定的，则 stack 的大小取决于 DFS 的深度，所以需要 `O(h)` 的空间去维持 `system stack`，`h` 是 DFS 的最大深度。
> 2. 考虑 Space Complexity 的时候，要记得将 **system stack** 考虑在内。
>
> In the template above, we stop when we find the `first` path.     
> What if you want to find the `shortest` path? **Hint:** Add one more parameter to indicate the shortest path you have already found.

[200. Number of Islands]()
[Clone Graph]()
[Target Sum]()

### 4.3 DFS - Template 2 (Using an explicit stack)
> The advantage of the recursion solution is that it is easier to implement.
> However, there is a huge disadvantage: if the depth of recursion is too high, you will suffer from `stack overflow`.
> In that case, you might want to use BFS instead or implement DFS using an explicit stack.

* Template - Explicit stack
```java 
/*
 * Return true if there is a path from cur to target.
 */
boolean DFS(int root, int target) {
    Set<Node> visited;
    Stack<Node> stack;
    add root to stack;
    while (s is not empty) {
        Node cur = the top element in stack;
        remove the cur from the stack;
        return true if cur is target;
        for (Node next : the neighbors of cur) {
            if (next is not in visited) {
                add next to visited;
                add next to stack;
            }
        }
    }
    return false;
}
```
> The logic is exactly the same with the recursion solution.
> But we use `while-loop` and `stack` to simulate the `system call stack` during recursion.
> Running through several examples manully will definitely help you understand it better.  

[Binary Tree Inorder Traversal]()


## 5. Conclusion
[Implementing Queue using Stacks]()
[Implementing Stack using Queues]()
[Decoding String]()
[Flood Fill]()
[01 Matrix]()
[Keys and Rooms]()

