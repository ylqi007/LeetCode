## [6 Introduction to Backtracking - Brute Force Approach](https://www.youtube.com/watch?v=DKCbsiDBN6c&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=63)
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




## References:
* [leetcode解题笔记：backtracking类型解题思路](https://blog.csdn.net/crystal6918/article/details/51924665)
* [算法漫游指北（第十篇）:泛型递归、递归代码模板、递归思维要点、分治算法、回溯算法](https://www.cnblogs.com/Nicholas0707/p/13138193.html#_label2)
* [6 Introduction to Backtracking - Brute Force Approach](https://www.youtube.com/watch?v=DKCbsiDBN6c&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=63)
* [[树/链表/图] 谈一谈backtracking算法](https://www.1point3acres.com/bbs/thread-583166-1-1.html)
* []()
* []()
* []()
* 