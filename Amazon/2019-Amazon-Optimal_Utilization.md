[Amazon | OA 2019 | Optimal Utilization](https://leetcode.com/discuss/interview-question/373202)

[LeetCode - playground](https://leetcode.com/playground/oSCWW6dY)


Your task is to find an element from `a` and an element from `b` such that the sum of their values is less or equal to `target` and as close to `target` as possible.
Return a list of ids of selected elements.


* Note 1: To get all the matching pair of the current index i towards left of j

```java
public class OptimalUtilization_TwoSum {
    
    public static List<int[]> getPairs(List<int[]> a, List<int[]> b, int target) {
        Collections.sort(a, (o1, o2) -> (o1[1] - o2[1]));   // a[0] is index, a[1] is value
        Collections.sort(b, (o1, o2) -> (o1[1] - o2[1]));   // b[0] is index, b[1] is value
        
        List<int[]> res = new ArrayList<>();
        int m = a.size();
        int n = b.size();
        int i = 0;
        int j = n - 1;
        int max = Integer.MIN_VALUE;
        while(i < m && j >= 0) {
            int sum = a.get(i)[1] + b.get(j)[1];
            if(sum > target) {
                j--;
            } else {    // i.e. sum <= target
                if(sum > max) { // If sum is larger than previous sum, then clear the res array
                    max = sum;
                    res.clear();
                }
                res.add(new int[]{a.get(i)[0], b.get(j)[0]});   // Since this is already the largest sum recently.
                int idx = j - 1;
                while(idx >= 0 && b.get(idx)[1] == b.get(idx+1)[1]) {   // Note 1.
                    res.add(new int[]{a.get(i)[0], b.get(idx--)[0]});
                }
            }
            i++;    // keep the j at the same position
        }
        return res;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        /*
        * Example 1:
        * a = [[1, 2], [2, 4], [3, 6]]
        * b = [[1, 2]]
        * target = 7
        */
        List<int[]> a1 = new ArrayList<>();
        a1.add(new int[]{1, 4});
        a1.add(new int[]{2, 4});
        a1.add(new int[]{3, 4});
        List<int[]> b1 = new ArrayList<>();
        b1.add(new int[]{1, 2});
        b1.add(new int[]{2, 2});
        int target1 = 7;
        List<int[]> res1 = getPairs(a1, b1, target1);
        for(int[] r: res1) {
            System.out.println("[" + r[0] + "," + r[1] + "]");
        }
    }
}
```

    O(nlgn) time O(1) space complexity (not counting the result array which automatically makes it O(n)), n being the total number of elements in two lists.
    just noticed when every possible pair has the same sum, worst case is O(n^2), thanks for the heads up. But why do you think space is lgn? Given worst case and taking the output array in to consideration space is n^2, if not, then amount of memory you use do not change with respect to your input size aka O(1)
    