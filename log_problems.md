[TOC]

---
## 1. Data Structure
### DFS
(20200711)
- [x] 200.Number of Islands         : DFS, BFS, Union Find
    - [x] 130.Surrounded Regions    : DFS, BFS
    - [x] 286.Walls and Gates       : BFS
    - [x] 695.Max Area of Island    : DFS
    - [x] 463.Island Perimeter      : Count
- [x] 1192.Critical Connections in a Network    : DFS, Dijistra, *Add explanation to the post*
  
    - [x] 1489.Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
- [x] 199.Binary Tree Right Side View   ： BFS
    - [x] 116.Populating Next Right Pointers in Each Node
    - [x] 117.Populating Next Right Pointers in Each Node II
    - [ ] 545.Boundary of Binary Tree
- [x] 394.Decode String             : stack
    - [ ] 726.Number of Atoms       : stack
    - [ ] 736.Parse Lisp Expression : stack
- [x] 124.Binary Tree Maximum Path Sum
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
- [x] 105.Construct Binary Tree from Preorder and Inorder Traversal
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
    
    
### Tree
(20200815)
* Traversal
- [x] 94.Binary Tree Inorder Traversal
- [x] 144.Binary Tree Preorder Traversal        : recursion + iteration, without morris
- [x] 145.Binary Tree Postorder Traversal       : recursion + iteration, without morris
- [x] 589.N-ary Tree Preorder Traversal         : 1.注意 iterative 的写法，基于 Stack 实现；   2.recursion
- [x] 590.N-ary Tree Postorder Traversal        : 1.注意 iterative 的写法，基于 Stack 实现；   2.recursion
- [x] 314.Binary Tree Vertical Order Traversal
- [x] 102.Binary Tree Level Order Traversal     : BFS
- [x] 107.Binary Tree Level Order Traversal II
- [x] 103.Binary Tree Zigzag Level Order
- [x] 429.N-ary Tree Level Order Traversal
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


### Graph  
(20200817)  
- [x] 269.Alien Dictionary                  : DFS, Topological Sort
    - [x] 210.Course Schedule II
- [x] 207.Course Schedule                   : DFS, 
    - [x] 210.Course Schedule II
    - [x] 630.Course Schedule III
    - [x] 261.Graph Valid Tree
    - [x] 310.Minimum Height Trees
- [x] 332.Reconstruct Itinerary             : DFS, 
- [x] 133.Clone Graph
    - [x] 138.Copy List with Random Pointer
    - [x] 1485.Clone Binary Tree with Random Pointer
    - [x] 1490.Clone N-ary Tree
- [x] 399.Evaluate Division                 : DFS, Union Find
- [x] 785.Is Graph Bipartie?                : DFS, BFS
    - [x] 886.Possible Bipartition
- [x] 210.Course Schedule II
- [x] 1153.String Transforms Into Another String
- [x] 323.Number of Connected Components in an Undirected Graph
    - [x] 200.Number of Islands             : DFS, Union Find
    - [x] 261.Graph Valid Tree              : Union Find, DFS
    - [x] 547.Friend Circles
- [x] 444.Sequence Reconstruction           : BFS, Topological sort
- [x] 743.Network Delay Time                : DFS, Dijkstra's Algorithm
### Queue & Stack
(20200901)
- [x] 621.Task Schedule     
    - [x] 358.Rearrange String k Distance Apart
    - [x] 767.Reorganize String
- [x] 363.Max Sum of Rectangle No Larger Than K
[71. Simplify Path](https://leetcode.com/problems/simplify-path/)
### Hash Table
(20200921)
- [ ] [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
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

- [ ] [677. Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/)
- [ ] 648.Replace Words
- [ ] Add and Search Word -
  

Maximum XOR of Two Numbers in an Array
Word Search II
Word Square
Palindrome Pairs



---
## 2. Algorithm
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

### 20200706. Backtracking
- [x] 78.Subsets
- [x] 90.Subsets II
- [x] 784.Letter Case Permutation

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
- [x] Generate Parentheses
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


---
### Union Find
- [x] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
    - [x] [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)
    - [ ] [305. Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/)
- [x] [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) 
    * 记住 `currentLen` 的写法，出现连续相同数字的情况是，`currentLen` 没有改变
- [x] [547. Friend Circles](https://leetcode.com/problems/friend-circles/)
- [x] [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/)
- [x] [721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)  : DSU, Union-Find
- [x] [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)  
    - [x] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
    - [x] [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/), **not related to UF**
- [x] [959. Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/)
- [x] [765. Couples Holding Hands](https://leetcode.com/problems/couples-holding-hands/)    : Cyclic Swapping (LC 41, 268)
    - [x] [268. Missing Number](https://leetcode.com/problems/missing-number/description/)
    - [x] [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/)
- [x] [323. Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
    - [x] [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)
    - [x] [261. Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/)   **UF, DFS**
    - [x] [547. Friend Circles](https://leetcode.com/problems/friend-circles/)
- [ ] [1202. Smallest String With Swaps](https://leetcode.com/problems/smallest-string-with-swaps/)
- [x] [305. Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/)
- [ ] [1319. Number of Operations to Make Network Connected](https://leetcode.com/problems/number-of-operations-to-make-network-connected/)
- [ ] [839. Similar String Groups](https://leetcode.com/problems/similar-string-groups/)
- [ ] **hard** : [685. Redundant Connection II](https://leetcode.com/problems/redundant-connection-ii/)
- [x] [1135. Connecting Cities With Minimum Cost](https://leetcode.com/problems/connecting-cities-with-minimum-cost/)
- [ ] [947. Most Stones Removed with Same Row or Column](https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/)
- [ ] [1102. Path With Maximum Minimum Value](https://leetcode.com/problems/path-with-maximum-minimum-value/)
- [ ] [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)
- [ ] [924. Minimize Malware Spread](https://leetcode.com/problems/minimize-malware-spread/)
- [ ] [737. Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/)


---
## 3. Contest
1. [20200919 - Weekly Contest 206](contests/0_Log.md/#20200912.Weekly-Contest-206)
2. [20200919 - Weekly Contest 207](contests/0_Log.md/#20200919.Weekly-Contest-207)
3. [20200919 - Weekly Contest 208](contests/0_Log.md/#20200926.Weekly-Contest-208)
4. [20200919 - Weekly Contest 209](contests/0_Log.md/#20201003.Weekly-Contest-209)
5. [20200919 - Weekly Contest 210](contests/0_Log.md/#20201003.Weekly-Contest-210)

