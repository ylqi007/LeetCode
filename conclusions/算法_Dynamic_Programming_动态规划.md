## 1. 动态规划的三大步骤
动态规划，无非就是**利用历史记录，来避免我们的重复计算**。
而这些历史记录，我们得需要一些**变量**来保存，一般是用**一维数组**或者**二维数组**来保存。

### 1.1 定义数组元素的含义
比如当我们用一个数组(`int[] dp`)保存历史数据的时候，要规定这个数组元素的含义，比如 `dp[i]` 代表的意义。

### 1.2 找出数组元素之间的关系式
根据历史数据(`dp[n-1], dp[n-2], ..., dp[1]`)推导 `dp[n]`。

### 1.3 找出初始值
就像 Top to Bottom 的 Recursion 一样，Dynamic Programming 也需要终止条件。
因为将一个问题不断分解成子问题的时候，直到最基本的子问题的时候，就需要直接返回需要的值。


## 2. 案例详解

### 2.1 案例一、简单的一维 DP
> 问题描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

(1) 首先我们来定义 `dp[i]` 的含义: 跳上一个 `i` 级的台阶总共有 `dp[i]` 种跳法。

(2) 找出数组元素间的关系式: `dp[n] = dp[n-1] + dp[n-2]`        
由于情况可以选择跳一级，也可以选择跳两级，所以青蛙到达第 `n` 级的台阶有两种方式
* 一种是从第 `n-1` 级跳上来      
* 一种是从第 `n-2` 级跳上来      
所以有 `dp[n] = dp[n-1] + dp[n-2]`         

(3) 找出初始条件
当 `n = 1` 时，`dp[1] = dp[0] + dp[-1]`，而我们是数组是不允许下标为负数的，所以对于 `dp[1]`，我们必须要直接给出它的数值，相当于初始值，
显然，`dp[1] = 1`。一样，`dp[0] = 0`.（因为 0 个台阶，那肯定是 0 种跳法了）。于是得出初始值：       
`dp[0] = 0. dp[1] = 1. 即 n <= 1 时，dp[n] = n.`

* 上述初始化还是有问题的，当 `n=2` 的时候，`dp[2] = dp[1] + dp[0] = 1`，然而实际上 `dp[2] = 2`。所以初始化的时候，也应该将包括 `n = 2`。

### 2.2 案例二：二维数组的 DP
(0) 问题描述 ([LC 62. Unique Paths](https://leetcode.com/problems/unique-paths/))
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

(1) 定义数组元素的含义           
定义 `dp[i][j]` 的含义为：当机器人从左上角走到 `(i, j)` 这个位置时，一共有 `dp[i][j]` 种路径。

(2) 找出关系数组元素间的关系式
于机器人可以向下走或者向右走，所以有两种方式到达： (a)一种是从 (i-1, j) 这个位置走一步到达; (b)一种是从(i, j - 1) 这个位置走一步到达。          
因为是计算所有可能的步骤，所以是把所有可能走的路径都加起来，所以关系式是 `dp[i][j] = dp[i-1][j] + dp[i][j-1]`。

(3) 找出初始值           
显然，当 `dp[i][j]` 中，如果 `i` 或者 `j` 有一个为 `0`，那么还能使用关系式吗？答是不能的，因为这个时候把 `i - 1` 或者 `j - 1`，就变成负数了，
数组就会出问题了，所以我们的初始值是计算出所有的 `dp[0][0,...,n-1]` 和所有的 `dp[0,...,m-1][0]`。
* `dp[0][0,...,n-1] = 1`; // 相当于最上面一行，机器人只能一直往左走
* `dp[0,...,m-1][0] = 1`; // 相当于最左面一列，机器人只能一直往下走

```java
public static int uniquePaths(int m, int n) {
    if (m <= 0 || n <= 0) {
        return 0;
    }

    int[][] dp = new int[m][n]; // 
    // 初始化
    for(int i = 0; i < m; i++){
      dp[i][0] = 1;
    }
    for(int i = 0; i < n; i++){
      dp[0][i] = 1;
    }
        // 推导出 dp[m-1][n-1]
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
        }
    }
    return dp[m-1][n-1];
}
```

### 2.3 案例三、二维数组 DP
(0) 问题描述 ([LC 64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/))            
给定一个包含非负整数的 `m x n` 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。每次只能向下或者向右移动一步。

    举例：
    输入:
    arr = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    输出: 7
    解释: 因为路径 1→3→1→1→1 的总和最小。

(1) 定义数组元素的含义       
定义 `dp[i][j]` 的含义为：当机器人从左上角走到 `(i, j)` 这个位置时，最下的路径和是 `dp[i][j]`。

(2) 找出关系数组元素间的关系式           
机器人要怎么样才能到达 `(i, j)` 这个位置？由于机器人可以向下走或者向右走，所以有两种方式到达:        
* 一种是从 `(i-1, j)` 这个位置走一步到达         
* 一种是从 `(i, j-1)` 这个位置走一步到达         

不过这次不是计算所有可能路径，而是计算哪一个路径和是最小的，那么我们要从这两种方式中，选择一种，使得 `dp[i][j]` 的值是最小的，显然有:       
`dp[i] [j] = min(dp[i-1][j]，dp[i][j-1]) + arr[i][j];// arr[i][j] 表示网格种的值`       

(3) 找出初始值       
显然，当 `dp[i][j]` 中，如果 `i` 或者 `j` 有一个为 `0`，那么还能使用关系式吗？答是不能的。          
所以我们的初始值是计算出所有的 `dp[0][0,...,n-1]` 和所有的 `dp[0,...,m-1][0]`。这个还是非常容易计算的，相当于计算机图中的最上面一行和左边一列。因此初始值如下：         
`dp[0][j] = arr[0][j] + dp[0][j-1];` // 相当于最上面一行，机器人只能一直往左走         
`dp[i][0] = arr[i][0] + dp[i-1][0];` // 相当于最左面一列，机器人只能一直往下走         

```java
public static int uniquePaths(int[][] arr) {
    int m = arr.length;
    int n = arr[0].length;
    if (m <= 0 || n <= 0) {
        return 0;
    }

    int[][] dp = new int[m][n]; // 
    // 初始化
    dp[0][0] = arr[0][0];
    // 初始化最左边的列
    for(int i = 1; i < m; i++){
      dp[i][0] = dp[i-1][0] + arr[i][0];
    }
    // 初始化最上边的行
    for(int i = 1; i < n; i++){
      dp[0][i] = dp[0][i-1] + arr[0][i];
    }
        // 推导出 dp[m-1][n-1]
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            dp[i][j] = Math.min(dp[i-1][j], dp[i][j-1]) + arr[i][j];
        }
    }
    return dp[m-1][n-1];
}
```

### 2.4 案例 4：编辑距离       
(0) 问题描述([LC 72. Edit Distance](https://leetcode.com/problems/edit-distance/))        
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：插入一个字符 删除一个字符 替换一个字符

    示例：
    输入: word1 = "horse", word2 = "ros"
    输出: 3
    解释: 
    horse -> rorse (将 'h' 替换为 'r')
    rorse -> rose (删除 'r')
    rose -> ros (删除 'e')

(1) 定义数组元素的含义           
定义 `dp[i][j]` 的含义为：当字符串 word1 的长度为 `i`，字符串 word2 的长度为 `j` 时，将 word1 转化为 word2 所使用的最少操作次数为 `dp[i][j]`。

(2) 找出关系数组元素间的关系式           
`dp[i] [j] = min(dp[i-1] [j-1]，dp[i] [j-1]，dp[[i-1] [j]]) + 1;`

(3) 找出初始值       
显然，当 `dp[i][j]` 中，如果 `i` 或者 `j` 有一个为 0，那么还能使用关系式吗？答是不能的，因为这个时候把 `i-1` 或者 `j-1`，就变成负数了，
数组就会出问题了，所以我们的初始值是计算出所有的 `dp[0][0,...,n]` 和所有的 `dp[0,...,m][0]`。这个还是非常容易计算的，因为当有一个字符串的长度
为 `0` 时，转化为另外一个字符串，那就只能一直进行插入或者删除操作了。


## 3. 如何优化？

## 4. 优化核心：画图！画图！画图
`O(n*m)` 空间复杂度优化成 `O(n)`

### 4.1 案例1：最多路径数
(0) 问题描述        
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

(1) 优化          
将 2D 优化为 1D： `dp[i] = dp[i-1] + dp[i]`


### 4.2 案例2：编辑距离
对于这道题，我们还需要一个额外的变量 `pre` 来时刻保存 `dp(i-1,j-1)` 的值。所以推导公式可以从二维变成一维：        
`dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1] , dp[i][j-1]) + 1`    ==> `dp[i] = min(dp[i-1], pre, dp[i]) + 1`


## 5. 总结


## Top Interview 150 (1D DP)
* [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
* [198. House Robber](https://leetcode.com/problems/house-robber/)
* [139. Word Break](https://leetcode.com/problems/word-break/)
* [322. Coin Change](https://leetcode.com/problems/coin-change/)
* [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)


## Top Interview 150 (Multidimensional DP)
* [120. Triangle](https://leetcode.com/problems/triangle/description/)
* [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
* [62. Unique Paths](https://leetcode.com/problems/unique-paths/)
* [63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
* [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
* [97. Interleaving String](https://leetcode.com/problems/interleaving-string/)


## Reference:
* [告别动态规划，连刷 40 道题，我总结了这些套路，看不懂你打我（万字长文）](https://zhuanlan.zhihu.com/p/91582909)
* 灵茶山艾府: [分享丨【算法题单】动态规划（入门/背包/划分/状态机/区间/状压/数位/树形/优化）](https://leetcode.cn/discuss/post/3581838/fen-xiang-gun-ti-dan-dong-tai-gui-hua-ru-007o/)