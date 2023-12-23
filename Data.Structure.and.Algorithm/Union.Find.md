# Union Find

灵活使用**并查集**的思想，熟练掌握并查集的**模板**，模板中有两种并查集的实现方式，一种是路径压缩 + 秩优化的版本，另外一种是计算每个集合中元素的个数 + 最大集合元素个数的版本，这两种版本都有各自使用的地方。


## Template (模板)
```Java
class UF {
    /* 将 p 和 q 连接 */
    public void union(int p, int q);
    /* 判断 p 和 q 是否连通 */
    public boolean connected(int p, int q);
    /* 返回图中有多少个连通分量 */
    public int count();
}
```



* https://leetcode.com/problems/redundant-connection/editorial/
* https://github.com/halfrost/LeetCode-Go/tree/master#union-find
* https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-03a72/bing-cha-j-323f3/
