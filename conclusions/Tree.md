## 分析
✅⭐ 对 Tree 有关类型的题目，考虑访问到每个节点时，应该返回什么值。
* [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

## Tree 的遍历
### 1. **Preorder**: `root -> left -> right`
* Recursion: Classical + Straightforward
* Iteration: Stack + `stack.push(root)` + `while(!stack.isEmpty())` + `res.add(curr.val)` + **push from right to left**
    * 注意要 **push from right to left**, 然后才能在 `pop` 的时候遵循 **from left to right** 的顺序

### 2. **Inorder**: `left -> root -> right`
* Recursion: Classical + Straightforward
* Iteration: Stack + `while(!stack.isEmpty() || root!=null)` + `res.addFirst(curr.val)` + `root = root.right`

### 3. **Postorder**: `left -> right -> root`
* Recursion: Classical + Straightforward
* Iteration: Stack + `stack.push(root)` + `while(!stack.isEmpty())` + **push from left to right** + `res.addFirst(curr.val)`. **Must use `res.addFirst(val)`**
    * `LinkedList<Integer> res = new LinkedList<>()`: 此处要用 `LinkedList`, 因为后面要用到 `LinkedList.addFirst()`

* Traversal related questions:
- [x] 94.Binary Tree Inorder Traversal
- [x] 144.Binary Tree Preorder Traversal    : recursion + iteration, without morris
- [x] 145.Binary Tree Postorder Traversal   : recursion + iteration, without morris
- [x] 589.N-ary Tree Preorder Traversal     : recursion + iteration
- [x] 590.N-ary Tree Postorder Traversal    : recursion + iteration

## Tree 的搜索
- [x] 700.Search in a Binary Search Tree    : recuresion + iteration
- [x] 270.Closest Binary Search Tree Value
- [x] 272.Closest Binary Search Tree Value II


## Tree 的 Merge, Split, Delete and Insert
- [x] 617.Merge Two Binary Trees    : recursion + iteration
- [x] 776.Split BST
- [x] 450.Delete Node in a BST      : predecessor & successor
- [x] 701.Insert into a Binary Search Tree  : recursion + iteration
