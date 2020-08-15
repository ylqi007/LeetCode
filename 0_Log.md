

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
- [ ] 1192.Critical Connections in a Network    : DFS, Dijistra, *Add explanation to the post*
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
- [x] 314.Binary Tree Vertical Order Traversal
    - [x] 102.Binary Tree Level Order Traversal
    - [x] 107.Binary Tree Level Order Traversal II
    - [x] 103.Binary Tree Zigzag Level Order
    - [x] 429.N-ary Tree Level Order Traversal
    - [x] 589.N-ary Tree Preorder Traversal     : 1.注意 iterative 的写法，基于 Stack 实现；   2.recursion
    - [x] 590.N-ary Tree Postorder Traversal    : 1.注意 iterative 的写法，基于 Stack 实现；   2.recursion
    - [x] 104.Maximum Depth of Binary Tree      : BFS
    - [x] 111.Minimum Depth of Binary Tree      : BFS
    - [x] 637.Average of Levels in Binary Tree  :
    - [x] 993.Cousins in Binary Tree
- [x] 98.Validate Binary Search Tree
    - [x] 94.Binary Tree Inorder Traversal
        - [x] 501.Find Mode in Binary Tree          : Follow up, no extra space. Inorer traversal: 升序
        - [x] 426.Convert Binary Search Tree to Sorted Doubly Linked List
        - [x] 783.Minimum Distance Between BST Nodes
    - [x] 173.Binary Search Tree Iterator       : essentially, this is about inorder traversal 
        - [x] 285.Inorder Successor in BST
    * Iterator
        - [ ] Flatten 2D Vector
        - [ ] Zigzag Iterator
        - [ ] Peeking Iterator
    - [x] 230.Kth Smallest Element in a BST
        - [x] 671.Second Minimum Node in a Binary Tree
        - [x] 450.Delete Node in a BST      : predecessor & successor
            - [x] 776.Split BST
        - [x] 701.Insert into a Binary Search Tree  : recursion + iteration
            - [x] 700.Search in a Binary Search Tree
        - [x] 617.Merge Two Binary Trees    : recursion + iteration
        - [x] 270.Closest Binary Search Tree Value
        - [x] 272.Closest Binary Search Tree Value II
        - [ ] 222.Count Complete Tree Nodes         : Recursion, Binary Search 
    - [ ] 
    - [ ] 
    - [ ] 
    - [ ] 
    - [ ] 
    - [ ]
- [x] 94.Binary Tree Inorder Traversal
    - [x] 144.Binary Tree Preorder Traversal    : recursion + iteration, without morris
    - [x] 145.Binary Tree Postorder Traversal   : recursion + iteration, without morris
    - [x] 589.N-ary Tree Preorder Traversal     : recursion + iteration
    - [x] 590.N-ary Tree Postorder Traversal    : recursion + iteration
    - [x] 255.Verify Preorder Sequence in Binary Search Tree    : 
