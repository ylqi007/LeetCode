[TOC]

---
## 1. Data Structure

### Array-TODO






### Tree
* Traversal
- [x] [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)  **recursion + iteration, morris**
- [x] [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) **recursion + iteration, morris**
- [x] [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)  **recursion + iteration**
- [x] [589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)  **1.注意 iterative 的写法，基于 Stack 实现；   2.recursion**
- [x] [590. N-ary Tree Postorder Traversal](https://leetcode.com/problems/n-ary-tree-postorder-traversal/)  **1.注意 iterative 的写法，基于 Stack 实现；   2.recursion**
- [x] [314. Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal/)  **Pair; Two Queue**
- [x] [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)  **BFS; recursion**
- [x] [107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)   **LinkedList.addFirst(); Collections.reverse()**
- [x] [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
- [x] [429. N-ary Tree Level Order Traversal](https://leetcode.com/problems/n-ary-tree-level-order-traversal/) **BFS; Recursion**

- [x] [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- [x] [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
- [x] [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [x] [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)
- [x] [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

* Search
- [x] 700.Search in a Binary Search Tree        : recuresion + iteration
- [x] 270.Closest Binary Search Tree Value      : recuresion + iteration
- [x] 272.Closest Binary Search Tree Value II   : stack
- [x] 230.Kth Smallest Element in a BST         : inorder traversal(recursion, iteration)
- [x] 671.Second Minimum Node in a Binary Tree  : 
- [x] 255.Verify Preorder Sequence in Binary Search Tree    : recuresion + iteration
* Merge, Split, Delete and Insert
- [x] 617.Merge Two Binary Trees    : recursion + iteration
- [x] 776.Split BST
- [x] 450.Delete Node in a BST      : predecessor & successor
- [x] 701.Insert into a Binary Search Tree  : recursion + iteration
* Depth
- [x] 104.Maximum Depth of Binary Tree      : BFS, DFS, Recursion
- [x] 111.Minimum Depth of Binary Tree      : BFS, Recursion
- [x] 110.Balanced Binary Tree              : top down approach + bottom up approach
- [x] 559.Maximum Depth of N-ary Tree       : recursion, DFS, BFS
- [x] 637.Average of Levels in Binary Tree  :
- [x] 993.Cousins in Binary Tree
- [ ] 222.Count Complete Tree Nodes         : Recursion, Binary Search 
* Others
- [x] 98.Validate Binary Search Tree
- [x] 501.Find Mode in Binary Tree          : Follow up, no extra space. Inorer traversal: 升序


- [x] 426.Convert Binary Search Tree to Sorted Doubly Linked List
- [x] 783.Minimum Distance Between BST Nodes
- [x] 285.Inorder Successor in BST
- [x] 173.Binary Search Tree Iterator       : essentially, this is about inorder traversal 

下面三道题都是将一个线性的array or list，创建成一个Balanced binary tree。思路都是取中间element创建root节点，然后以recursion的方式创建左右子树。
- [x] 🟩 [1382. Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree)
  - [ ] [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)
  - [ ] [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/)


### Queue & Stack



#### Queue
- [ ] [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)
- [ ] [767. Reorganize String](https://leetcode.com/problems/reorganize-string/)
- [ ] [358. Rearrange String k Distance Apart](https://leetcode.com/problems/rearrange-string-k-distance-apart/)
- [ ] [353. Design Snake Game](https://leetcode.com/problems/design-snake-game/)
- [ ] [346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)  **circular queue or array**
- [ ] [622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)
- [ ] [641. Design Circular Deque](https://leetcode.com/problems/design-circular-deque/)
- [ ] [1670. Design Front Middle Back Queue](https://leetcode.com/problems/design-front-middle-back-queue/)
- [x] [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)
- [x] [582.Kill Process](https://leetcode.com/problems/kill-process/)

(20200901)
- [x] 621.Task Schedule
  - [x] 358.Rearrange String k Distance Apart
  - [x] 767.Reorganize String
- [x] 363.Max Sum of Rectangle No Larger Than K
  [71. Simplify Path](https://leetcode.com/problems/simplify-path/)
  

### Trie
- [ ] 692.Top K Frequent Words
- [ ] 211.Design Add and Search Words Data Structure
- [ ] 212.Word Search II
- [ ] 472.Concatenated Words
- [ ] 336.Palindrome Pairs
- [ ] 642.Design Search Autocomplete System
- [ ] 208.Implement Trie (Prefix Tree)
- [ ] 421.Maximum XOR of Two Numbers in an Array
- [ ] 720.Longest Word in Dictionary
- [x] 🟩🌟 [386. Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers)

- [ ] [677. Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/)
- [ ] 648.Replace Words
- [ ] Add and Search Word -


Maximum XOR of Two Numbers in an Array
Word Search II
Word Square
Palindrome Pairs


### Hash Table

(20200921)
- [ ] [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)




---
## 2. Algorithm

### Depth First Search
DFS（深度优先搜索）通常是用在树或者图结构的问题上，然而有使用也可以用在**网格**结构上。岛屿问题是这类网格DFS问题的典型代表。

🟩🌟 [岛屿类问题的通用解法、DFS 遍历框架](https://leetcode.cn/problems/number-of-islands/solutions/211211/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/)
- [x] [200.Number of Islands](https://leetcode.com/problems/number-of-islands/) **DFS, BFS, Union Find**
- [x] [827. Making A Large Island](https://leetcode.com/problems/making-a-large-island)
- [x] [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/) : Count, DFS
  - [x] [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)    : DFS, BFS
  - [x] 286.Walls and Gates       : BFS
  - [x] 695.Max Area of Island    : DFS
- [x] 🟩🌟 [339. Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum) **(DFS, BFS)**
  - [x] 🟩🌟 [364. Nested List Weight Sum II](https://leetcode.com/problems/nested-list-weight-sum-ii/)
  - [x] [565. Array Nesting](https://leetcode.com/problems/array-nesting/)
  - [x] [690. Employee Importance](https://leetcode.com/problems/employee-importance/)

- [x] [1192.Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)    **DFS, Dijistra, *Add explanation to the post***

  - [x] 1489.Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree

- [x] [199.Binary Tree Right Side View](https://github.com/ylqi007/LeetCode/issues/new)     **BFS + sentinel**

  - [x] 116.Populating Next Right Pointers in Each Node
  - [x] 117.Populating Next Right Pointers in Each Node II
  - [ ] 545.Boundary of Binary Tree

- [x] [394.Decode String](https://leetcode.com/problems/decode-string/)             **stack**

  - [ ] 726.Number of Atoms       : stack
  - [ ] 736.Parse Lisp Expression : stack

- [x] [124.Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)    **Recursion/DFS**

  * 计算路径上值的和

  - [x] 112.Path Sum      : from root-to-leaf, is there any sum equals target or not
  - [x] 113.Path Sum II   : from root-to-leaf, all paths that have sum equals target
  - [x] 437.Path Sum III  : (prefix sum) the number of paths that sum to a given value, the path does not need to start or end at the root or leaf, but must go downwards
  - [x] 666.Path Sum IV   : return the sum of all paths from the root towards the leaves
  - [x] 129.Sum Root to Leaf Numbers: DFS

  * 计算 Tree 的路径长度

  - [x] 687.Longest Univalue Path
  - [x] 543.Diameter of Binary Tree
  - [x] 1522.Diameter of N-Ary Tree

  * Univalue tree

  - [x] 250.Count Univalue Subtrees
  - [x] 572.Subtree of Another Tree
  - [x] 687.Longest Univalue Path

- [x] [547. Friend Circles](https://leetcode.com/problems/friend-circles/)    **DFS, BFS, UF**

- [x] 301.Remove Invalid Parentheses

  - [x] 20.Valid Parentheses
  - [x] 22.Generate Parentheses
    - [x] 17.Letter Combination of a Phone Number   : Backtracking
  - [x] 32.Longest Valid Parentheses
  - [x] 1003.Check If Word Is Valid After Substitutions
  - [x] 39.Combination Sum    : DP or Backtracking
    - [x] 40.Combination Sum II : 与 39 题相比, each candidate number can only be used for one time, and need to avoid duplicate candidate numbers.
    - [x] 216.Combination Sum III
    - [x] 377.Combination Sum IV
  - [x] 77.Combinations
    - [x] 46.Permutations       : backtrack
    - [x] 47.Permutations II    : `nums` array may contains duplicate numbers
    - [x] 31.Next Permutations  
    - [x] 17.Letter Combinations of a Phone Number  : Backtracking
    - [x] 254.Factor Combinations   : Recursive
  - [x] 46.Permutations       : backtrack
    - [x] 47.Permutations II    : `nums` array may contains duplicate numbers
    - [x] 60.Permutation Sequence   !!!

- [x] 472.Concatnated Words

  - [x] 139.Word Break
  - [x] 140.Word Break II

- [x] 332.Reconstruct Itinerary     : DFS

  - [x] 207.Course Schedule       : DFS, BFS, inDegree, detect cycle
  - [x] 210.Course Schedule II    : 
  - [x] 630.Course Schedule III   : Greedy
  - [x] 261.Graph Valid Tree      : Detect if a cycle exists or not
  - [x] 547.Friend Circles        : Union Find, DFS
  - [x] 310.Minimum Height Trees  : 

- [x] [105.Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)    **DFS/Recursion**

  - [x] 106.Construct Binary Tree from Inorder and Postorder Traversal
  - [x] 889.Construct Binary Tree from Preorder and Postorder Traversal
  - [x] 1008.Construct Binary Search Tree from Preorder Traversal

- [x] 108.Convert Sorted Array to Binary Search Tree

  - [x] 109.Convert Sorted List to Binary Search Tree

- [x] 114.Flatten Binary Tree to Linked List

  - [x] 430.Flatten a Multilevel Doubly Linked List

- [x] 863.All Nodes Distance K in Binary Tree

- [x] 98.Valid Binary Search Tree

- [x] 529.Minesweeper

- [x] 314.Binary Tree Vertical Order Traversal

- [x] 695.Max Area of Island

  - [x] 200.Number of Islands
  - [x] 463.Island Perimeter
  - [x] 1034.Coloring A Border
  - [x] 733.Flood Fill

- [x] 329.Longest Increasing Path in a Matrix

- [x] 721.Accounts Merge

  - [x] 684.Redundant Connection      : undirected graph, Union Find
  - [x] 685.Redundant Connection II   : directed graph, Union Find
  - [x] 734.Sentence Similarity
  - [x] 737.Sentence Similarity II

- [x] 133.Clone Graph

  - [x] 138.Copy List with Random Pointer
  - [x] 1485.Clone Binary Tree with Random Pointer
  - [x] 1490.Clone N-ary Tree

* Iterator
  - [ ] Flatten 2D Vector
  - [ ] Zigzag Iterator
  - [ ] Peeking Iterator



### Breadth First Search
- [x] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
  - [x] [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
- [ ] space
- [x] [127. Word Ladder](https://leetcode.com/problems/word-ladder/)    **BFS, Two Direction BFS**
- [x] [199.Binary Tree Right Side View](https://github.com/ylqi007/LeetCode/issues/new)     **BFS + sentinel**
- [x] 🟩🌟 [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)    **BFS, BFS 1ms 值得再看**
  - [x] 🟩🌟[286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/) **BFS**
- [x] [1197. Minimum Knight Moves](https://leetcode.com/problems/minimum-knight-moves/)    **BFS + Formular**
- [x] [301. Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)    **DFS, BFS**
- [x] [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)    **DFS, BFS**
- [ ] []()
- [ ] []()
- [ ] []()


### Dynamic Programming
- [x] 🟩🌟[42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) **DP; Two Pointers**
  - [x] 🟩🌟[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
  - [x] 🟩 [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
  - [ ] [407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) [Hard]
  - [ ] [755. Pour Water](https://leetcode.com/problems/pour-water/)
- [x] 🟩🌟[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
  - [x] [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
  - [x] [123.Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
  - [x] [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
  - [x] [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
- [x] 🟩🌟 [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring) [Not an obvious DP, extend from center]
  - [x] 🟥 🌟 [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)
  - [x] [266. Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/)
  - [ ] [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) [Not DP]
  - [x] 🟩🌟 [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) [**DP, 两种写法**]
  - [x] [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
  - [ ] [2472. Maximum Number of Non-overlapping Palindrome Substrings](https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/)
- [x] [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [x] [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) **DP**
- [x] [1335. Minimum Difficulty of a Job Schedule](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/)
- [x] [221. Maximal Square](https://leetcode.com/problems/maximal-square/)  **DP; 还有一个1ms的方法**
- [x] [139. Word Break](https://leetcode.com/problems/word-break/)  **DP with memoization**
- [ ] [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)  **DP, top-down, bottom-up**
- [x] [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) **DP, top-down, bottom-up**
- [ ] [1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/) **DP, TreeMap**
- [ ] [140. Word Break II](https://leetcode.com/problems/word-break-ii/)
- [ ] [322. Coin Change](https://leetcode.com/problems/coin-change/)
- [ ] [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
- [ ] [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/)
- [ ] 871
- [ ] [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- [ ] 1531
- [ ] [403. Frog Jump](https://leetcode.com/problems/frog-jump/)
- [ ] [72. Edit Distance](https://leetcode.com/problems/edit-distance/)
- [x] [91. Decode Ways](https://leetcode.com/problems/decode-ways/) **DP**


  

### Backtracking

[//]: # "TODO: 20201007, 10.Regular Expression Matching"
[//]: # "TODO: 20201007, 17.Letter Combinations of a Phone Number"
[//]: # "TODO: 20201007, 140.Word Break II"
[//]: # "TODO: 20201007, 211.Design Add and Search Words Data Structure"
[//]: # "TODO: 20201007, 131.Palindrome Partitioning"
[//]: # "TODO: 20201007, 78.Subsets"
[//]: # "TODO: 20201007, 37.Sodoku Solver"
[//]: # "FIXME: test1, test2"

- [ ] Typical Problems
  * Subsets
  * Combinations
  * Combination Sum
  * Permutation
  * Parentheses
- [x] 🟩🌟 Parentheses
  - [x] [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
  - [x] [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
  - [x] [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [x] Permutations
  - [x] [46. Permutations](https://leetcode.com/problems/permutations/)           **: Swap untill all**
  - [x] [47. Permutations II](https://leetcode.com/problems/permutations-ii/)     **: Swap untill all, Pick and add one by one**
  - [x] [77. Combinations](https://leetcode.com/problems/combinations/)
  - [x] [31. Next Permutation](https://leetcode.com/problems/next-permutation/)
  - [x] [60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)
- [x] Word Search
  - [x] [79. Word Search](https://leetcode.com/problems/word-search/)
  - [x] [212. Word Search II](https://leetcode.com/problems/word-search-ii/)
- [ ] [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)      
- [x] [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) 
  - [x] [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
  - [x] [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
  - [x] [401. Binary Watch](https://leetcode.com/problems/binary-watch/)
- [x] Subsets
  - [x] [78. Subsets](https://leetcode.com/problems/subsets/)
  - [x] [90. Subsets II](https://leetcode.com/problems/subsets-ii/)
  - [x] [320. Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/)
  - [x] [784. Letter Case Permutation](https://leetcode.com/problems/letter-case-permutation/)

- [x] Unique Paths
  - [x] [980. Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)
  - [x] [212. Word Search II](https://leetcode.com/problems/word-search-ii/)
  - [x] [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)     : DP

- [x] 八皇后 N-Queens
  - [x] [51. N-Queens](https://leetcode.com/problems/n-queens/)
  - [x] [52. N-Queens II](https://leetcode.com/problems/n-queens-ii/)
  - [x] [1001. Grid Illumination](https://leetcode.com/problems/grid-illumination/)
- [ ] Sodoku 
  - [x] [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)
  - [x] [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)
- [x] Combination Sum
  - [x] [39. Combination Sum](https://leetcode.com/problems/combination-sum/)
  - [x] [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
  - [x] [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)
  - [x] [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

- [ ] Word Ladder
- [ ] Palindrome Partitioning
  - [ ] [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)
  - [ ] [132. Palindrome Partitioning II](https://leetcode.com/problems/palindrome-partitioning-ii/)



- [x] 78.Subsets
- [x] 90.Subsets II
- [x] 784.Letter Case Permutation


### Union Find
- [x] 🟩🌟 [959. Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/)

[//]: # "TODO: 20201110, common factor"

- [x] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)    **DFS, BFS, UF**

  - [ ] [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
  - [ ] [305. Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/)

- [x] [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)    **Sort, Set, Map**

  * 记住 `currentLen` 的写法，出现连续相同数字的情况是，`currentLen` 没有改变

- [x] [547. Friend Circles](https://leetcode.com/problems/friend-circles/)     **Graph + DFS, UF**，此处的 graph 是用 adjacent matrix 表示的。

- [x] [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/)   **Graph + DFS, UF**, `a/b = (a/c) / (b/c) = a/b`

- [x] [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)     **Graph+DFS, UF**， Graph represented by adjacent list.

- [x] [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)    **DFS, UF**

  - [ ] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
  - [ ] [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/), **not related to UF**

- [x] [959. Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/)    **UF**

- [x] [765. Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/)    **Cyclic Swapping (LC 41, 268)**

  - [ ] [268. Missing Number](https://leetcode.com/problems/missing-number/description/)
  - [ ] [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/)

- [x] [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)    **UF, DFS**

  - [ ] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
  - [ ] [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)   **UF, DFS**
  - [ ] [547. Friend Circles](https://leetcode.com/problems/friend-circles/)

- [x] [1202. Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/)    **UF + PriorityQueue**

- [ ] [305. Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/)

- [ ] [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)

- [ ] [839. Similar String Groups](https://leetcode.com/problems/similar-string-groups/)

- [ ] **hard** : [685. Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/)

- [ ] [1135. Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)

- [ ] [947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)

- [ ] [1102. Path With Maximum Minimum Value](https://leetcode.com/problems/path-with-maximum-minimum-value/)

- [ ] [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)

- [ ] [924. Minimize Malware Spread](https://leetcode.com/problems/minimize-malware-spread/)

- [ ] [737. Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/)


### Sliding Window + Two Pointers
(20200904)
* Sliding Window Problems
  * At Most K Distinct Elements
    * 对于 3, 159, 340, and 904, 都是求最长的 substring or subarray 的长度
    - [x] 3.Longest Substring Without Repeating Characters
    - [x] 159.Longest Substring with At Most Two Distinct Characters
    - [x] 340.Longest Substring with At Most K Distinct Characters
    - [x] 904.Fruit Into Baskets **(The same with 159)**
    * 对于 992, 1248, 1358, 是求满足所有要求的 substrings or subarrays 的数量, 区别是 992, 1248 是一个范围内的都可以，1358 是要求准确的 K 个
    - [x] 992.Subarrays with K Different Integers                       --> **hard**, **atMost()**, or **prefix**
    - [x] 1248.Count Number of Nice Subarrays                           --> **hard**, **atMost()**, or **prefix**
    - [x] 1358.Number of Substrings Containing All Three Characters     --> **hard**, **atMost()**, or **prefix**
  * Consecutive Ones
    * 485 & 1446 都是在**不连续**发生的时候，改变 counter 的状态，然后进行更新。
    - [x] 485.Max Consecutive Ones
    - [x] 1446.Consecutive Characters
    * For 487, 1004: (a) Use a counter; (b) Use a `Queue` to store the indexes of 0s.
    - [x] 487.Max Consecutive Ones II
    - [x] 1004.Max Consecutive Ones III
    - [x] 424.Longest Repeating Character Replacement
  * Min or Max length -- Two Pointers + Prefix Sum/counter
    - [x] 209.Minimum Size Subarray Sum                 --> Two Pointers + Prefix Sum: When prefix larger than S, try to update the res
    - [x] 76.Minimum Window Substring                   --> Two Pointers + Counter
      - [x] 727.Minimum Window Subsequence            --> **hard**, Two Pointers --> From left to right, then right to left
    - [x] 325.Maximum Size Subarray Sum Equals k        --> Prefix Sum + HashMap to store the index of prefix sum
    - [x] 718.Maximum Length of Repeated Subarray       --> **DP**, **Don't understand method 2**
    - [x] 862.Shortest Subarray with Sum at Least K         : Queue
    - [x] 1234.Replace the Substring for Balanced String    : Two Pointers, Outside the window
    - [x] 930.Binary Subarrays With Sum                     : Two Window + Presum
  * Sum / Product
    - [x] [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)    : **判断是否存在**
    - [x] [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)        : **HashMap or Prefix Sum**
    - [x] [1. Two Sum](https://leetcode.com/problems/two-sum/)
    - [x] [713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)  : **Sliding Window**
    - [x] [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)
    - [x] [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)
    - [x] [1590. Make Sum Divisible by P](https://leetcode.com/problems/make-sum-divisible-by-p/)
    - [x] [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
    - [x] [325. Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
    - [x] [1099. Two Sum Less Than K](https://leetcode.com/problems/two-sum-less-than-k/)



### Dynamic Programming -- (20200907)
- [x] [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
  - [x] [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
  - [x] [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
  - [x] [697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array/)
  - [x] [978. Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/)

- [x] [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)  : **Extend from center**
  - [x] [266. Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/)
  - [x] [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)          : **Extend from center or Dynamic Programming**
  - [x] [336. Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)
  - [x] [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)    : **DP**
  - [x] [214. Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/)

- [x] [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
  - [x] [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
  - [x] [123.Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
  - [x] [188. Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
  - [x] [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)

- [x] [91.Decode Ways](https://leetcode.com/problems/decode-ways/)
  - [x] [639. Decode Ways II](https://leetcode.com/problems/decode-ways-ii/)

- [x] [139. Word Break](https://leetcode.com/problems/word-break/)
  - [x] [140. Word Break II](https://leetcode.com/problems/word-break-ii/)
  - [x] [472. Concatenated Words](https://leetcode.com/problems/concatenated-words/)
  - [x] [Java Common template - Word Break I, Word Break II, Concatenated Words](https://leetcode.com/problems/concatenated-words/discuss/348972/Java-Common-template-Word-Break-I-Word-Break-II-Concatenated-Words)

- [x] [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
  - [x] [221. Maximal Square](https://leetcode.com/problems/maximal-square/)
  - [x] [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
  - [x] [764. Largest Plus Sign](https://leetcode.com/problems/largest-plus-sign/)

- [x] [322. Coin Change](https://leetcode.com/problems/coin-change/)
  - [x] [983. Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/)

- [x] [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
  - [x] [44. Wildcard Matching](https://leetcode.com/problems/wildcard-matching/)

- [x] [312. Burst Balloons](https://leetcode.com/problems/burst-balloons/)
  - [x] [1000. Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/)
  - [x] [1167. Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/)

- [x] [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)   : DP
- [x] [62. Unique Paths](https://leetcode.com/problems/unique-paths/)           : DP
  - [x] [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)     : DP
  - [x] [980. Unique Paths III](https://leetcode.com/problems/unique-paths-iii/)  : Backtracking, Depth-First Search
- [x] [174. Dungeon Game](https://leetcode.com/problems/dungeon-game/)
  - [x] [741. Cherry Pickup](https://leetcode.com/problems/cherry-pickup/)

- [x] [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
  - [x] [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/)
  - [x] [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)
  - [x] [646. Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/)
    - [x] [491. Increasing Subsequences](https://leetcode.com/problems/increasing-subsequences/)
  - [x] [673. Number of Longest Increasing Subsequence](https://leetcode.com/problems/number-of-longest-increasing-subsequence/)
  - [x] [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)
    - [x] [72. Edit Distance](https://leetcode.com/problems/edit-distance/)
    - [x] [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
    - [x] [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)

- [x] [674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)
- [x] [549. Binary Tree Longest Consecutive Sequence II](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/)

- [x] [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)
  - [x] [72. Edit Distance](https://leetcode.com/problems/edit-distance/)
  - [x] [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)
  - [x] [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)

- [x] [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)
  - [x] [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

- [x] [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
  - [x] [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
  - [x] [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)
  - [x] [1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)

- [x] [472. Concatenated Words](https://leetcode.com/problems/concatenated-words/)
  - [x] [140. Word Break II](https://leetcode.com/problems/word-break-ii/)

- [x] [72. Edit Distance](https://leetcode.com/problems/edit-distance/)
  - [x] [161. One Edit Distance](https://leetcode.com/problems/one-edit-distance/)

- [ ] [97. Interleaving String](https://leetcode.com/problems/interleaving-string/)
- [ ] [403. Frog Jump](https://leetcode.com/problems/frog-jump/)
- [ ] [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)
- [x] [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)
  - [x] [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

* Consecutive Sequence in Binary Tree
- [x] [298. Binary Tree Longest Consecutive Sequence](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/)

- [x] [549. Binary Tree Longest Consecutive Sequence II](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/)



- [x] [698. Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)
- [x] [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)
- [x] [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

- [ ] - [ ] 


### Divide and Conquer
- [x] [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)
  - [x] [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
  - [x] [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
  - [x] [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)
- [x] [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
  Wiggle Sort II
  - [x] [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
    Third Maximum Number
    Kth Largest Element in a Stream
  - [x] [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)



---
### Greedy
- [x] [763. Partition Labels](https://leetcode.com/problems/partition-labels/)
  - [x] [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [x] Meeting Rooms
  - [x] [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
  - [x] [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [ ] Jump Game
  - [x] [55. Jump Game](https://leetcode.com/problems/jump-game/)
  - [ ] [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)
  - [ ] [1306. Jump Game III](https://leetcode.com/problems/jump-game-iii/)
- [ ] []()
- [ ] []()
- [ ] []()


### --- Split ---



### 20200701: Review of Basic Calculators

Review of the following questoins:
1. 224.Basic Calculator
2. 227.Basic Calculator II
3. 772.Basic Calculator III

### 20200702: Clone-related problems
1. 133.Clone Graph
2. 138.Copy List with Random Pointer
3. 1485.Clone Binary Tree with Random Pointer
4. 1490.Clone N-ary Tree

* 用 HashMap 标记已经访问过的 or 复制过的 node，从而避免陷入死循环。
* 在 `1485. Clone Binary Tree with Random Pointer` 中，需要有 `HashMap` 来标记已经访问过的 Nodes。
* 然而在 `1490. Clone N-ary Tree` 中，并不需要 `HashMap`，只要简单的 DFS 就可以。这是因为 `1490` 是普通的 Tree，没有 `random`，因此不会有循环的产生。

### 20200705: Brace Expansion
- [x] 1087.Brace Expansion
- [x] 1096.Brace Expansion II

- [x] 

### 20200708. Abbreviaton
- [x] 187.Repeated DNA Sequences    : **对 iterate range 的分析**
- [x] 408.Valid Word Abbreviation   : Two Pointers
- [x] 288.Unique Word Abbreviation  : HashSet + hashCode
- [x] 320.Generalized Abbreviation  : Backtracking
- [x] 527.Word Abbreviation         : !!!
- [ ] 411.Minimum Unique Word Abbreviation  : Still not figure out.

- [ ] 1044.Longest Duplicate Substring
- [ ] 626.Exchange Seats            : SQL


### 20200825. Dynamic Programming, Greedy, Two Pointers
- [x] 392.Is Subsequence                        : Two Pointers
    - [x] 792.Number of Matching Subsequences   : Tow Pointers, Next Letter Pointer
    - [x] 1055.Shortest Way to Form String      : Two Pointers


* Range Sum Query
    - [x] 303.Range Sum Query - Immutable  : prefix sum
    - [x] 304.Range Sum Query 2D - Immutable
    - [?] 307.Range Sum Query - Mutable     : Segment Tree
    - [?] 308.Range Sum Query 2D - Mutable      

  

- [ ] 353.Design Snake Game          
- [ ] 622.Design Circular Queue          
- [ ] 346.Moving Average from Data Stream                 

- [ ] 1489.Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
- [ ] 1268.Search Suggestions System

- [ ] 1049.Last Stone Weight II

### 20200906
- [x] [1007.Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)
- [x] [1165. Single-Row Keyboard](https://leetcode.com/problems/single-row-keyboard/)
- [x] [1161. Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)

* Room meeting and Merge intervals
    - [x] [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
    - [x] [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
    - [x] [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
        - [x] [57. Insert Interval](https://leetcode.com/problems/insert-interval/)
        - [x] [495. Teemo Attacking](https://leetcode.com/problems/teemo-attacking/)
        - [x] [616. Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/)
              [758. Bold Words in String](https://leetcode.com/problems/bold-words-in-string/)
    - [x] [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)
    - [x] [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
    - [x] [1094. Car Pooling](https://leetcode.com/problems/car-pooling/)   



---
- [ ] 


---
- [ ] 


---
## 3. Contest
1. [20200919 - Weekly Contest 206](contests/0_Log.md/#20200912.Weekly-Contest-206)
2. [20200919 - Weekly Contest 207](contests/0_Log.md/#20200919.Weekly-Contest-207)
3. [20200919 - Weekly Contest 208](contests/0_Log.md/#20200926.Weekly-Contest-208)
4. [20200919 - Weekly Contest 209](contests/0_Log.md/#20201003.Weekly-Contest-209)
5. [20200919 - Weekly Contest 210](contests/0_Log.md/#20201003.Weekly-Contest-210)


--
## 4. Company
### Google
- [x] [843. Guess the Word](https://leetcode.com/problems/guess-the-word/)  **keep narrowing range; minimax**
- [x] [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) **Sliding Window**
- [x] [359. Logger Rate Limiter](https://leetcode.com/problems/logger-rate-limiter/)	**Hash Table**
- [x] [946. Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/) **Stack operation**
- [x] [727. Minimum Window Subsequence](https://leetcode.com/problems/minimum-window-subsequence/)  **Find and then optimize**

- [ ] [1548. The Most Similar Path in a Graph](https://leetcode.com/problems/the-most-similar-path-in-a-graph/) **DFS, Dijkstra**
- [ ] [1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)     **Sliding Window**
- [ ] [1153. String Transforms Into Another String](https://leetcode.com/problems/string-transforms-into-another-string/)   **linkedlist or cycle**
- [ ] [715. Range Module](https://leetcode.com/problems/range-module/)  **Not finish yet**
- [ ] 

### Amazon
[Amazon Online Assessment Questions](https://algo.monster/problems/amazon_online_assessement_questions)

New Grad
- [x] 1. Cut off Rank: **Bucket Sort; PriorityQueue**
    - [x] [Cutoff Ranks](https://aonecode.com/amazon-online-assessment-cutoff-ranks)
    - [ ] [[NA] Amazon SDE Intern OA 2](https://leetcode.com/discuss/interview-question/824381/na-amazon-sde-intern-oa-2)
    - [x] [playground](https://leetcode.com/playground/7XyKjun3)
    - [x] [Amazon-CutOff_Rank](./companies/Amazon/2021_CutOffRank.md)
- [x] 2. Fill the truck: **Bucket Sort; PriorityQueue**
    - [x] [Load The Cargo](https://aonecode.com/interview-question/load_cargo)
    - [x] [playground](https://leetcode.com/playground/bhLiku4X)
    - [x] [1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/) **buckets; Sort array; Priority Queue**
    - [x] [1710. Maximum Units on a Truck.md](./problems/1710)
- [x] 3. Disk Space Analysis: **Dynamic Programming; Deque**
    - [x] [The Max Of Minima](https://aonecode.com/interview-question/MaxOfMinima)  **Deque; DP**
    - [x] [Amazon Online Assessment (OA) - Find The Maximum Available Disk Space](https://algo.monster/problems/find_the_maximum_available_disk_space)
    - [x] [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) **Dynamic Programming; Deque**
    - [ ] [Maximum of Minimum Values II](https://leetcode.com/discuss/interview-question/442377/Maximum-of-Minimum-Values-II/397715)
    - [ ] [1102. Path With Maximum Minimum Value](https://leetcode.com/problems/path-with-maximum-minimum-value/)
    - [ ] [Amazon-Disk_Space_Analysis](./companies/Amazon/Amazon-Disk_Space_Analysis.md)
- [x] 4. Nearest City:  **HashMap + TreeSet**
    - [x] [Amazon | OA 2020 | Nearest City](https://leetcode.com/discuss/interview-question/872961/Amazon-or-OA-2020-or-Nearest-City)
    - [x] [Amazon-Nearest_City](./companies/Amazon/2021_Nearest_City.md)
    - [x] [Playground](https://leetcode.com/playground/h6T9VMRi)
- [x] 5. Subtree with Maximum Average: 
    - [x] [Amazon | OA 2019 | Subtree with Maximum Average](https://leetcode.com/discuss/interview-question/349617)
    - [x] [1120. Maximum Average Subtree](https://leetcode.com/problems/maximum-average-subtree/)
    - [x] [Amazon-Subtree_with_Maximum_Average.md](./companies/Amazon/Amazon-Subtree_with_Maximum_Average.md)
    - [ ] [Amazon-Subtree_with_the_Maximum_Average](./companies/Amazon/2021_Subtree_with_the_Maximum_Average.md)
- [x] 6. 解除回文: 
    - [x] [1328. Break a Palindrome](https://leetcode.com/problems/break-a-palindrome/)
    - [x] [1328. Break a Palindrome](./problems/1328.Break_a_Palindrome.md)
- [x] 7. Smallest Negative Balance: **HashMap**
    - [ ] [Find Countries with the Largest Deficit](https://aonecode.com/interview-question/FindCountriesWithTheLargestDeficit)
    - [x] [2021_Smallest_Negative_Balance](./companies/Amazon/2021_Smallest_Negative_Balance_or_Amazon_Debt_Records.md)
    - [x] [Playground](https://leetcode.com/playground/kEa2XYnW)
- [x] 8. Find the highest Profit; Maximize Profit: **PrirityQueue**
    - [ ] [Maximize Profit](https://aonecode.com/maximize-profit) **Priority Queue**
    - [x] [Amazon-Higest_Profit](./companies/Amazon/Amazon-Highest_Profit.md)   **HashMap**
    - [ ] [2021_Find_the_Highest_Profit.md](./companies/Amazon/2021_Find_the_Highest_Profit.md)
- [x] 9. Ways to Split String into Prime Numbers:
    - [ ] [ [面试经验] 亚麻oa2 ng ](https://www.1point3acres.com/bbs/thread-661768-1-1.html)
    - [x] [count the number of ways the string can split to get pime number](https://leetcode.com/discuss/interview-question/593211/count-the-number-of-ways-the-string-can-split-to-get-pime-number)
    - [x] [Amazon-Split_String_into_Primes](./companies/Amazon/Amazon-Split_String_Into_Primes.md)
    - [x] [Find all possible ways to Split the given string into Primes](https://www.geeksforgeeks.org/find-all-possible-ways-to-split-the-given-string-into-primes/)
    - [x] [Playground](https://leetcode.com/playground/2WpmBFRX)
- [x] 10. Fetch items to display:   **Sort**
    - [ ] [Ranking Products](https://aonecode.com/interview-question/ranking-products)
    - [ ] [[面试经验] 亞麻OA2](https://www.1point3acres.com/bbs/interview/amazon-software-engineer-678189.html)
    - [ ] [Amazon Online Assessment (OA) - Fetch Items To Display](https://algo.monster/problems/fetch_items_to_display)
    - [x] [Amazon-Pagination](./companies/Amazon/Amazon-Pagination.md)
    - [x] [Playground](https://leetcode.com/playground/EyTrfrQD)
    - [x] ~/Dropbox/Jobs/Amazon/OA_part1.pdf
- [x] 11. Packaging Automation: **HashMap**
    - [ ] [[面试经验] 求OA2 packaging automation](https://www.1point3acres.com/bbs/interview/amazon-software-engineer-701392.html)
    - [ ] [AMAZON OA | SDE | 2021 | hackerrank | packaging automation](https://leetcode.com/discuss/interview-question/1018060/AMAZON-OA-or-SDE-or-2021-or-hackerrank-or-packaging-automation)
    - [x] $$$ [Playground](https://leetcode.com/playground/TzdtAVaj)
    - [x] $$$ [Markdown](./companies/Amazon/2021_Packaging_Automation.md)
- [x] 12. Min Distance Between Robots: **Union Find**
    - [ ] [Squared Shortest Distance](https://aonecode.com/interview-question/squared-shortest-distance)
    - [ ] [Amazon Online Assessment (OA) - Squared Shortest Distance](https://algo.monster/problems/squared_shortest_distance)
    - [ ] [Shortest Distance Between Robots](https://leetcode.com/discuss/interview-question/799431/)
    - [x] [Shortest Distance Between Robots](./companies/Amazon/Amazon-Shortest_Distance_Between_Robots.md)
    - [x] [Shortest Distance](./companies/Amazon/Amazon-Shortest_Distance.md)
- [x] 13. Power Grid    **Union Find**
    - [x] [Amazon OA2 - SDE1(New Grad) 2021 - Power Grid - With Solutions](https://leetcode.com/discuss/interview-question/797541/Amazon-Online-Assessment-2-SDE-1)
    - [ ] [1135. Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)
    - [x] [1135. Connecting Cities With Minimum Cost.md](./companies/Amazon/Amazon-Min_Cost_to_Connect_All_Nodes.md)
- [x] 14. Count Teams   **排列组合**
    - [ ] [Count Review Combinations](https://aonecode.com/interview-question/Count-Review-Combinations)
    - [ ] [Amazon Online Assessment (OA) - Count Teams](https://algo.monster/problems/count_teams)
    - [x] [3.Associates Roster](https://www.1point3acres.com/bbs/thread-661422-1-1.html)
    - [x] [⭐ [面试经验] 亚麻 新鲜OA2 NG全职 08/21/2020](https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=662496&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D5%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline)
    - [x] [Playground](https://leetcode.com/playground/X7YCu9Dy)
    - [x] [Markdown](./companies/Amazon/Amazon-Associates_Roster.md)
- [x] 15. Copy List with Random Pointer: **Method 4**
    - [x] [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)
    - [x] [138. Copy List with Random Pointer](./problems/138.Copy_List_with_Random_Pointer.md)


## 5. The First 400
- [x] [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [x] [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- [x] [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [x] [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- [x] [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [x] [6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)
- [x] [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/)
- [x] [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)
- [x] [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
- [ ] [10. Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)
- [x] [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- [ ] [12. Integer to Roman](https://leetcode.com/problems/integer-to-roman/)
- [ ] [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
- [x] [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- [x] [15. 3Sum](https://leetcode.com/problems/3sum/)
- [x] [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)
- [x] [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [ ] [18. 4Sum](https://leetcode.com/problems/4sum/)
- [x] [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [x] [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [x] [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [x] [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)   **Backtracking**
- [x] [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)   **Quick Merge**
- [x] [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)     **Recursion, Iterative**
- [x] [⭐ 25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)     **Recursion, Iterative**
- [x] [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) **Two Pointers**
- [x] [27. Remove Element](https://leetcode.com/problems/remove-element/)     **Two Pointers**
- [x] [28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)   **Two Pointers**
- [ ] [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)
- [ ] [⭐ 30. Substring with Concatenation of All Words](https://leetcode.com/problems/substring-with-concatenation-of-all-words/)   **Hash Table; Two Pointers?**
- [ ] [⭐ 31. Next Permutation](https://leetcode.com/problems/next-permutation/)
- [ ] [⭐ 32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)   **Dynamic Programming**
- [x] [⭐ 33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) **Binary Search**
