[Amazon | OA 2019 | Min Cost to Connect All Nodes](https://leetcode.com/discuss/interview-question/356981/amazon-oa-2019-min-cost-to-connect-all-nodes)

Input:

    `n`, an int representing the total number of nodes.
    `edges`, a list of integer pair representing the nodes already connected by an edge.
    `newEdges`, a list where each element is a triplet representing the pair of nodes between which an edge can be added and the cost of addition, respectively (e.g. [1, 2, 5] means to add an edge between node 1 and 2, the cost would be 5).

Example 1:

    Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
    Output: 7
    Explanation:
    There are 3 connected components [1, 4, 5], [2, 3] and [6].
    We can connect these components into a single component by connecting node 1 to node 2 and node 1 to node 6 at a minimum cost of 5 + 2 = 7.


## Method 1. UnionFind
[LeetCode - playgroudn](https://leetcode.com/playground/EwHL5ypd)
1. 先将已有的 edge connected。
2. 将 newEdges 按照 cost 进行升序排序，最小的在前。
3. 依次取出 newEdge，如果 newEdge 的两个顶点不在同一个 component 中，则必须要将其连接，因为这条 newEdge 是将两个独立的 components 相连的最小 cost。
4. 在一个 component 中，只有一个 node， `parant[nodeID] == nodeID`,
```java
// Amazon | OA 2019 | Min Cost to Connect All Nodes
// https://leetcode.com/discuss/interview-question/356960/Amazon-or-OA-2019-or-Find-Pair-With-Given-Sum

public class Main {
    int[] parent;
    int component;
    
    private int find(int v){
        if(parent[v] == v) return v;
        return parent[v] = find(parent[v]);
    }
    
    private void connect(int v1, int v2){  
        if(find(v1) == find(v2)) return;
        int root = find(v1);
        while(v2 != parent[v2]){
            int temp = parent[v2];
            parent[v2] = root;
            v2 = temp;
        }
        --component;
        parent[v2] = root;
    }
    
    private boolean isConnected(int v1, int v2){
        return find(v1) == find(v2);
    }
    
    public int minCosttoConnectAllNodes(int n, int edges[][], int newEdges[][]){
        parent = new int[n + 1]; component = n;
        for(int i = 0; i <= n; ++i) parent[i] = i;
        for(int[] edge: edges) connect(edge[0], edge[1]);
        Arrays.sort(newEdges, (a, b) -> (a[2] - b[2]));
        int cost = 0;
        for(int i = 0; i < newEdges.length; ++i){
            if(!isConnected(newEdges[i][0], newEdges[i][1])) {
                connect(newEdges[i][0], newEdges[i][1]);
                cost += newEdges[i][2];
                if(component == 1) return cost;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        Main main = new Main();
        int[] n_tests = {6};
        int[][][] edges_tests = { {{1, 4}, {4, 5}, {2, 3}}};
        int[][][] newEdges_tests = { {{1, 2, 5}, {1, 3, 10}, {1, 6, 2}, {5, 6, 5}}};
        for(int i = 0; i < n_tests.length; ++i){
            System.out.println(main.minCosttoConnectAllNodes(n_tests[i], edges_tests[i],
                                                    newEdges_tests[i]));
        }
    }
}
```

