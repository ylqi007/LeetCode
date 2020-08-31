[Amazon | OA 2019 | Treasure Island](https://leetcode.com/discuss/interview-question/347457)

* Figure out a shortest route to the treasure island.
* BFS


## Method 1. BFS
[Playground - Amazon | OA 2019 | Treasure Island](https://leetcode.com/playground/LxKTF3PL)
```java
// https://leetcode.com/discuss/interview-question/347457/Amazon-or-OA-2019-or-Treasure-Island
public class Main {
    private static final int[][] DIRS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    
    public static int minSteps(char[][] grid) {
        Queue<Point> q = new ArrayDeque<>();
        q.add(new Point(0, 0));
        grid[0][0] = 'D'; // mark as visited
        for (int steps = 1; !q.isEmpty(); steps++) {
            for (int sz = q.size(); sz > 0; sz--) {
                Point p = q.poll();
            
                for (int[] dir : DIRS) {
                    int r = p.r + dir[0];
                    int c = p.c + dir[1];
                    
                    if (isSafe(grid, r, c)) {
                        if (grid[r][c] == 'X') return steps;
                        grid[r][c] = 'D';
                        q.add(new Point(r, c));
                    }
                }
            }
        }
        return -1;
    }
    
    private static boolean isSafe(char[][] grid, int r, int c) {
        return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length && grid[r][c] != 'D';
    }
    
    private static class Point {
        int r, c;
        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
    
    public static void main(String[] args) {
        char[][] grid = {{'O', 'O', 'O', 'O'},
                         {'D', 'O', 'D', 'O'},
                         {'O', 'O', 'O', 'O'},
                         {'X', 'D', 'D', 'O'}};
        System.out.println(minSteps(grid));
    }
}
```


or 

[Playground - Amazon | OA 2019 | Treasure Island_1](https://leetcode.com/playground/aJN4AcPR)


