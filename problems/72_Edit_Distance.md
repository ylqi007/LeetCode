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
