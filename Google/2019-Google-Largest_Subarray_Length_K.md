[Google | OA 2019 | Largest Subarray Length K](https://leetcode.com/discuss/interview-question/352459/)    

Questions:
1. Since the array A contains N distinct integers, then the first element in each subarray should be unique.


## Method 1.
[Google | OA 2019 | Largest Subarray Length K](https://leetcode.com/playground/aqe34NQP)
Analysis:
1. Use a `PriorityQueue<int[]> pq` to store the `[nums[i], i]` and sorted by `nums[i]`, then we can get the largest first element.
```java
// https://leetcode.com/discuss/interview-question/352459/
public class Main {
    
    public static int[] maxSubarray(int[] nums, int k) {
        if(nums == null || nums.length == 0) {
            return nums;
        }
        int N = nums.length;
        if(k == N) {
            return nums;
        }
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (b[0] - a[0]));
        for(int i=0; i<=N-k; i++) {
            pq.offer(new int[]{nums[i], i});
        }
        int idx = pq.poll()[1];
        return Arrays.copyOfRange(nums, idx, idx+k);
    }
    
    private static void printArray(int[] arr) {
        for(int num: arr) {
            System.out.print(" " + num);
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        // Example 1:
        int[] nums1 = {1, 4, 3, 2, 5};
        int[] res1 = maxSubarray(nums1, 4);
        printArray(res1);
    }
}
```




