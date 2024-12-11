# 动态规划 (Dynamic Programming)

## 算法解析
**动态规划(Dynamic Programming)**通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法。
动态规划常常适用于**有重叠子问题**和**最优子结构性质**的问题，动态规划方法所耗时间往往远少于朴素解法。
动态规划背后的基本思想非常简单。大致上，若要解一个给定问题，我们需要解其不同部分(即子问题)，再根据子问题的解以得出原问题的解。

所以动态规划中每一个状态一定是由上一个状态推导出来的，这一点区分于贪心算法，贪心算法没有状态推导，而是从局部直接选最优的。
* 动态规划，由前一个状态推导出来的。
* 贪心算法则是局部直接选最优。

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


## 动态规划的解题步骤
对于动态规划问题，可以拆解为以下五步:
1. 确定dp数组(dp table)以及下标的含义
2. 确定递推公式
3. dp数组如何初始化
4. 确定遍历顺序
5. 举例推导dp数组



## Classic questions
* LCS: https://practice.geeksforgeeks.org/problems/longest-common-subsequence/0
* LPS: https://leetcode.com/problems/longest-palindromic-subsequence/
* SCS: https://leetcode.com/problems/shortest-common-supersequence/


## LeetCode题目
* [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
* [139. Word Break](https://leetcode.com/problems/word-break/)
  * [教你一步步思考 DP：从记忆化搜索到递推，附题单！（Python/Java/C++/Go/JS/Rust）](https://leetcode.cn/problems/word-break/solutions/2968135/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-chrs/)
* [140. Word Break II](https://leetcode.com/problems/word-break-ii/)
* [1092. Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)   
  * **题目**: 给出两个字符串 str1 和 str2, 返回同时以 str1 和 str2 作为子序列的最短的字符串。    
  * **分析**: 1) 使用 `DP`，选出最长的公共子字符串(common subsequence)；2) 使用双指针，按照要求构成最短字符串。
* [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/)
* [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
* [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
* ✅ [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

### 1. 斐波那契数列
1. []()

### Best Time to Buy and Sell Stock
* [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
  * [力扣: 暴力解法、动态规划（Java）](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/solutions/38477/bao-li-mei-ju-dong-tai-gui-hua-chai-fen-si-xiang-b/)
* [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
* [123. Best Time to Buy and Sell Stock III]
* [188. Best Time to Buy and Sell Stock IV]


## 动态规划应该如何debug
* 找问题的最好方式就是把dp数组打印出来，看看究竟是不是按照自己的思路推导的。
* 做动态规划的题目，写代码之前一定要把状态转移在dp数组上的具体情况模拟一遍，心中有数，确定最后推导出的是想要的结果。


References:
1. [Dynamic-Programming Interview questions.](https://leetcode.com/discuss/interview-question/344578/Dynamic-Programming-Interview-questions.)
2. [Longest Common Subsequence Problem](https://en.m.wikipedia.org/wiki/Longest_common_subsequence_problem)
3. [【算法面试通关40讲】43 - 理论理解：动态规划（上）&44 - 理论理解：动态规划（下）](https://blog.nowcoder.net/n/425f1a25e0684097928c0bd306b93079)
4. [力扣: 经典动态规划问题（理解「无后效性」）](https://leetcode.cn/problems/maximum-subarray/solutions/9058/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/)
5. [代码随想录: 动态规划理论基础](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.md)
6. [代码随想录: 动态规划最强总结篇！](https://github.com/youngyangyang04/leetcode-master/blob/master/problems/%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E6%80%BB%E7%BB%93%E7%AF%87.md)
7. [告别动态规划，连刷 40 道题，我总结了这些套路，看不懂你打我（万字长文）](https://zhuanlan.zhihu.com/p/91582909)
8. [Leetcode 题解 - 动态规划](https://gitcode.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92.md#0-1-%E8%83%8C%E5%8C%85?utm_source=csdn_github_accelerator)
9. Bilibili: [动态规划入门：从记忆化搜索到递推](https://www.bilibili.com/video/BV1Xj411K7oF/)
10. [教你一步步思考 DP：从记忆化搜索到递推，附题单！（Python/Java/C++/Go/JS/Rust）](https://leetcode.cn/problems/word-break/solutions/2968135/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-chrs/)
