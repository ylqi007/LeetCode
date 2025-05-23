
## LeetCode Explore Card提供的三种模板
### 1. Template 1: The most basic and elementary form of Binary Search: Find a target number
```java
class Solution {
   public int binarySearch(int[] nums, int target) {
      // Corner case
      if (nums == null || nums.length == 0)
         return -1;

      // Initial search space
      int left = 0;
      int right = nums.length - 1;
      while (left <= right) {
         int mid = left + (right - left) / 2;    // Prevent (left + right) overflow
         if (nums[mid] == target) {
            return mid;
         } else if (nums[mid] < target) {
            left = mid + 1;  // Searching Right: left = mid+1
         } else {
            right = mid - 1; // Searching Left: right = mid-1
         }
      }

      // End Condition: left > right
      return -1;
   }
}
```
**Key Attributes:**
* Most basic and elementary form of Binary Search
* Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
* No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found

**✅ Distinguishing Syntax(区分的语法要点):**
1. Initial Condition: `left = 0, right = length-1`, 即搜索区间为 `[left, right]`，两端都闭合。
2. Termination: `left > right`
3. Find the target: `nums[mid] == target`, return directly.
4. Searching Left: `right = mid-1`, because `nums[mid]` cannot be the answer.
5. Searching Right: `left = mid+1`, because `nums[mid]` cannot be the answer.

**典型LeetCode题目:**
* ✅ [704. Binary Search](https://leetcode.com/problems/binary-search/description/)
* ✅ [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/description/)
* [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/description/)
* ✅ [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)


### 2. Template 2: An advanced form of Binary Search
```java
class Solution {
    private int binarySearch(int[] nums, int target) {
        // Corner case: There is no enough search space
        if (nums == null || nums.length == 0) return -1;
        
        int left = 0;
        int right = nums.length - 1;    // Search space: [left, right]
        while (left < right) {
            int mid = left + (right - left) / 2;  // Prevent (left + right) overflow
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        } // End Condition: left == right
        
        // Post-processing: 
        if (nums[left] == target) return left;
        return -1;
   }
}
```
**Key Attributes:**
* An advanced way to implement Binary Search.
* **Use the element's right neighbor to determine if the condition is met and decide whether to go left or right**
* **Guarantees Search Space is at least 2 in size at each step**
* Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.

**✅ Distinguishing Syntax:**
1. Initial Condition: `left = 0, right = length - 1`
2. Termination: `left == right`
3. Searching Left: `right = mid` 
4. Searching Right: `left = mid+1`

**典型LeetCode题目:**
* [278. First Bad Version](https://leetcode.com/problems/first-bad-version/description/)
* [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)
* [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)


### 3. Template 3: 
```java
class Solution {
    private int binarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0) 
            return -1;
        
        int left = 0, right = nums.length - 1;
      
        while (left + 1 < right){
            // Prevent (left + right) overflow
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid;
            } else {
                right = mid;
            }
        }

        // Post-processing:
        // End Condition: left + 1 == right
        if(nums[left] == target) return left;
        if(nums[right] == target) return right;
        return -1;
    }
}
```
**Key Attributes:**
* An alternative way to implement Binary Search
* **Use the element's neighbors to determine if the condition is met and decide whether to go left or right**
* **Guarantees Search Space is at least 3 in size at each step**
* Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.

**✅ Distinguishing Syntax:**
1. Initial Condition: `left = 0, right = length-1`
2. Termination: `left + 1 == right`
3. Searching Left: `right = mid`
4. Searching Right: `left = mid`

**典型LeetCode题目:**
* ✅ [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
* [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)
* [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)
* ✅ [1060. Missing Element in Sorted Array](https://leetcode.com/problems/missing-element-in-sorted-array/description/)



### 1. 模板1: 在有序数组中查找目标值
```java
class Solution {
    public int binarySearch2(int[] nums, int target) {
        // left和right都在数组下标范围内: [left, right], both left and right included
        int left = 0;
        int right = nums.length - 1;
        // while循环跳出的条件是right < left
        // 如果没找到target的话，也不需要特判了
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;     // New search range: [left', right], where left'=mid+1, since nums[mid] is not considered anymore
            } else {
                right = mid - 1;    // New search range: [left, right'], where right'=mid-1
            }
        }
        // 如果没找到就只能返回-1
        return -1;
    }
}
```
**Note:**
1. 最初的搜索范围是`[left, right]`，左右index都在搜索范围内。
2. 每次移动`left`, `right`之后的新范围，依然是`[left, right]`

**理解重点:**
1. `[left, right]`左右皆为闭区间，将`[left, right]`想象成可行解区间(i.e.在这个区间之外，目标一定不会存在，在这个区间中，目标可能存在)。
2. 终止条件。如果没有搜索到结果，最后的指针一定是`right+1==left (right<left)`(也就是说，可行解区间`[left, right]`是一个空区间，比如区间`[2, 1])。
3. 模板特点:
   1. Initial condition: `left=0, right=length-1`
   2. Terminal condition: `left > right`
   3. Searching left: `right=mid-1`(此处right, mid均为index)
   4. Searching right: `left=mid+1`(此处left, mid均为index)


### 2. 模板2: 适合判断当前index和index+1之间的关系
```java
class Solution {
    public int binarySearch3(int[] nums, int target) {
        // [left, right), right不在下标范围内
        int left = 0;
        int right = nums.length;
        // while循环跳出的条件是left == right
        // 这个模板比较适合判断当前index和index + 1之间的关系
        // left < right, example, left = 0, right = 1
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {    // index mid is not result, therefore set left as mid+1
                left = mid + 1; // New search range: [mid+1, right)
            } else {            // target <= prefixSum[mid], new internal is [left, mid)
                right = mid;    // New search range: [left, mid), 因为搜索范围是左闭右开所以这里不能-1
            }
        }
        // 最后的特判
        if (left != nums.length && nums[left] == target) {
            return left;
        }
        return -1;
    }
}
```
**Note:**
1. 最初的搜索范围是: `[left, right)`, include `left`, exclude `right`
2. 每次移动后的搜索范围依然是: `[left, right)`

**理解重点:**
1. `[left, right)`为左闭右开区间。
2. 终止条件。如果没有搜索到结果，最后指针一定是`left==right`(也就是说，可行解区间`[left, right)`是一个空区间，比如说`[2,2)`)
3. 模板特点:
   1. Initial condition: `left=0, right=length`
   2. Terminal condition: `left==right`
   3. Searching left: `right=mid`
   4. Searching right: `left=mid+1`
4. 适用范围: 需要mid和mid+1两个元素同时判断左右

**思考:** 为什么是`left=mid+1; right=mid`，而不是`left=mid; right=mid-1`? (Hint: `left+1==right`的情况)


### 3. 模板3: 适合查找有序数组中是否存在某个元素
```java
class Solution {
    public int binarySearch1(int[] nums, int target) {
        // [left, right], left和right都在数组下标范围内
        int left = 0;
        int right = nums.length - 1;
        // 举例，start - 0, end = 3
        // 中间隔了起码有start + 1和start + 2两个下标
        // 这样跳出while循环的时候，start + 1 == end
        // 才有了最后的两个判断
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid;
            } else {
                right = mid;
            }
        }
        // 特判
        if (nums[left] == target) {
            return left;
        }
        if (nums[right] == target) {
            return right;
        }
        // 如果没找到就只能返回-1
        return -1;
    }
}
```

**总结:**
1. Binary Search是一个在`O(logN)`时间在有序区间实现搜索的算法
2. 两大原则:
   1. 每次都要缩减搜索区域(Shrink the search space every iteration or recursion)
   2. 每次缩减不能排除潜在答案(Cannot exclude potential answers during each shrinking)
3. 三种变种
4. 三大模板
   1. 找一个准确值
      * 循环条件: `l<=r`
      * 缩减搜索空间: `l=mid+1, r=mid-1`
   2. 找一个模糊值
      * 循环条件: `l<r`
      * 缩减搜索空间: `l=mid, r=mid-1` or `l=mid+1, r=mid`
   3. 万用型
      * 循环条件: `l<r-1`
      * 缩减搜索空间: `l=mid, r=mid`



## LeetCode Problems
* 1062 Longest Repeating Substring
* 410 Split Array Largest Sum
* 1231 Divide Chocolate
* 852 Peak Index in a Mountain Array
* 1011 Capacity To Ship Within D Days 
* 1292 Maximum Side Length of a Square with Sum Less than or Equal to Threshold

## Top 100
* [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
* [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
* [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
* [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
* [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)
* [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
* [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)


## 高频题目(截自2024/03/19)
* 4	    Median of Two Sorted Arrays
* 2009	Minimum Number of Operations to Make Array Continuous
* 1235	Maximum Profit in Job Scheduling
* 528	Random Pick with Weight
* [2513. Minimize the Maximum of Two Arrays](https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/description/)
* 2468	Split Message Based on Limit
* ✅ [162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)
* [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)
* [362. Design Hit Counter](https://leetcode.com/problems/design-hit-counter/description/) [Binary Search?]
* 2251	Number of Flowers in Full Bloom
* 300	Longest Increasing Subsequence
* 1268	Search Suggestions System
* 34	Find First and Last Position of Element in Sorted Array
* 1838	Frequency of the Most Frequent Element
* 33	Search in Rotated Sorted Array
* [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
* [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
* 981	Time Based Key-Value Store
* 456	132 Pattern
* ✅ [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)
* [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
  * [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
* 1802	Maximum Value at a Given Index in a Bounded Array
* [268. Missing Number](https://leetcode.com/problems/missing-number/description/) (没看出来跟Binary Search有关)
* [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/description/)
* [704. Binary Search](https://leetcode.com/problems/binary-search/description/)
* [825. Friends Of Appropriate Ages](https://leetcode.com/problems/friends-of-appropriate-ages/description/)



## Refernce
* [LeetCode Explore Card: Binary Search](https://leetcode.com/explore/learn/card/binary-search/)
* [Leetcode 题解 - 二分查找](https://blog.nowcoder.net/n/799b30349a8d4eb68f489ddc97a463c2)
* ✅ [CNoodle: [LeetCode] 二分查找模板 binary search](https://www.cnblogs.com/cnoodle/p/14267991.html)
* ✅ [CNoodle: LeetCode Binary Search Summary 二分搜索法小结](https://www.cnblogs.com/grandyang/p/6854825.html)
* [【小小福讲算法】硅谷工程师十五分钟带你全面理解 Binary Search （二分查找）算法以及应用](https://www.youtube.com/watch?v=U3U9XMtSxQc&list=PL6i_0cc-sEeIH2xUJX8xrDHoEhkni1Tk8)
* [二分查找Binary Search套路和解题模板【LeetCode刷题套路教程3】](https://www.youtube.com/watch?v=j2_JW3In9PE&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=3)
* ✅ [力扣: 排除法（双指针）+ 二分法（Java、Python）](https://leetcode.cn/problems/find-k-closest-elements/solutions/12476/pai-chu-fa-shuang-zhi-zhen-er-fen-fa-python-dai-ma/)
* ✅ [力扣: 通过二分法确定左边界](https://leetcode.cn/problems/find-k-closest-elements/solutions/376097/tong-guo-er-fen-fa-que-ding-zuo-bian-jie-by-hao-ha/)
* ✅ [二分查找细节详解，顺便赋诗一首](https://leetcode.cn/problems/binary-search/solutions/8337/er-fen-cha-zhao-xiang-jie-by-labuladong/)
  * 详细讲解了如何更新左右指针的情况。

## 技巧
* 分析二分查找的一个技巧是：不要出现 else，而是把所有情况用 else if 写清楚，这样可以清楚地展现所有细节。
* 