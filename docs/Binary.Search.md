

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


## Refernce
* [Leetcode 题解 - 二分查找](https://blog.nowcoder.net/n/799b30349a8d4eb68f489ddc97a463c2)
* [CNoodle: [LeetCode] 二分查找模板 binary search](https://www.cnblogs.com/cnoodle/p/14267991.html)
* [【小小福讲算法】硅谷工程师十五分钟带你全面理解 Binary Search （二分查找）算法以及应用](https://www.youtube.com/watch?v=U3U9XMtSxQc&list=PL6i_0cc-sEeIH2xUJX8xrDHoEhkni1Tk8)
