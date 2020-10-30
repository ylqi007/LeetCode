[Amazon - Server Cluster](https://www.1point3acres.com/bbs/thread-662080-1-1.html)

Analysis:
1. 2D grid of servers;
2. All servers are running a special software which is represented by a single lowercase letter;
3. Adjacent servers running the same software are organized in clusters, [如果相邻的 server running the same software，则归于一个 cluster]

Input: 
1. `numOfRows`: an integer representing the number of rows in the grid;
2. `grid`: a list of strings representing the 2D grid of servers.

Output:
1. Write an algorithm to find how many clusters are in the grid currently.


[Amazon_ServerCluster](https://leetcode.com/playground/new/empty)
```java
// "static void main" must be defined in a public class.
public class Amazon_ServerCluster {
    
    public static int serverCluster(int numOfRows, List<String> grid) {
        char[][] matrix = new char[numOfRows][grid.get(0).length()];
        for(int i=0; i<numOfRows; i++) {
            matrix[i] = grid.get(i).toCharArray();
        }
        
        boolean[][] visited = new boolean[numOfRows][grid.get(0).length()];
        int M = numOfRows;
        int N = grid.get(0).length();
        int res = 0;
        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(!visited[i][j]) {
                    res++;
                    dfs(matrix, visited, i, j, matrix[i][j]);
                }
            }
        }
        return res;
    }
    
    private static void dfs(char[][] matrix, boolean[][] visited, int i, int j, char c) {
        if(i < 0 || i >= matrix.length || j < 0 || j >= matrix[0].length || visited[i][j] || matrix[i][j] != c) {
            return;
        }
        visited[i][j] = true;
        dfs(matrix, visited, i+1, j, c);
        dfs(matrix, visited, i-1, j, c);
        dfs(matrix, visited, i, j+1, c);
        dfs(matrix, visited, i, j-1, c);
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        List<String> grid1 = Arrays.asList("aabba", "aabba", "aaacb");
        int res1 = serverCluster(3, grid1);
        System.out.println(res1);
    }
}
```

