[Amazon | OA 2019 | Two Sum - Unique Pairs](https://leetcode.com/discuss/interview-question/372434)

[LeetCode -- Playground](https://leetcode.com/playground/kV4GrKoa)

```java
// "static void main" must be defined in a public class.
public class UniquePairs {
    
    public static int uniquePairs(int[] nums, int target) {
        Set<Integer> set = new HashSet<>();
        Set<Integer> seen = new HashSet<>();
        int res = 0;
        for(int num: nums) {
            if(set.contains(target - num) && !seen.contains(num)) {
                res++;
                seen.add(target - num);
                seen.add(num);
            } else if(!set.contains(num)) {
                set.add(num);
            }
        }
        return res;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        int[] nums1 = new int[]{1, 1, 2, 45, 46, 46};
        int target1 = 47;
        System.out.println("Expected output is 2: -- " + uniquePairs(nums1, target1));
        
        int[] nums2 = new int[]{1, 1};
        int target2 = 2;
        System.out.println("Expected output is 1: -- " + uniquePairs(nums2, target2));
        
        int[] nums3 = new int[]{1, 5, 1, 5};
        int target3 = 6;
        System.out.println("Expected output is 1: -- " + uniquePairs(nums3, target3));
    }
}
```