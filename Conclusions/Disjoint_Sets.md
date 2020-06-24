# Disjoint Set (并查集)

## 1. 用与不想交集合的数据结构 [Chap 21 of 数据导论]
> 在某些应用中，要将 `n` 个不同的元素分成一组不想交的集合。
> 在不相交的集合上有两个重要操作：
> 1. 找出给定元素所属的集合；
> 2. 合并两个集合。


### 1.1 不相交集合上的操作
不相交集合数据结构(disjoint-set data structure)保持一组不相交的动态集合 `S = {S1, S2, ..., Sk}`。
每个集合通过一个代表来识别或表示，在某些应用中，哪一个成员被选作代表是无所谓的。

通常希望动态集合能够满足关于对象 `x` 的以下操作：
1. `MAKE-SET(X)`, 建立一个新的集合，其唯一成员就是 `x`，因而其代表也就是 `x`。因为各个集合是不相交的，故而要求 `x` 没有在其他集合中出现过。 
2. `UNION(X, Y)`, 将包含 `x` 和 `y` 的动态集合 (i.e. `Sx, Sy`) 合并成一个新的集合 (即并集操作).
3. `FIND-SET(X)`, 返回一个指针，指向包含 `x` 的集合的唯一代表。 

#### * 不相交集合数据结构的一个引用
用于确定一个无向图中连通子图的个数。


### 1.2 不相交集合的链表(List)表示
要实现不相交集合的数据结构，一种简单的方法是每个集合都用一个链表来表示。每个链表的第一个对象作为它所在集合的代表。

#### * 合并的一个简单实现 
也就是合并两个链表的操作。

#### * 一种加权合并启发式策略
假设每个链表中包含了链表的长度，并且总是把较短的链表拼接到较长的链表上去；如果两个 List 一样长的话，则可以按任意顺序拼接。
使用这种简单的**加权合并启发式策略(weighted-union heuristic)**，如果两个集合都有 N 个成员的话，一次 `UNION` 操作然会需要 `\Theta(N)` 的时间。


### 1.3 不相交集合森林
在不相交的另一种更快个实现中，用有根树表示集合，树中的每个结点都表示集合中的一个成员，每棵树表示一个集合。

#### * 改进运行时间的启发式策略 
* 按秩合并(union by rank)
其思想是使包含较少结点的树的根指向包含较多结点的树的跟。
在 union by rank 中，具有较小秩(rank)的根要指向具有较大秩(rank)的根。

* 路径压缩(path compression)
使用这种策略，使查找路径上的每个结点都直接指向根节点。路径压缩并不改变结点的秩(rank)。

#### * 不相交集合森林的伪代码
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

#### * 启发式策略对运行时间的影响


---
> Disjoint set means two sets are not having anything common.
>
> Two operation: Find & Union
>
> Detect Cycle: 如果连接两个点，并且两个点在同一个 set 中，则说明有 cycle。



## Reference:
1. [【算法导论-36】并查集(Disjoint Set)详解](https://blog.csdn.net/BrilliantEagle/article/details/52422188)
2. [Disjoint set(并查集) data structure](https://blog.csdn.net/a130737/article/details/38438531)
3.
4. 