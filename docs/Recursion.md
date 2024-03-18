# 递归(Recursion)

## 1. 递归知识
### 1.1 递归函数的结构模板
1. base case: 递归必须有一个终止的条件，即不能无限循环地调用本身。
2. recursion relationship: 原问题可以分解为子问题，子问题和原问题的求解方法是一致的，即都是调用自身的同一个函数。

### 1.2 Recursion在计算机的实现方式
* 任何一个函数调用，计算机会在内存中生成一块区域，用于存放函数的参数，返回地址等，这块区域叫做"栈"(Stack)。
* 递归函数也是一种函数调用，因而也会生成一些列的stack。

### 1.3 递归形式
#### 1. Memorization (缓存)
Memorization缓存，将计算结果保存，避免重复计算。

Examples:
* LeetCode 509, 
* LeetCode 70

#### 2. Divide and Conquer (分治)
将一个大问题分解成小问题，各个击破，然后将小问题的解组合起来。与标准Recursion的区别在于，最后需要将子问题的结果进行合并。

* LeetCode 98

#### 3. Backtracking (回溯)
* 不断试错，知错就改
* 类似于暴力搜索，但比暴力搜索更高效(因为知错就改)

回溯问题的形式: 通常要求寻找所有满足Xxx条件的结果，并且问题可以使用递归实现。

* LeetCode 22

### 1.4 总结
* 递归是一种非常intuitive的解决复杂问题的方法。
* 递归分两步: Base Case + Recursion Relationship

* 递归遇到重复计算的情况: 使用memorization
* 递归遇到子问题组合的情况: 使用Divide and Conquer
* 递归要求返回所有满足条件的解答: 使用Backtracking


## 2. LeetCode题目


## Reference
* [【小小福讲算法】硅谷工程师十五分钟带你深入理解 Recursion （递归）算法，及其衍生出的算法（分治算法Divide and Conquer, 回溯 Backtracking）](https://www.youtube.com/watch?v=AqGagBmFXgw)
* [递归算法——超详细讲解（图文并茂）](https://blog.csdn.net/weixin_46312449/article/details/106792544)