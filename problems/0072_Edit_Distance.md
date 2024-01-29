[72. Edit Distance](https://leetcode.com/problems/edit-distance/)

* Google, Amazon, Square, ByteDance, Uber
* String, Dynamic Programming
* Similar Questions
    * One Edit Distance
    * [583. Delete Operation for Two Strings](https://leetcode.com/problems/delete-operation-for-two-strings/)
    * [712. Minimum ASCII Delete Sum for Two Strings](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/)
    * Uncrossed Lines

对于 `Dynamic Programming` 的问题，通常要考虑**迭代公式**的构建。因为一个 DP 问题，通常可以分解为一个小一点的子问题，再加一些基本的操作。
比如对于本题，Edit Distance：
如果要计算 `word1(0,1,...,n)` 到 `word2(0,1,...,m)` 的距离，可以首先考虑 `word1(0,1,...,n-1)` 到 `word2(0,1,...,m-1)` 之间的距离，然后再判断 `word1(n)` 与 `word2(m)` 之间是否相等，如果相等就不需更多的操作；如果不想等，则需要一步操作，比如增、删、改。


## Method 1. Dynamic Programming
```java
class Solution {
    public int minDistance(String word1, String word2) {
        if(word1==null && word2==null) {
            return 0;
        }
        if(word1 == null) {
            return word2.length();
        }
        if(word2 == null) {
            return word1.length();
        }
        
        int m = word1.length();
        int n = word2.length();
        int[][] dp = new int[m + 1][n + 1];
        for(int i=0; i<=m; i++) {
            dp[i][0] = i;
        }
        for(int j=0; j<=n; j++) {
            dp[0][j] = j;
        }
        
        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                if(word1.charAt(i) == word2.charAt(j)) {
                    dp[i+1][j+1] = dp[i][j];
                } else {
                    dp[i+1][j+1] = Math.min(dp[i][j], Math.min(dp[i+1][j], dp[i][j+1])) + 1;
                }
            }
        }
        return dp[m][n];
    }
}
```
Complexity Analysis
1. Time complexity : `O(mn)` as it follows quite straightforward for the inserted loops.
2. Space complexity : `O(mn)` since at each step we keep the results of all previous computations.


## Method 2. Recursion (Time Limit Exceeded)
```Java
class Solution {
    public int minDistance(String word1, String word2) {
        return minDistance(word1, word2, word1.length(), word2.length());
    }

    private int minDistance(String word1, String word2, int i, int j) {
        if(i == 0) {
            return j;
        }
        if(j == 0) {
            return i;
        }
        if(word1.charAt(i-1) == word2.charAt(j-1)) {
            return minDistance(word1, word2, i-1, j-1);
        } else {
            int insertOperation = minDistance(word1, word2, i, j-1);
            int deleteOperation = minDistance(word1, word2, i-1, j);
            int replaceOperation = minDistance(word1, word2, i-1, j-1);
            return Math.min(Math.min(insertOperation, deleteOperation), replaceOperation) + 1;
        }
    }
}
```
**Complexity Analysis:**
Let `M` be the length of string `word1` and `N` be the length of string `word2`. Let `K=max(M,N)`.
1. Time Complexity: `O(3^K)`. The time complexity is exponential. For every pair of word1 and word2, if the characters do not match, we recursively explore three possibilities. In the worst case, if none of the characters match, we will end up exploring `O(3^K)` possibilities.
2. Space Complexity: `O(K)`. The recursion uses an internal call stack equal to the depth of the recursion tree. The recursive process will terminate when either word1 or word2 is empty.


## Method 3. Memoization: Top-Down Dynamic Programming (3ms, beat 97%) [Recursive]
```Java
class Solution {
    private Integer[][] memo;

    public int minDistance(String word1, String word2) {
        memo = new Integer[word1.length()+1][word2.length()+1];
        return minDistance(word1, word2, word1.length(), word2.length());
    }

    // Transfer the word1[0,...,i-1] to word2[0,...,j-1], i.e. the first i chars of word1 to the first j chars of work2
    private int minDistance(String word1, String word2, int i, int j) {
        if(i == 0) return j;    // i.e. word1.length()=i, we need to insert j chars to word1
        if(j == 0) return i;    // i.e. word1.length()=i, word2="", we need to delete all i chars from word1

        if(memo[i][j] != null) {
            return memo[i][j];
        }

        int minEditDistance = 0;
        if(word1.charAt(i-1) == word2.charAt(j-1)) {
            minEditDistance = minDistance(word1, word2, i-1, j-1);
        } else {
            int insertOperation = minDistance(word1, word2, i, j-1);
            int deleteOperation = minDistance(word1, word2, i-1, j);
            int replaceOperation = minDistance(word1, word2, i-1, j-1);
            minEditDistance = Math.min(Math.min(insertOperation, deleteOperation), replaceOperation) + 1;
        }
        return memo[i][j] = minEditDistance;
    }
}
```
**Complexity Analysis:**
Let `M` be the length of string `word1` and `N` be the length of string `word2`.
1. Time Complexity: `O(M⋅N)`. As the memoization approach uses the cache, for every combination of `word1` and `word2` the result is computed only once.
2. Space Complexity: `O(M⋅N)`. The space is for the additional 2-dimensional array memo of size `(M⋅N)`.


## Method 4. Bottom-Up Dynamic Programming: Tabulation (5ms, beat 72%) [Iterative]
In the bottom-up way, the algorithm starts from the bottom, that is, the smallest sub-problem, and iteratively computes the results of the larger sub-problems.

In this problem, the smallest sub-problem is the base case where `word1` or `word2` is empty. Furthermore, the larger sub-problems are built by adding a character one by one to each of the words. 
The results of smaller sub-problems can be used to compute the result of larger ones. For this purpose, we must store the results of every sub-problem in a 2D array `dp`.
```Java
class Solution {
    public int minDistance(String word1, String word2) {
        int len1 = word1.length();
        int len2 = word2.length();
        
        // Base case 1
        if(len1 == 0) return len2;
        if(len2 == 0) return len1;

        int[][] memo = new int[len1 + 1][len2 + 1];
        for(int i=1; i<=len1; i++) {
            memo[i][0] = i;
        }
        for(int j=1; j<=len2; j++) {
            memo[0][j] = j;
        }

        for(int i=1; i<=len1; i++) {
            for(int j=1; j<=len2; j++) {
                if(word1.charAt(i-1) == word2.charAt(j-1)) {
                    memo[i][j] = memo[i-1][j-1];
                } else {
                    int insertOperation = memo[i-1][j];
                    int deleteOperation = memo[i][j-1];
                    int replaceOperation = memo[i-1][j-1];
                    memo[i][j] = Math.min(Math.min(insertOperation, deleteOperation), replaceOperation) + 1;
                }
            }
        }
        return memo[len1][len2];
    }
}
```
**Complexity Analysis:**
Let `M` be the length of string `word1` and `N` be the length of string `word2`.
1. Time Complexity: `O(M⋅N)`. In the nested for loop, the outer loop iterates MMM times, and the inner loop iterates NNN times.

Thus, the time complexity is O(M⋅N)\mathcal{O}(M \cdot N)O(M⋅N).

    Space Complexity: O(M⋅N)\mathcal{O}(M \cdot N)O(M⋅N)
        The space is for the additional 2-dimensional array dp of size (M⋅N)(M \cdot N)(M⋅N).


## Reference
* https://leetcode.com/problems/edit-distance/editorial/
* [花花酱 LeetCode 72. Edit Distance - 刷题找工作 EP87](https://www.youtube.com/watch?v=Q4i_rqON2-E)
* [贾考博 LeetCode 72. Edit Distance](https://www.youtube.com/watch?v=lCkIPGlP6Mc)
