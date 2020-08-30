

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
 
### 20200711. DFS
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
- [ ] 329.Longest Increasing Path in a Matrix
- [ ] 721.Accounts Merge
- [ ] 133.Clone Graph




* Iterator
    - [ ] Flatten 2D Vector
    - [ ] Zigzag Iterator
    - [ ] Peeking Iterator
    
    
### 20200815. Tree
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
 
 
## 20200817. Graph    
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


## 20200825. Dynamic Programming, Greedy, Two Pointers
- [x] 392.Is Subsequence                        : Two Pointers
    - [x] 792.Number of Matching Subsequences   : Tow Pointers, Next Letter Pointer
    - [x] 1055.Shortest Way to Form String      : Two Pointers


- [ ] 1489.Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
- [ ] 1268.Search Suggestions System