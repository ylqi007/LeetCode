[Amazon | OA 2019 | Subtree with Maximum Average](https://leetcode.com/discuss/interview-question/349617)

[1120.Maximum Average Subtree](https://leetcode.com/problems/maximum-average-subtree/)

[Ref](https://leetcode.com/discuss/interview-question/349617/Amazon-or-OA-2019-or-Subtree-with-Maximum-Average/317193)

```java
class Solution {

    double max = Integer.MIN_VALUE;
    TreeNode maxNode = null;
    
    public TreeNode maximumAverageSubtree(TreeNode root) {
        if (root == null) {
            return null;
        }
        helper(root);
        return maxNode;
    }
    
    private double[] helper(TreeNode root) {
        if (root == null) {
            return new double[] {0, 0};    
        }
    
        double curTotal = root.val;
        double count = 1;
        for (TreeNode child : root.children) {
            double[] cur = helper(child);
            curTotal += cur[0];
            count += cur[1];
        }        
        double avg = curTotal / count;
        if (count > 1 && avg > max) { //taking "at least 1 child" into account
            max = avg;
            maxNode = root;
        }
        return new double[] {curTotal, count};
    }
}
```
Bottom up recursion, T=O(N)

```java
class Solution {
    double res = Integer.MIN_VALUE;
    
    public double maximumAverageSubtree(TreeNode root) {
        helper(root);
        return res;
    }
    
    private int[] helper(TreeNode root) {
        int[] arr = new int[2];
        if(root == null) {
            return arr;
        }
        arr[0] += root.val;
        arr[1] = 1;
        for(TreeNode child: root.children) {
            int[] tmp = helper(child);
            arr[0] += tmp[0];
            arr[1] += tmp[1];
        }
        res = Math.max(res, (double) arr[0] / arr[1]);
        return arr;
    }

}
```
