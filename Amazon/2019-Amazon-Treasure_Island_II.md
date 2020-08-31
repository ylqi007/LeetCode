[Amazon | OA 2019 | Treasure Island II](https://leetcode.com/discuss/interview-question/356150)    

*
*
*
*

[Playground - Amazon | OA 2019 | Treasure Island II](https://leetcode.com/playground/JA4gVDq7)
```java
// "static void main" must be defined in a public class.
public class Main {
    
    private static final int[][] DIRS = {{0, -1}, {0, 1}, {1, 0}, {-1, 0}};
    
    public static int minDist(char[][] grid) {
        Queue<Point> queue = collectSources(grid);
        
        for(int dist=0; !queue.isEmpty(); dist++) {
            for(int size=queue.size(); size>0; size--) {
                Point p = queue.poll();
                
                if(grid[p.r][p.c] == 'X') {
                    return dist;
                }
                grid[p.r][p.c] = 'D';   // marked as visited
                
                for(int[] dir: DIRS) {
                    int r = p.r + dir[0];
                    int c = p.c + dir[1];
                    if(isSafe(grid, r, c)) {
                        queue.offer(new Point(r, c));
                    }
                }
            }
        }
        return -1;
    }
    
    public static Queue<Point> collectSources(char[][] grid) {
        Queue<Point> sources = new ArrayDeque<>();
        for(int r=0; r<grid.length; r++) {
            for(int c=0; c<grid[0].length; c++) {
                if(grid[r][c] == 'S') {
                    sources.offer(new Point(r, c));
                }
            }
        }
        return sources;
    }
    
    public static boolean isSafe(char[][] grid, int r, int c) {
        return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length && grid[r][c] != 'D';
    }
    
    private static void test(int actual, int expected) {
        if (actual == expected) {
            System.out.println("PASSED!");
        } else {
            System.out.println(String.format("FAILED! Expected: %d, but got: %d", expected, actual));
        }
    }
    
    private static class Point {
        int r;
        int c;
        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        char[][] grid = {
            {'S', 'O', 'O', 'S', 'S'},
            {'D', 'O', 'D', 'O', 'D'},
            {'O', 'O', 'O', 'O', 'X'},
            {'X', 'D', 'D', 'O', 'O'},
            {'X', 'D', 'D', 'D', 'O'}}; 
        int output = minDist(grid);
        System.out.println(output);
        test(output, 3);
    }
}
```

[Playground - Amazon | OA 2019 | Treasure Island II_1](https://leetcode.com/playground/MriF5Zb6)
```java
// Amazon | OA 2019 | Shortest Path From Multiple Sources
// https://leetcode.com/discuss/interview-question/356150

public class Main {
    final int[][] dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    public int shortestPath(char[][] islands){
        if(islands.length == 0 || islands[0].length == 0) return -1;
        int R = islands.length, C = islands[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int steps = 1;
        // add all sources to queue and set 'visited'.
        for(int i = 0; i < R; ++i){
            for(int j = 0; j < C; ++j){
                if(islands[i][j] == 'S'){
                    queue.add(new int[]{i, j}); islands[i][j] = 'D';
                }
            }
        }
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; ++i){
                int[] pos = queue.poll();
                for(int[] dir: dirs){
                    int x = pos[0] + dir[0], y = pos[1] + dir[1];
                    if(x < 0 || x >= R || y < 0 || y >= C || islands[x][y] == 'D') continue;
                    if(islands[x][y] == 'E') return steps;
                    queue.add(new int[]{x, y});
                    islands[x][y] = 'D';
                }
            }
            ++steps;
        }
        return -1;
    }
    public static void main(String[] args) {
        Main main = new Main();
        char[][] testcase = {   {'S', 'O', 'O', 'S'},
                                {'D', 'O', 'D', 'D'},
                                {'O', 'O', 'O', 'E'},
                                {'E', 'D', 'D', 'O'}};
        System.out.println(main.shortestPath(testcase));
    }
}
```
