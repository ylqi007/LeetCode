

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
            } else if (nums[mid] < target) {
                left = mid + 1; // New search range: [mid+1, right)
            } else {
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
