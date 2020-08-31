[Amazon | OA 2019 | Find Pair With Given Sum](https://leetcode.com/discuss/interview-question/356960)


[Playground - Amazon | Find Pair With Given Sum](https://leetcode.com/playground/A6VpFxhx)

The corresponding problem is "Truck Package". If you suffer from 11/13 passed test cases, try to consider the following aspects:
1. Return null or empty list. You can test it out.
2. Consider when there is no such a pair, return null or empty list. Again, one of them is correct~
3. Consider a test case like [0, 0] and target = 30. Do you think it is a valid pair? YES!
4. I had been trying for 30 mins this morning. Please upvote. THX!~


```java
// https://leetcode.com/discuss/interview-question/356960
public class Main {
    
    public static List<Integer> findPair(List<Integer> nums, int target) {
        target -= 30;
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> result = Arrays.asList(-1, -1);
        int largest = 0;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums.get(i);
            if ((nums.get(i) > largest || complement > largest) && map.containsKey(complement)) {
                result.set(0, map.get(complement));
                result.set(1, i);
                largest = Math.max(nums.get(i), complement);
            }
            map.put(nums.get(i), i);
        }
        return result;
    }

    public static void main(String[] args) {
        test(Arrays.asList(1, 10, 25, 35, 60), 90);
        test(Arrays.asList(20, 50, 40, 25, 30, 10), 90);
        test(Arrays.asList(5, 55, 40, 20, 30, 30), 90);
    }
    
    private static void test(List<Integer> nums, int target) {
        System.out.println(findPair(nums, target));
    }
}
```
Complexity:
1. Time complexity: O(n).
2. Space complexity: O(n).

