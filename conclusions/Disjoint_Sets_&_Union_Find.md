[TOC]


# Disjoint Set (并查集)

## 1. 用与不想交集合的数据结构 [Chap 21 of 数据导论]
> 在某些应用中，要将 `n` 个不同的元素分成一组不想交的集合。
> 在不相交的集合上有两个重要操作：
> 1. 找出给定元素所属的集合；
> 2. 合并两个集合。


### 1.1 不相交集合上的操作
不相交集合数据结构 (disjoint-set data structure) 保持一组不相交的动态集合 `S = {S1, S2, ..., Sk}`。
每个集合通过一个代表来识别或表示，在某些应用中，哪一个成员被选作代表是无所谓的。

通常希望动态集合能够满足关于对象 `x` 的以下操作：
1. `MAKE-SET(X)`, 建立一个新的集合，其唯一成员就是 `x`，因而其代表也就是 `x`。因为各个集合是不相交的，故而要求 `x` 没有在其他集合中出现过。 
2. `UNION(X, Y)`, 将包含 `x` 和 `y` 的动态集合 (i.e. `Sx, Sy`) 合并成一个新的集合 (即并集操作).
3. `FIND-SET(X)`, 返回一个指针，指向包含 `x` 的集合的唯一代表。 

* 不相交集合数据结构的一个引用 (`count`)，用于确定一个无向图中连通子图的个数。

### 1.2 不相交集合的链表(List)表示
要实现不相交集合的数据结构，一种简单的方法是每个集合都用一个链表来表示。每个链表的第一个对象作为它所在集合的代表。
* **合并的一个简单实现**, 也就是合并两个链表的操作。
* **一种加权合并启发式策略**, 假设每个链表中包含了链表的长度，并且总是把较短的链表拼接到较长的链表上去；如果两个 List 一样长的话，则可以按任意顺序拼接。
使用这种简单的**加权合并启发式策略(weighted-union heuristic)**，如果两个集合都有 N 个成员的话，一次 `UNION` 操作然会需要 `\Theta(N)` 的时间。

### 1.3 不相交集合森林
在不相交的另一种更快个实现中，用有根树表示集合，树中的每个结点都表示集合中的一个成员，每棵树表示一个集合。

* **改进运行时间的启发式策略**
* 按秩合并(union by rank)
其思想是使包含较少结点的树的根指向包含较多结点的树的跟。
在 union by rank 中，具有较小秩(rank)的根要指向具有较大秩(rank)的根。

* 路径压缩(path compression)
使用这种策略，使查找路径上的每个结点都直接指向根节点。路径压缩并不改变结点的秩(rank)。

### 1.4 不相交集合森林的伪代码
``` 
MAKE-SET(x):
    p[x] = x
    rank[x] = 0


UNION(x, y):
    LINK(FIND-SET(X), FIND-SET(y))


LINK(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

or
LINK(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    elif rand[x] < rank[y]:
        p[x] = y
    else:
        p[x] = y
        rank[y] += 1


FIND-SET(x):    // with path-compression
    if x != p[x]:
        p[x] = FIND-SET(p[x])
    return p[x]
```

* **启发式策略对运行时间的影响**
> Disjoint set means two sets are not having anything common.
> Two operation: Find & Union
> Detect Cycle: 如果连接两个点，并且两个点在同一个 set 中，则说明有 cycle。


# Union-Find

## 1. Union-Find API & Template

**API**

<img src="https://algs4.cs.princeton.edu/15uf/images/uf-api.png" style="zoom:40%;" />

* `UF(int n)` , 构造器，创建一个 `UF` instance。
* `void union(int p, int q)`, 如果 `p` 和 `q` 没有连通，则进行连通。
* `int find(int p)`, 找到并返回 `p` 的 root，也就是 `parent[i] = i` 的时候，`i` 就是 root 节点。
* `boolean connected(int p, int q)`, 判断 `p` 和 `q` 两个节点是否连通，当这两个节点具有相同的 root 节点，则两者是连通的。
* `int count()`, 返回当前连通分量的个数。

**Template**
```java
class UF {
    private int count;		// 记录连通分量个数
    private int[] parent;	// 存储若干棵树
    private int[] size;		// 记录树的“重量”，也可以用 rank，记录树的高度

    public UF(int n) {
        count = n;
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    /* 将 p 和 q 连通 */
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ)		// 已经连通
            return;

        // 小树接到大树下面，较平衡
        if (size[rootP] > size[rootQ]) {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        } else {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        }
        count--;
    }

    /* 判断 p 和 q 是否互相连通 */
    public boolean connected(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        
        return rootP == rootQ;	// 处于同一棵树上的节点，相互连通
    }

    /* 返回节点 x 的根节点 */
    private int find(int x) {
        while (parent[x] != x) {
            parent[x] = parent[parent[x]];	// 进行路径压缩
            x = parent[x];
        }
        return x;
    }

    public int count() {
        return count;
    }
}
```
算法关键点：
1. 用 `parent` 数组记录每个节点的父节点，相当于指向父节点的指针，所以 `parent` 数组内部实际存储着一个森林 (若干颗多叉树)。
2. 用 `size` 数组记录着每棵树的重量，目的是让 `union` 后树依然拥有平衡性，而不会退化成链表，影响操作效率。也可以使用 `rank` 记录每棵树的高度，使树保持平衡。
3. 在 `find` 函数中进行路径压缩，保证任意树的高度保持在常数，使得 `union` 和 `connected` API 时间复杂度为 O(1)。

Union-Find 算法的关键就在于 `union` 和 `connect` 函数的效率。
那么应该用什么**模型**来表示连通图的联通状态？又该用什么**数据结构**实现代码？
`find` 主要功能是从某个节点向上遍历到树根，其时间复杂度就是树的高度。我们习惯性地认为树的高度就是 `log N`，但这并不一定。`log N` 的高度只存在于平衡二叉树中，对于一般的树而言，可能出现极端不平衡的情况，使得**树**退化成**链表**，最坏的情况下可能是变成 `N`。

### 1.1 平衡性优化
我们希望的是，小一些的树连接到大一些的树下面，这样就能避免头重脚轻的情况，使得整棵树平衡一些。解决方法是额外使用一个 `size` 数组，记录每棵树包含的节点数。比如 `size[3] = 5`，表示以节点 `3` 为根的树，总共有 5 个节点。

<img src="https://pic.leetcode-cn.com/1600677786-HPVMqN-file_1600677786373" style="zoom:50%;" />

### 1.2 路径压缩
如何进一步压缩每棵树的高度，使树的高度保持为常数。这样 `find` 就能够以 `O(1)` 的时间找到某一个节点的根节点，相应的，`connect` 和 `union` 复杂度都下降为 `O(1)`。
```java
private int find(int x) {
    while (parent[x] != x) {
        // 进行路径压缩
        parent[x] = parent[parent[x]];	// Set x's parent to parent[x]'s parent.
        x = parent[x];
    }
    return x;
}
```

<img src="https://pic.leetcode-cn.com/1600677787-AYENlA-file_1600677787301" style="zoom:50%;" />

由上图可见，调用 `find` 函数的时候，每次向树根遍历的同时，顺手将树的高度缩短了，所有的树高都不会超过 3 (进行 `union`，也就是 `connect` 的时候可能达到 3)。

### 1.3 Union-Find Complexity

构造函数的初始化数据结构需要 `O(N)` 的时间和空间复杂度；

联通两个节点的 `union`，判断两个节点的联通性 `connected`，计算联通分量 `count` 所需要的时间复杂度均为 `O(1)`。

### 1.4 Several different implementations

#### Quick-find

Quick-find Java implementation: [QuickFindUF.java](https://algs4.cs.princeton.edu/15uf/QuickFindUF.java)

```java
    /**
     * Merges the set containing element {@code p} with the 
     * the set containing element {@code q}.
     *
     * @param  p one element
     * @param  q the other element
     * @throws IllegalArgumentException unless
     *         both {@code 0 <= p < n} and {@code 0 <= q < n}
     */
    public void union(int p, int q) {
        validate(p);
        validate(q);
        int pID = id[p];   // needed for correctness
        int qID = id[q];   // to reduce the number of array accesses

        // p and q are already in the same component
        if (pID == qID) return;

        for (int i = 0; i < id.length; i++)	// 遍历整个 id array，将 id 为 pID 的所有节点的父节点设置为 qID。
            if (id[i] == pID) id[i] = qID;
        count--;
    }
```

> `p` and `q` are connected if and only if `id[p]` is equal to `id[q]`. In other words, all sites in a component must have the same value in `id[]`. 
>
> 在 quick-find 的实现方法中，在同一个连通分量中的所有节点，`id` 都是相同的。则在判断两个节点是否连通的时候，只需要一个判断语句就够了。
>
> <img src="https://algs4.cs.princeton.edu/15uf/images/quick-find-overview.png" style="zoom:90%;" />
>
> * 从上图中可以看出，当 `union(5, 9)` 的时候，`5` 的 id 为 `1`， `9` 的 id 为 `8`。将所有 id 与 `5` 相同的节点的 id 都设置为 `8`。
> * 所有 `id = 8` 的节点都在同一个连通分量中。


#### Quick-union

Quick-union java implementation: [QuickUnionUF.java](https://algs4.cs.princeton.edu/15uf/QuickUnionUF.java)

```java
    /**
     * Merges the set containing element {@code p} with the 
     * the set containing element {@code q}.
     *
     * @param  p one element
     * @param  q the other element
     * @throws IllegalArgumentException unless
     *         both {@code 0 <= p < n} and {@code 0 <= q < n}
     */
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ) return;
        parent[rootP] = rootQ; 		// 在 union 的时候，只需要将更新一个节点的父节点。
        count--;
    }
```

> A site that has a link to itself is a root; two sites are in the same component if and only if this process leads them to the same root. To validate this process, we need `union()` to maintain this invariant, which is easily arranged: we follow links to find roots associated with each of them given sites, then rename one of the components by linking one of those roots to the other.
>
> root 节点的 parent 是其本身，也就是 `parent[root] = root`；只有当两个节点的 root 节点相同的时候，两者在同一个连通分量中。要连通两个分量的时候，只需要找到分别找到它们的 root 节点，将其中一个 root 节点的 parent 设置为另一个 root 就可以，也就是 `parent[root1] = root2`。
>
> <img src="https://algs4.cs.princeton.edu/15uf/images/quick-union-overview.png" />
>
> * 从上图例子中可以看出，quick-union 在 union 的时候，只需要更新一个节点的 parent 就可以，在上例中，只需要将 `1` 的节点由 `1` 更新为 `8`。

#### Weighted quick-union

Weighted quick union Java implementation: [WeightedQuickUnionUF.java](https://algs4.cs.princeton.edu/15uf/WeightedQuickUnionUF.java)

```java
    /**
     * Merges the set containing element {@code p} with the 
     * the set containing element {@code q}.
     *
     * @param  p one element
     * @param  q the other element
     * @throws IllegalArgumentException unless
     *         both {@code 0 <= p < n} and {@code 0 <= q < n}
     */
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        if (rootP == rootQ) return;

        // make smaller root point to larger one
        if (size[rootP] < size[rootQ]) {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        } else {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        }
        count--;
    }	
```

> Rather than arbitrarily connecting the second tree to the first for `union()` in the quick-union algorithm, we keep track of the size of each tree and always connect the smaller tree to the larger.
>
> 在 quick-union 的 union 过程中，随机地将一棵树连接到另一棵树上，有可能是规模比较大的树连接到规模比较小的树上，从而造成不平衡。在 weighted quick-union 的 union 过程中，只将小树连接到比较大的树上。
>
> ![](https://algs4.cs.princeton.edu/15uf/images/weighted-quick-union-overview.png)
>
> * 第一行是 quick-union，可以看出有两种可能性。如果是以第一种方式 union 的话，则整棵树会变得不平衡。第二种 union 方式是更平衡的连接方式，但是不能保证每次都用这种方式进行连接。
> * 第二行是 weighted quick-union，weighted quick-union 总能保证树的平衡。

#### Weighted quick-union with path compression

Weighted quick-union with path compression: [WeightedQuickUnionPathCompressionUF.java](https://algs4.cs.princeton.edu/15uf/WeightedQuickUnionPathCompressionUF.java)

```java
    /**
     * Returns the canonical element of the set containing element {@code p}.
     *
     * @param  p an element
     * @return the canonical element of the set containing {@code p}
     * @throws IllegalArgumentException unless {@code 0 <= p < n}
     */
    public int find(int p) {
        validate(p);
        int root = p;
        while (root != parent[root])	// 找到节点 p 的 root 节点
            root = parent[root];
        while (p != root) {				// 将这条路径上所有节点，连接到 root 节点
            int newp = parent[p];		// track 节点 p 的 current parent
            parent[p] = root;			// 更新 p 节点的父节点为 root 节点
            p = newp;					// 将 p 节点原父节点也连接到 root 节点
        }
        return root;
    }
```

> There are a number of easy ways to improve the weighted quick-union algorithm further. Ideally, we would like every node to link directly to the root of its tree, but we do not want to pay the price of chaning a large nubmer of links. We can approach the ideal simply by making all the nodes that we do examine directly link to the root.
>
> 对于 quick-union 算法，还存在可以改进的地方。理想情况下，我们希望每个节点都直接连接到这棵树的 root 节点。



#### 总结

![](https://algs4.cs.princeton.edu/15uf/images/uf-performance.png)



## 2. Union Find 算法的应用

### 2.1 DFS 的替代方案

很多使用 DFS 深度优先算法解决的问题，也可以用 Union-Find 算法解决。

[130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)



### 2.2 判定合法等式

给你一个数组 equations，装着若干字符串表示的算式。每个算式 equations[i] 长度都是 4，而且只有这两种情况：`a==b` 或者 `a!=b`，其中 `a,b` 可以是任意小写字母。你写一个算法，如果 equations 中所有算式都不会互相冲突，返回 true，否则返回 false。

比如说，输入 `["a==b","b!=c","c==a"]`，算法返回 false，因为这三个算式不可能同时正确。

再比如，输入 `["c==c","b==d","x!=z"]`，算法返回 true，因为这三个算式并不会造成逻辑冲突。

我们前文说过，动态连通性其实就是一种等价关系，具有「自反性」「传递性」和「对称性」，其实 == 关系也是一种等价关系，具有这些性质。所以这个问题用 Union-Find 算法就很自然。

核心思想是，将 equations 中的算式根据 `==` 和 `!=` 分成两部分，先处理 == 算式，使得他们通过相等关系各自勾结成门派；然后处理 != 算式，检查不等关系是否破坏了相等关系的连通性。

```java
boolean equationsPossible(String[] equations) {
    // 26 个英文字母
    UF uf = new UF(26);
    // 先让相等的字母形成连通分量
    for (String eq : equations) {
        if (eq.charAt(1) == '=') {
            char x = eq.charAt(0);
            char y = eq.charAt(3);
            uf.union(x - 'a', y - 'a');
        }
    }
    // 检查不等关系是否打破相等关系的连通性
    for (String eq : equations) {
        if (eq.charAt(1) == '!') {
            char x = eq.charAt(0);
            char y = eq.charAt(3);
            // 如果相等关系成立，就是逻辑冲突
            if (uf.connected(x - 'a', y - 'a'))
                return false;
        }
    }
    return true;
}
```


# LeetCode题目
- [x] 🟩🌟[959. Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/)
- [ ] 🟩🌟[721. Accounts Merge](https://leetcode.com/problems/accounts-merge/) (UF, DFS)
    - [ ] [737. Sentence Similarity II](https://leetcode.com/problems/sentence-similarity-ii/)
        - [734. Sentence Similarity](https://leetcode.com/problems/sentence-similarity/)


- [ ] [Friend Cycles](), 经典的 Union Find 题目
- [ ] [Connecting Cities With Minimum Cost](), 按照 cost sort 之后，每次拿 edge，如果不相连，则 connect，totalCost += edgeCost；UF 判断是否相连。这题也可以从 Dijkstra 做，node 中存 city 和 cost，每次 poll 出来最小的 cost 连接 city，如果没有 visited 就加上，这样最后 visited 里面全部是 cities，就是最小的 cost。
- [ ] [Redundant Connection](), 经典 UF，如果两条边的 parent 相同，那么就是 redundant。
- [ ] [Redundant Connection II](), hard，此题要分三种情况讨论。
- [ ] [Connecting Graph ](https://blog.csdn.net/u013325815/article/details/103286248)标准模板；
- [ ] [Connecting Graph II](https://blog.csdn.net/u013325815/article/details/103286541)  (size的信息记录在老大哥那里，只需加一个size array就行，每次union的时候b的size += a.size; ) 
- [ ] [Connecting Graph III](https://blog.csdn.net/u013325815/article/details/103286571) (还是UnionFind的模板，注意count每次union的时候减减，就可以了。)
- [ ] [Number of Islands II](https://blog.csdn.net/u013325815/article/details/103291356) (这题就是加入一个点，然后跟他的四个连边进行union，如果四个边有1，那么进行union，result加入union之后的count；这个题是二维变成一维的union Find。题目出的还是不错的，不亏是google的题目，很有筛选性；)
- [ ] [Minimum Spanning Tree](https://blog.csdn.net/u013325815/article/details/103286722) (需要判断是否连通满了，所以需要用unionfind来判断；如何利用最小的边去connect，核心思想就是：首先把边按照value  sort一下，然后依次取出来，给city的点进行编号，然后看两个点是否connect，不connect则conenct，这样每次用的边都是value最小的，那么最后connect完了之后，所用到的value就是最小的，而且由于点全部connect了，那么后面value比较大的边，就不会用来connect了；最后如果能够形成的边如果是n-1那么就是正确答案，否则不能connect所有的点，return empty list)
- [ ] [Graph Valid Tree](https://blog.csdn.net/u013325815/article/details/103286577) 如果是tree的条件就是： 
  1. 只有一个连通块, connected component = 1;
  2. 边的数目 = 点的数目-1, i.e edges = points - 1;
- [ ] [Maximum Association Set ](https://blog.csdn.net/u013325815/article/details/103922115)(以书为node，建立一个<string,Integer> mapping, 注意size是2*n,  用不同的index代表不同的书，如果hashmap里面有了，就不用加了，是同一本书；union完之后，扫描一遍求出最大的size和最大的index，然后根据index来收集书名；注意去重，因为我是扫描了一遍书名，书名就有重复的，必须去重复；)


# Reference
1. [算法导论-36  并查集(Disjoint Set)详解](https://blog.csdn.net/BrilliantEagle/article/details/52422188)
2. [Disjoint set(并查集) data structure](https://blog.csdn.net/a130737/article/details/38438531)
4. [Union Find 题型总结](https://blog.csdn.net/u013325815/article/details/103905032)
4. [Union-Find算法应用](https://labuladong.gitbook.io/algo/gao-pin-mian-shi-xi-lie/unionfind-suan-fa-ying-yong)
5. [Union-Find 算法详解](https://leetcode-cn.com/problems/friend-circles/solution/union-find-suan-fa-xiang-jie-by-labuladong/)
6. [Leetcode总结之Union Find](https://www.cnblogs.com/zmyvszk/p/5351494.html)
7. [并查集(Union-Find)算法介绍](https://blog.csdn.net/dm_vincent/article/details/7655764)
8. [并查集(Union-Find) 应用举例 --- 基础篇](https://blog.csdn.net/dm_vincent/article/details/7769159)
9. [并查集详解 (转)](https://blog.csdn.net/dellaserss/article/details/7724401)
10. [Union-Find总结](https://maye.space/2020/06/07/Union-Find%E6%80%BB%E7%BB%93/)
11. [并查集](https://zh.wikipedia.org/wiki/%E5%B9%B6%E6%9F%A5%E9%9B%86)
12. Youtube: [并查集（Disjoint-set union）第1讲](https://www.youtube.com/watch?v=YKE4Vd1ysPI&t=322s)
13. Youtube: [并查集（Disjoint-set union）第3讲](https://www.youtube.com/watch?v=zos--xohLT0)
    * 压缩路径