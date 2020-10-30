[Amazon | OA 2019 | Critical Routers](https://leetcode.com/discuss/interview-question/436073/)

* [Bridges and Articulation points Algorithm | Graph Theory](https://www.youtube.com/watch?v=aZXi1unBdJA)       
* [Bridges and Articulation points source code | Graph Theory](https://www.youtube.com/watch?v=V6kRqdtM_Uk)     
* [ArticulationPointsAdjacencyList.java ](https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/graphtheory/ArticulationPointsAdjacencyList.java)

* [Playground - 2019-Amazon-Critical_Routers](https://leetcode.com/playground/2hsDQZUJ)


## Method 1. 
* [Bridges and Articulation points Algorithm | Graph Theory](https://www.youtube.com/watch?v=aZXi1unBdJA)       
* [Bridges and Articulation points source code | Graph Theory](https://www.youtube.com/watch?v=V6kRqdtM_Uk) 
* [Playground - 2019-Amazon-Critical_Routers](https://leetcode.com/playground/2hsDQZUJ)
```java
// "static void main" must be defined in a public class.
public class CriticalRouters {
    
    private static int id;
    private static int rootNodeOutcommingEdgeCount;
    private static int[] ids;
    private static int[] low;
    private static boolean[] visited;
    private static boolean[] isArticulationPoint;
    private static List<List<Integer>> graph;
    public static List<Integer> getCriticalRouters(int numNodes, int numEdges, List<List<Integer>> edges) {
        List<Integer> res = new ArrayList<>();
        if(numNodes * numEdges == 0) {
            return res;
        }
        
        ids = new int[numNodes];
        low = new int[numNodes];
        visited = new boolean[numNodes];
        isArticulationPoint = new boolean[numNodes];
        
        // Initialize and create the graph
        graph = new ArrayList<>(numNodes);
        for(int i=0; i<numNodes; i++) {
            graph.add(new ArrayList<>());
        }
        for(List<Integer> e: edges) {
            graph.get(e.get(0)).add(e.get(1));
            graph.get(e.get(1)).add(e.get(0));
        }
        
        for(int i=0; i<numNodes; i++) {
            if(!visited[i]) {   // a starting point
                rootNodeOutcommingEdgeCount = 0;
                dfs(i, i, -1);
                isArticulationPoint[i] = (rootNodeOutcommingEdgeCount > 1);
            }
        }
        for(int i=0; i<numNodes; i++) {
            if(isArticulationPoint[i]) {
                res.add(i);
            }
        }
        return res;
    }
    
    private static void dfs(int root, int curr, int parent) {
        if(parent == root) {
            rootNodeOutcommingEdgeCount++;
        }
        visited[curr] = true;
        ids[curr] = id;
        low[curr] = id++;
        List<Integer> neighbors = graph.get(curr);
        for(Integer nei: neighbors) {
            if(nei == parent) {
                continue;
            }
            if(!visited[nei]) {
                dfs(root, nei, curr);
                low[curr] = Math.min(low[curr], low[nei]);
                if(ids[curr] < low[nei]) {
                    isArticulationPoint[curr] = true;
                }
                if(ids[curr] == low[nei]) {
                    isArticulationPoint[curr] = true;
                }
            } else {
                low[curr] = Math.min(low[curr], ids[nei]);
            }
        }
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        // Example 1.
        int numNodes1 = 7;
        int numEdges1 = 7;
        List<List<Integer>> edges1 = new ArrayList<>();
        edges1.add(Arrays.asList(0, 1));
        edges1.add(Arrays.asList(0, 2));
        edges1.add(Arrays.asList(1, 3));
        edges1.add(Arrays.asList(2, 3));
        edges1.add(Arrays.asList(2, 5));
        edges1.add(Arrays.asList(5, 6));
        edges1.add(Arrays.asList(3, 4));
        // for(List<Integer> edge: edges1) {
        //     System.out.println(edge);
        // }
        System.out.println(getCriticalRouters(numNodes1, numEdges1, edges1));
        
        // Example 2.
        int numNodes2 = 5;
        int numEdges2 = 6;
        List<List<Integer>> edges2 = new ArrayList<>();
        edges2.add(Arrays.asList(0, 1));
        edges2.add(Arrays.asList(0, 2));
        edges2.add(Arrays.asList(1, 2));
        edges2.add(Arrays.asList(2, 3));
        edges2.add(Arrays.asList(2, 4));
        edges2.add(Arrays.asList(3, 4));
        System.out.println(getCriticalRouters(numNodes2, numEdges2, edges2));
        
        // Example 3.
        int numNodes3 = 4;
        int numEdges3 = 4;
        List<List<Integer>> edges3 = new ArrayList<>();
        edges3.add(Arrays.asList(0, 1));
        edges3.add(Arrays.asList(1, 2));
        edges3.add(Arrays.asList(2, 3));
        edges3.add(Arrays.asList(3, 0));
        System.out.println(getCriticalRouters(numNodes3, numEdges3, edges3));
        
        // Example 4.
        int numNodes4 = 5;
        int numEdges4 = 5;
        List<List<Integer>> edges4 = new ArrayList<>();
        edges4.add(Arrays.asList(0, 1));
        edges4.add(Arrays.asList(0, 4));
        edges4.add(Arrays.asList(1, 2));
        edges4.add(Arrays.asList(2, 3));
        edges4.add(Arrays.asList(3, 0));
        System.out.println(getCriticalRouters(numNodes4, numEdges4, edges4));
    }
    
}
```


## Method 2. 
```java
// "static void main" must be defined in a public class.
public class Main {
    static int time = 0;

    private static List<Integer> getCriticalNodes(int[][] links, int numLinks, int numRouters) {
        time = 0;
        Map<Integer, Set<Integer>> map = new HashMap<>();
        for(int i=0;i<numRouters;i++) {
            map.put(i, new HashSet<>());
        }
        for(int[] link : links) {
            map.get(link[0]).add(link[1]);
            map.get(link[1]).add(link[0]);
        }
        Set<Integer> set = new HashSet<>();
        int[] low = new int[numRouters];
        int[] ids = new int[numRouters];
        int parent[] = new int[numRouters]; 
        Arrays.fill(ids, -1);       // Initially, all id is 0
        Arrays.fill(parent, -1);    // Initially, all parent is 0
        for(int i=0;i<numRouters;i++) {
            if(ids[i] == -1)
                dfs(map, low, ids, parent, i, set);
        }
        return new ArrayList<>(set);
    }

    private static void dfs(Map<Integer, Set<Integer>> map, int[] low, int[] ids, int[] parent, int cur, Set<Integer> res) {
        int children = 0; 
        ids[cur] = low[cur]= ++time;
        for(int nei : map.get(cur)) {
            if(ids[nei] == -1) {
                children++;
                parent[nei] = cur;
                dfs(map, low, ids, parent, nei, res);
                low[cur] = Math.min(low[cur], low[nei]);
                // * parent[cur] == -1 : means this is a root node, i.e. starting node
                if((parent[cur] == -1 && children > 1) || (parent[cur] != -1 && low[nei] >= ids[cur]))
                    res.add(cur);
            }
            else if(nei != parent[cur])
                low[cur] = Math.min(low[cur], ids[nei]);
        }
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        // Example 1:
        int numRouters1 = 7;
        int numLinks1 = 7;
        int[][] links1 = {{0, 1}, {0, 2}, {1, 3}, {2, 3}, {2, 5}, {5, 6}, {3, 4}};
        System.out.println(getCriticalNodes(links1, numLinks1, numRouters1));
        
        // Example 2:
        int numRouters2 = 5;
        int numLinks2 = 6;
        int[][] links2 = {{0, 1}, {0, 2}, {1, 2}, {2, 3}, {2, 4}, {3, 4}};
        System.out.println(getCriticalNodes(links2, numLinks2, numRouters2));
        
        // Example 3:
        int numRouters3 = 4;
        int numLinks3 = 4;
        int[][] links3 = {{0, 1}, {1, 2}, {2, 3}, {3, 0}};
        System.out.println(getCriticalNodes(links3, numLinks3, numRouters3));
        
        // Example 4:
        int numRouters4 = 5;
        int numLinks4 = 5;
        int[][] links4 = {{0, 1}, {1, 2}, {2, 3}, {3, 0}, {0, 4}};
        System.out.println(getCriticalNodes(links4, numLinks4, numRouters4));
        
        
    }
}
```


## Reference:
1. [Articulation Points (or Cut Vertices) in a Graph](https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/)