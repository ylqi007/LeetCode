[Amazon | OA 2019 | Max Of Min Altitudes](https://leetcode.com/discuss/interview-question/383669/)

**Don't include the first or final entry**
@KamyC Good point, I missed that condition. To fix it:

    Iterate over first row and column. Propagate the minimum value all the way down the line, but start with the second value (index 1).
    Continue as usual (start at position [1,1] and check for minimums).
    When matrix[r-1, c-1] is reached, ignore the value in matrix[r-1. c-1] when selecting the max value for the path.

https://leetcode.com/playground/jCeXqqNb

I'm not sure what the answer should be in the case of a matrix with a single value (or two values), though. Depending on the required output, we'd need to check for those special cases.

## Method 1. [Java BFS + PQ](https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/323927/Java-BFS-%2B-PQ)
> [ref](https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/323927/Java-BFS-+-PQ/455293)
> `pq.offer(new int[]{Math.min(top[0], A[r][c]), r, c});` ==> This will ensure that we always pick up next node in the priority queue with maximum smallest value.
>   * `Math.min(top[0], A[r][c])` ==> This will make sure that we always keep the minimum value of the path ending with `cell[r][c]`.
>   * The priority queue `pq` is sorted by value in descending order. ==> The top value in the pq is always the max value of current paths in the priority queue.


[Ref](https://leetcode.com/playground/new/empty)
Thought process:

    Iterate over first row and column. The minimum value must be propagated all the way down the line.
    Example:
    6, 7, 8
    5, 4, 2
    8, 7, 6
    The top row becomes 6, 6, 6 and the first column becomes 6, 5, 5. Resulting matrix:
    6, 6, 6
    5, 4, 2
    5, 7, 6

    Each of the internal elements in the grid will be the minimum of (1) itself, (2) the element above it in the grid, or (3) the element left of it in the grid. Therefore, we want to choose the maximum of two minimum comparisons. Example:
    i = 1, j = 1, element = 4.
    [i-1, j] = [0, 1] = 6
    [i, j-1] = [1, 0] = 5
    Therefore, we keep the element 4, since max(min(4, 6), min(4, 5)) == max(4, 4) == 4. For similar reasons, element [1, 2] will remain 2.

    Element [2,1], however, will become 5. Note that position [2, 1] can be reached via 6 -> 5 -> 5 -> 7, so we select max(5, 4) and choose 5 as the new element:
    i = 2, j = 1, element = 7.
    [i-1, j] = [1, 1] = 4
    [i, j-1] = [2, 0] = 5
    max(min(7, 4), min(7, 5)) == max(4, 5) == 5.
    For similar reasons, element [2, 2] will become 5.

    We return the value in the bottom right. The answer is 5.

Edit: There is a minor error in this solution, please see the replies to this comment for potential fixes. (We are supposed to ignore the first and last element in the path, which we can achieve with only minor adjustments to this algorithm.)

[Playground: Amazon-MaxMinPath](https://leetcode.com/playground/nL9ZY7G2)

```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static int maxMinPath(int[][] grid) {
        if(grid == null || grid.length == 0) {
            return 0;
        }
        // Update the first row
        for(int j=1; j<grid[0].length; j++) {
            grid[0][j] = Math.min(grid[0][j-1], grid[0][j]);
        }
        // Update the first col
        for(int i=1; i<grid.length; i++) {
            grid[i][0] = Math.min(grid[i-1][0], grid[i][0]);
        }
        for(int i=1; i<grid.length; i++) {
            for(int j=1; j<grid[0].length; j++) {
                grid[i][j] = Math.max(Math.min(grid[i-1][j], grid[i][j]), Math.min(grid[i][j-1], grid[i][j]));
            }
        }
        return grid[grid.length-1][grid[0].length-1];
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        // Testing:
        int[][] grid1 = {{5, 1}, {4, 5}};
        System.out.println("Max score should be 4: " + maxMinPath(grid1));
        
        int[][] grid2 = {{5, 1, 7}, {4, 8, 5}};
        System.out.println("Max score should be 4: " + maxMinPath(grid2));
        
        int[][] grid3 = {{1, 9, 9}, {9, 9, 9}, {9, 9, 9}};
        System.out.println("Max score should be 1: " + maxMinPath(grid3));
        
        int[][] grid4 = {{10, 7, 3}, {12, 11, 9}, {1, 2, 8}};
        System.out.println("Max score should be 8: " + maxMinPath(grid4));
        
        int[][] grid5 = {{20, 20, 3}, {20, 3, 20}, {3, 20, 20}};
        System.out.println("Max score should be 3: " + maxMinPath(grid5));
    }
}
```


or [Ref1](https://leetcode.com/discuss/interview-question/383669/Amazon-or-OA-2019-or-Max-Of-Min-Altitudes/497947)