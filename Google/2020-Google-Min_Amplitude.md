[Google | OA 2020 | Min Amplitude & Ways to Split String](https://leetcode.com/discuss/interview-question/553399/)

Question:
1. Find the minimum amplitude after changing up to 3 elements;
2. Amplitude is the range of the array (basically difference between the largest and smallest element).


Example 1:
```
Input: [-1, 3, -1, 8, 5 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5
```


Example 2:
```
Input: [10, 10, 3, 4, 10]
Output: 0
Explanation: change 3 and 4 to 10
```


Analysis: [Ref](https://leetcode.com/discuss/interview-question/553399/Google-or-OA-2020-or-Min-Amplitude-and-Ways-to-Split-String/496073)
1. 要想找到最小的 amplitude，只能从 sorted array 的两端删除数字，因为删除中间的数字并不影响 amplitude;
2. 要从长度为 `n` 的 array 中删除 `k` 个元素，最终会剩下 `n-k` 个 elements，包含的情况如下：
    * `nums[0], nums[1], ..., nums[n-k-1]`
    * `nums[1], nums[2], ..., nums[n-k]`
    * ...
    * `nums[k], nums[k+1], ..., nums[n-1]`
        * `nums[k]` is because that we remove the first-k elements, i.e. `nums[0], nums[1], ..., nums[k-1]`
        * `nums[n-1-m]` is the last element, where `m` represent how many elements we remove from the end, `m=0` means just delete from the begining, `m=k` means remove `k` elements from the end.

  
[Playground - Google | OA 2020 | Min Amplitude](https://leetcode.com/playground/FGZCGYpL)  
```java
public class MinAmplitude {
    
    public static int getMinAmplitude(int[] nums, int k) {
        // 1. Sort the array -> O(NlogN)
        Arrays.sort(nums);
        
        int N = nums.length;
        
        // 2. corner case
        if(N < k + 1) {
            return 0;
        }
        
        // 3. Iterate through all cases
        int res = nums[N-k-1] - nums[0]; 
        for(int i=1, j=N-k; j < N; i++, j++) {
            res = Math.min(res, nums[j] - nums[i]);
        }
        return res;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        // Example 1:
        int[] nums1 = {-1, 3, -1, 8, 5, 4};
        int expected1 = 2;
        System.out.println("Expected: " + expected1 + " -- " + "Output: " + getMinAmplitude(nums1, 3));
        
        // Example 2:
        int[] nums2 = {10, 10, 3, 4, 10};
        int expected2 = 0;
        System.out.println("Expected: " + expected2 + " -- " + "Output: " + getMinAmplitude(nums2, 3));
    }
}
```

   