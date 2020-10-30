* Strongly Connected Components (SCCs) can be thought of as **self-contained cycles** within a **directed graph** where every vertex in a given cycle can reach every other vertex in the same cycle.
[强连通分量，在有向图中的自包含的环结构，也就是在这个结构中的每一个点都可以到达环中的其他点。]

* The **low-link** value of a node is the smallest (i.e. lowest) node is reachable from that node when doing a DFS (including itself).
[low-link 值，就是从某个节点出发，可以达到的所有节点中，最小的 id。]

* Depending on where the DFS starts and which edges are visited the low-link values could be wrong. In the context of Tarjan's SCC algorithm we maintain an invariant that prevents SCCs to interfere with each other's low-link values.
[对于某些节点和某些边的访问顺序的不同，会导致某些点的 low-link value 不同，最终可能导致错误的结果。]

* Solution - The **Stack Invariant**： To cope with the random traversal order of the DFS, Tarjan's algorithm maintains a set (often as a stack) of valid nodes from which to update low-link values from. [也就是用一个 stack 存储可以更新 low-link value 的节点]
    * Nodes are added to the stack (i.e. set) of valid nodes as they're explored for the first time.
    * Nodes are removed from the stack (i.e. set) each time a complete SCC is found.

* New low-link update condition:
    * If `u` and `v` are nodes in a graph and we're currently exploring `u` then our new low-link update condition is that:
        * To update node `u`'s low-link value to node `v`'s low-link value there has to be a path of edges from `u` to `v` and node `v` must be on the stack.
     
* Time complexity: `O(V + E)`

 
* Psuode Code
```
UNVISITED = -1
n = number of nodes in the graph
g = adjacency list with directed edges

id = 0          # Used to give each node an id
sccCount = 0    # Used to count number of SCCs found

# Index i in there arrays represents node i
ids = [0, 0, ..., 0, 0]                         # with length n
low = [0, 0, ..., 0, 0]                         # with length n
onStack = [false, false, ..., false, false]     # With length n
stack = an empty stack data structure


function findSCCs():
    for(int i=0; i<n; i++): ids[i] = UNVISITED   # Initialize all ids as unvisited
    for(int i=0; i<n; i++): 
        if(ids[i] == UNVISITED):
            dfs(i)
    return low      # I.e. low-link values of each node


function dfs(at):
    stack.push(at)
    onStack[at] = true
    ids[at] = low[at] = id++

    # Visited all neighbors & min low-link on callback
    for(to: g[at]):
        if(ids[to] == UNVISITED): dfs(to)
        if(onStack[to]) : low[at] = min(low[at], low[to])

    # After having visited all the neighbors of `at`
    # If we're at the start of a SCC empty the seen stack until we're back to the start of the SCC.
    if(ids[at] == low[at]):
        for(node = stack.pop(); ...; node = stack.pop()):
            onStack[node] = false;
            low[node] = ids[at]
            if(node == at):
                break
        sccCount++
```  
