# 动态规划 (Dynamic Programming)

## 算法解析
**动态规划(Dynamic Programming)**通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法。
动态规划常常适用于**有重叠子问题**和**最优子结构性质**的问题，动态规划方法所耗时间往往远少于朴素解法。
动态规划背后的基本思想非常简单。大致上，若要解一个给定问题，我们需要解其不同部分(即子问题)，再根据子问题的解以得出原问题的解。

**维基百科的概述:**
> 动态规划在查找有很多重叠子问题的情况的最优解时有效。它将问题重新组合成子问题。为了避免多次解决这些子问题，它们的结果都逐渐被计算并被保存，从简单的问题直到整个问题都被解决。因此，动态规划保存递归时的结果，因而不会在解决同样的问题时花费不必要的时间。
>
> 动态规划只能应用于有最优子结构的问题。最优子结构的意思是局部最优解能决定全局最优解（对有些问题这个要求并不能完全满足，故有时需要引入一定的近似）。简单地说，问题能够分解成子问题来解决。


**要点:**
* 动态规划常常适用于**有重叠子问题**和**最优子结构性质**的问题。
* 子问题重叠性质: 原问题可以分解为相对简单的子问题。
* 最优子结构性质: 如果问题的最优解所包含的子问题的解也是最优的，我们就称该问题具有最优子结构性质(即满足最优化原理)。


在算法上，**动态规划**和**查表的递归(也称记忆化递归)**有很多相似的地方。

## 记忆化递归
**递归**是指在函数中**调用函数自身**的方法。
有意义的递归通常会把问题分解成**规模缩小的同类子问题**，当子问题缩小到一步可以解决的时候，我们可以直接知道它的解(即base cases)。然后通过建立递归函数之间的联系(转移)即可解决原问题。

一个问题要使用**递归(recursion)**来解决必须有递归终止条件(算法的有穷性)，也就是说递归会逐步缩小到寻常规模。
:x:虽然下面代码也是递归，但是由于其无法结束，因此不算一个有效算法。如果没有外界干预，否则会永远执行下去，不会停止。
```python
def f(x):
    return x + f(x-1)
```
:white_check_mark:更多的情况应该是
```python
def f(n):
    if n == 1:
        return 1
    return n + f(n-1)
```
使用递归通常可以使代码短小，有时候也更可读。在算法中使用递归可以很简单地完成一些循环不太容易实现的功能，比如二叉树中的左中右序遍历。




**举例:**
* [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
> You are climbing a staircase. It takes n steps to reach the top.
> 
> Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



## Classic questions
* LCS: https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0
* LPS: https://leetcode.com/problems/longest-palindromic-subsequence/
* SCS: https://leetcode.com/problems/shortest-common-supersequence/


[1092. Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)   
**题目**: 给出两个字符串 str1 和 str2, 返回同时以 str1 和 str2 作为子序列的最短的字符串。    
**分析**: 1) 使用 `DP`，选出最长的公共子字符串(common subsequence)；2) 使用双指针，按照要求构成最短字符串。



References:
1. [Dynamic-Programming Interview questions.](https://leetcode.com/discuss/interview-question/344578/Dynamic-Programming-Interview-questions.)
2. [Longest Common Subsequence Problem](https://en.m.wikipedia.org/wiki/Longest_common_subsequence_problem)
3. [【算法面试通关40讲】43 - 理论理解：动态规划（上）&44 - 理论理解：动态规划（下）](https://blog.nowcoder.net/n/425f1a25e0684097928c0bd306b93079)
4. 
