# 回溯算法 (backtracking algorithm)
解决一个回溯问题，实际上就是一个**决策树的遍历过程**。在此过程中，我们需要考虑3个问题：
1. 路径：依旧是已经做出的选择。
2. 选择列表：当前可以做的选择。
3. 结束条件：到达决策层底层，无法再做选择的条件。

```
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
```
其核心就是 for 循环里面的递归，在递归调用之前**「做选择」**，在递归调用之后**「撤销选择」**。


回溯算法（backtracking algorithm）是一种通过**穷举**来解决问题的方法，它的核心思想是从一个初始状态出发，暴力搜索所有可能的解决方案，当遇到正确的解则将其记录，直到找到解或者尝试了所有可能的选择都无法找到解为止。

回溯算法通常采用“深度优先搜索”来遍历解空间。

✅ **回溯三步曲：**
1. 明确「路径」和「选择列表」
2. 递归 + 回退（恢复现场）
3. 剪枝优化，防止重复 / 超时


# [6 Introduction to Backtracking - Brute Force Approach](https://www.youtube.com/watch?v=DKCbsiDBN6c&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=63)
* Backtracking uses brute force strategy.
* Brute force is the strategy that you try up all possible solutions and pick up desired solutions.
* 在 DP 算法中，也用动  Brute Force 的思想，但是最终的要求是 optimial solution。
* 在 BT 用在有多种 solutions 并且要求返回所有的 solutions。
* State Space Tree
* Backtracking follows **DFS**
* Branch and Bound follows **BFS**
* [6.1 N Queens Problem using Backtracking](https://www.youtube.com/watch?v=xFv_Hl4B83A&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=64)
    * **Boundary Function**: Not in the same row, column and diagonal.
* [6.2 Sum Of Subsets Problem - Backtracking](https://www.youtube.com/watch?v=kyLxTdsT8ws&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=65)
    * `0/1` means excluding/including.
* [6.3 Graph Coloring Problem - Backtracking](https://www.youtube.com/watch?v=052VkKhIaQ4&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=66)
    * M coloring optimization problem
* [6.4 Hamiltonian Cycle - Backtracking](https://www.youtube.com/watch?v=dQr4wZCiJJ4&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=67)


## [leetcode解题笔记：backtracking类型解题思路](https://blog.csdn.net/crystal6918/article/details/51924665)
> **基本概念:** backtracking（回溯算法）也叫试探法，它是一种系统地搜索问题的解的方法。回溯算法的基本思想是：从一条路往前走，能进则进，不能进则退回来，换一条路再试。
> 回溯算法说白了就是穷举法。不过回溯算法使用剪枝函数，剪去一些不可能到达最终状态（即答案状态）的节点，从而减少状态空间树节点的生成。
> * 回溯法在用来求问题的所有解时，要回溯到根，且根结点的所有子树都已被搜索遍才结束。
> * 而回溯法在用来求问题的任一解时，只要搜索到问题的一个解就可以结束。
    > 这种**以深度优先的方式**系统地搜索问题的解的算法称为回溯法，它适用于解一些组合数较大的问题。





1. [51. N-Queens](https://leetcode.com/problems/n-queens/)
2. [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)
3. [78. Subsets](https://leetcode.com/problems/subsets/)
4. [90. Subsets II](https://leetcode.com/problems/subsets-ii/)
5. [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
6. [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
7. [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)
8. [46. Permutations](https://leetcode.com/problems/permutations/)
9. [47. Permutations II](https://leetcode.com/problems/permutations-ii/)
10. [77. Combinations](https://leetcode.com/problems/combinations/)
11. [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
12. [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
13. [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)



## [[Leetcode] Backtracking回溯法(又称DFS,递归)全解](https://segmentfault.com/a/1190000006121957)
* 一般回溯的问题有三种：
    1. Find a path to success 有没有解
        * [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
    2. Find all paths to success 求所有解
        * 求所有解的个数
            * [51. N-Queens](https://leetcode.com/problems/n-queens/)
        * 求所有解的集体信息
            * [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)
            * [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
    3. Find the best path to success 求最优解

## [[树/链表/图] 谈一谈backtracking算法](https://www.1point3acres.com/bbs/thread-583166-1-1.html)

## Permutation (排列) & Combination (组合)
![](images/Permutations-and-Combinations.webp)


## 回溯分类
### 1. 子集型回溯
**两种思路:**
1. 对于当前元素，选 or 不选
2. 站在答案角度，每次必须选一个。但是为了避免 `[1,2], [2,1]`这种重复，只能增量去选，即，这次选了 `i`，下次只能从 `i+1` 开始选。

**子集型回溯题目:**
* [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
* [78. Subsets](https://leetcode.com/problems/subsets/)
* [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)


### 2. 组合型回溯
可以优化的点
1. 剪枝, pruning

* [77. Combinations](https://leetcode.com/problems/combinations/)
* [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)
* [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)


### 3. 排列型回溯
* [46. Permutations](https://leetcode.com/problems/permutations/)
* [51. N-Queens](https://leetcode.com/problems/n-queens/)
* [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)


## Top Interview 150
* [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
* [77. Combinations](https://leetcode.com/problems/combinations/)
* 



## LeetCode题目
* [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
* ✅ [489. Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/)
* [79. Word Search](https://leetcode.com/problems/word-search/description/)
    * [489. Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/description/)
* [212. Word Search II](https://leetcode.com/problems/word-search-ii/description/)
* [78. Subsets](https://leetcode.com/problems/subsets/)
* [90. Subsets II](https://leetcode.com/problems/subsets-ii/)


## Top 100 Liked
* [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
* [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
* [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
* [46. Permutations](https://leetcode.com/problems/permutations/)


## Reference
* Hello 算法: [13.1   回溯算法](https://www.hello-algo.com/chapter_backtracking/backtracking_algorithm/)
* ✅ [力扣: 回溯算法（Java）](https://leetcode.cn/problems/word-search/solutions/12096/zai-er-wei-ping-mian-shang-shi-yong-hui-su-fa-pyth/)
* [带你学透回溯算法（理论篇）| 回溯法精讲！](https://www.bilibili.com/video/BV1cy4y167mM/?spm_id_from=333.337.search-card.all.click&vd_source=bd5e1cdd20d83feef8e77a781b33f083)
* [leetcode解题笔记：backtracking类型解题思路](https://blog.csdn.net/crystal6918/article/details/51924665)
* [算法漫游指北（第十篇）:泛型递归、递归代码模板、递归思维要点、分治算法、回溯算法](https://www.cnblogs.com/Nicholas0707/p/13138193.html#_label2)
* [6 Introduction to Backtracking - Brute Force Approach](https://www.youtube.com/watch?v=DKCbsiDBN6c&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=63)
* [[树/链表/图] 谈一谈backtracking算法](https://www.1point3acres.com/bbs/thread-583166-1-1.html)
* ✅灵茶山艾府: [回溯算法套路①子集型回溯【基础算法精讲 14】](https://www.bilibili.com/video/BV1mG4y1A7Gu)
* ✅灵茶山艾府: [回溯算法套路②组合型回溯+剪枝【基础算法精讲 15】](https://www.bilibili.com/video/BV1xG4y1F7nC)
* ✅灵茶山艾府: [回溯算法套路③排列型回溯+N皇后【基础算法精讲 16】](https://www.bilibili.com/video/BV1mY411D7f6)
* [回溯算法详解](https://github.com/jiajunhua/labuladong-fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E8%AF%A6%E8%A7%A3%E4%BF%AE%E8%AE%A2%E7%89%88.md)