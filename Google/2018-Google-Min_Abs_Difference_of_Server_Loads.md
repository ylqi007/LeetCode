[Google | OA 2018 | Min Abs Difference of Server Loads](https://leetcode.com/discuss/interview-question/356433/) 

Key Points:
1. We can't compare each subarray because that is exponential, thus we need to use Dynamic Programming (DP).
2. Find the maximum value that are close to `sum / 2`;
3. `i == 0`, means that we are considering the first item now:
    * If `loads[0] <= j`, then we can take this load;
    * If `loads[0] > j`, we cannot take this load, and then the sum should be 0.
4. `i > 0`, means we are considering more than 1 items:
    * If `loads[i] > j`, means we cannot take `loads[i]`;
    * If `loads[i] <= j`, means we can take this `loads[i]`:
        * If we do not take `loads[i]`, then the sum we can get is `dp[i-1][j]`, i.e. when we have `loads[0, 1, ..., i-1]` and the max sum is `j`, the maximum sum we can get is `dp[i-1][j]`;
        * If we take `loads[i]`, then the sum we can get is `dp[i-1][j-loads[i]] + loads[i]`, where `dp[i-1][j-loads[i]]` is the max sum we can take from the first `i-1` loads, and plus the value of `loads[i]`.

[Playground - Google | OA 2018 | Min Abs Difference of Server Loads](https://leetcode.com/playground/CWz5SFEd)
```
// https://leetcode.com/discuss/interview-question/356433/
public class Main {
    
    public static int getMinAbs(int[] loads) {
        int sum = 0;    // The total sum of loads
        Arrays.sort(loads);
        for(int load: loads) {
            sum += load;
        }
        
        int[][] dp = new int[loads.length][sum / 2 + 1];
        for(int i=0; i<loads.length; i++) { // Consider each item
            for(int j=0; j<dp[i].length; j++) {
                if(i == 0) {
                    if(loads[i] <= j) { // take item i
                        dp[i][j] = Math.max(0, loads[i]);
                    } else {
                        dp[i][j] = 0;
                    }
                } else {
                    if(loads[i] > j) {
                        dp[i][j] = dp[i-1][j];
                    } else {
                        dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - loads[i]] + loads[i]);
                    }
                }
            }
        }
        return (sum - 2 * dp[loads.length - 1][sum / 2]);
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        // Example 1: 
        int[] loads1 = {1, 2, 3, 4, 5};
        System.out.println(getMinAbs(loads1));
    }
}
```


## Reference:
1. [caelandaily](https://leetcode.com/discuss/interview-question/356433/Google-or-OA-2018-or-Min-Abs-Difference-of-Server-Loads/481818)
2. [DeVil98](https://leetcode.com/discuss/interview-question/356433/Google-or-OA-2018-or-Min-Abs-Difference-of-Server-Loads/653716)
3. [The 0/1 Knapsack Problem (Demystifying Dynamic Programming)](https://www.youtube.com/watch?v=xCbYmUPvc2Q)

