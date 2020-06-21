# [二分查找、二分边界查找算法的模板代码总结](https://segmentfault.com/a/1190000016825704)

> 一般而言，当一个题目出现以下特性时，你就应该立即联想到它可能需要使用二分查找：
> 1. 待查找的数组有序或者部分有序
> 2. 要求时间复杂度低于O(n)，或者直接要求时间复杂度为O(log n)


## 1. 标准二分查找
```java 
class BinarySearch {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] == target) return mid;
            else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }
}
```
* 循环条件： `left <= right`
* 中间位置计算： `mid = left + ((right -left) >> 1)`
* 左边界更新： `left = mid + 1`
* 右边界更新： `right = mid - 1`
* 返回值： `mid / -1`

几点需要注意：
1. **我们的循环条件中包含了 `left == right` 的情况，则我们必须在每次循环中改变 `left` 和 `right` 的指向，以防止进入死循环。**
如果是 `left = mid` or `right = mid`，当 `left == right` 成立进入循环的时候，`mid = left + ((right - left) >> 1) = left`，那么下次更新的时候还是 `left = right`，最终就是进入死循环。
2. 循环终止的条件包括：
    * 找到了目标值， i.e. `nums[mid] == target`
    * `left > right` （这种情况发生于当left, mid, right指向同一个数时，这个数还不是目标值，则整个查找结束。）
3. `left + ((right -left) >> 1)` 其实和 `(left + right) / 2` 是等价的，这样写的目的一个是为了防止 `(left + right)` 出现溢出，一个是**用右移操作替代除法提升性能**。
4. `left + ((right -left) >> 1)` 对于目标区域长度为奇数而言，是处于正中间的，对于长度为偶数而言，是中间偏左的。因此左右边界相遇时，只会是以下两种情况：
    * `left/mid` , `right` (i.e. `left, mid` 指向同一个数，`right` 指向它的下一个数)
    * `left/mid/right` （`left, mid, right` 指向同一个数）          
    
即因为 `mid` 对于长度为偶数的区间总是偏左的，所以当区间长度小于等于2时，`mid` 总是和 `left` 在同一侧。


* Example 1: `nums = [2, 3, 5, 7]`, `target = 1`
1. `left = 0, right = 3` --> `mid = 0 + (3 - 0) / 2 = 1` and `nums[mid] = 3 > target` --> `right = mid - 1 = 0`
2. `left = 0, right = 0` --> `mid = 0` and `nums[mid] = 2 > target` --> `right = mid - 1 = -1`
3. `return -1`

* Example 2: `nums = [2, 3, 5, 7]`, `target = 6`
1. `left = 0, right = 3` --> `mid = 0 + (3 - 0) / 2 = 1` and `nums[mid] = 3 < target` --> `left = mid + 1 = 2`
2. `left = 2, right = 3` --> `mid = 2 + (3 - 0) / 2 = 2` and `nums[mid] = 5 < target` --> `left = mid + 1 = 3`
3. `left = 3, right = 3` --> `mid = 3` and `nums[mid] = 7 > target` --> `right = mid - 1 = 3 - 1 = 2`
4. `return -1`


## 2. 二分查找左边界
> 利用二分法寻找左边界是二分查找的一个变体，应用它的题目常常有以下几种特性之一：
> 1. 数组有序，但包含重复元素
> 2. 数组部分有序，且不包含重复元素
> 3. 数组部分有序，且包含重复元素

### 2.1 左边界查找类型1
> Including above case 1 and case 2, i.e. to find the left boundary in `[left, right]` or [left, right)`

> 既然要寻找**左边界**，搜索范围就需要从右边开始，不断往左边收缩，
> 1. 当 `nums[mid] < target`，`left = mid + 1`。因为 `nums[mid] < target`，所以 `left = mid + 1` 而不是 `left = mid`。
> 2. 当 `nums[mid] == target`，此时 `mid` 也不一定是最左侧的边界，还需要继续收缩，`right = mid`。
> 3. 当 `nums[mid] > target`，此时 `right = mid`。[按理来说应该设置 `right=mid-1`]
> 此时可以将 case 2 & 3 合并，即当 `nums[mid] >= target` 时的更新规则为 `right = mid`。
```java 
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left] == target ? left : -1;
    }
}
```
* 循环条件： `left < right`
* 中间位置计算： `mid = left + ((right -left) >> 1)` ==> 1. Avoid overflow; 2. speed
* 左边界更新： `left = mid + 1`
* 右边界更新： `right = mid`
* 返回值： `nums[left] == target ? left : -1`


与标准的二分查找不同：
1. 首先，这里的右边界的更新是 `right = mid`，因为我们需要在找到目标值后，继续向左寻找左边界。
2. 其次，这里的循环条件是 `left < right`。      
因为在最后 `left` 与 `right` 相邻的时候，`mid` 和 `left` 处于相同的位置(前面说过，`mid` 偏左)，则下一步，无论怎样，`left, mid, right` 都将指向同一个位置，
如果此时循环的条件是 `left <= right`，则我们需要再进入一遍循环，此时，如果 `nums[mid] < target` 还好说，循环正常终止；否则，我们会令 `right = mid` ，这样并没有改变 `left,mid,right` 的位置，将进入死循环。           
事实上，我们只需要遍历到 `left` 和 `right` 相邻的情况就行了，因为这一轮循环后，无论怎样，`left,mid,right` 都会指向同一个位置，
而如果这个位置的值等于目标值，则它就一定是最左侧的目标值；如果不等于目标值，则说明没有找到目标值，这也就是为什么返回值是 `nums[left] == target ? left : -1`。

* 当 `left` and `right` 相邻的时候：`mid = left + (right - left) / 2 = left`
如果 `nums[mid] < target`，则有 `left = mid + 1 = right`;
如果 `nums[mid] >= target`，则有 `right = mid = left`.
所以当 `left` 和 `right` 相邻的时候，经过下一轮循环的时候，`left, mid, right` 总会指向同一个位置，不会进入死循环。

如果最后的位置 `left=mid=right` 指向的元素等于 target，则一定是最左侧的目标，否则就没有找到。
`return nums[left] == target ? left : -1`


### 2.2 左边界查找类型2
> 左边界查找的第二种类型用于数组**部分有序**且包含**重复元素**的情况，这种条件下在我们向左收缩的时候，不能简单的令 `right = mid`，因为有重复元素的存在，这会导致我们有可能遗漏掉一部分区域，**此时向左收缩只能采用比较保守的方式**。

```java 
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid;
            } else {
                right--;
            }
        }
        return nums[left] == target ? left : -1;
    }
}
```
* 它与**类型1**的唯一区别就在于对右侧值的收缩更加保守。这种收缩方式可以有效地防止我们一下子跳过了目标边界从而导致了搜索区域的遗漏。
![images](../images/154_axis.png)


## 3. 二分查找右边界
### 3.1 Pattern 1
```java 
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + ((right - left) >> 1) + 1;
            if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid;
            }
        }
        return nums[right] == target ? right : -1;
    }
}
```
* 循环条件： `left < right`
* 中间位置计算： `mid = left + ((right -left) >> 1) + 1`
* 左边界更新： `left = mid`
* 右边界更新： `right = mid - 1`
* 返回值： `nums[right] == target ? right : -1`

> 这里大部分和寻找左边界是对称着来写的，唯独有一点需要尤其注意——**中间位置的计算变了，我们在末尾多加了1**。这样，**无论对于奇数还是偶数，这个中间的位置都是偏右的**。

> 对于这个操作的理解，从对称的角度看，寻找左边界的时候，中间位置是偏左的，那寻找右边界的时候，中间位置就应该偏右呗，但是这显然不是根本原因。
> **根本原因是**，在最后 `left` 和 `right` 相邻时，如果 `mid` 偏左，则 `left, mid` 指向同一个位置，`right` 指向它们的下一个位置，在 `nums[left]` 已经等于目标值的情况下，这三个位置的值都不会更新，从而进入了死循环。
> 所以我们应该让 `mid` 偏右，这样 `left` 就能向右移动。这也就是为什么我们之前一直强调查找条件，判断条件和左右边界的更新方式三者之间需要配合使用。


## 4. 二分查找左右边界

### 实战
[34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)


## 5. 二分查找极值
> 二分查找还有一种有趣的变体是二分查找极值点，之前我们使用 `nums[mid]` 去比较的时候，常常是和给定的目标值target比，或者和左右边界比较，在二分查找极值点的应用中，我们是**和相邻元素去比**，以完成某种单调性的检测。

### 实战
[162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)

```java 
class Solution {
    public int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + ((right - left) >> 1);
            if (nums[mid] < nums[mid + 1]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}
```


## 总结
| 查找方式 | 循环条件 | 左侧更新 | 右侧更新 | 中间点位置 | 返回值 |
|:----------:|:---------------:|:----------------:|:-------------------:|:-------------------------:|:-------------:|
| 标准二分查找 | `left <= right` | `left = mid - 1` | `right = mid + 1`   | `left + (right - left) / 2`      | `-1/mid`      |
| 二分找左边界 | `left < right`  | `left = mid - 1` | `right = mid`       | `left + (right - left) / 2`      | `-1/left`     |
| 二分找右边界 | `left < right`  | `left = mid`     | `right = mid - 1`   | `left + (right - left + 1) / 2`  | `-1/right`    |

* 标准的二分查找：标准的二分查找是找一个确定的 target，因此所有的可能的位置都要进行比较。在循环条件中包含 `left == right`，则说明当搜索范围仅仅剩下一个 element 的时候，也要对最后一个 element 进行比较。
* 找左边界的时候，就排除不可能的左边界，比如说 `mid` 不可能为左边界，则更新 `left = mid + 1`，此时 `mid+1` 有可能是左边界，但 `mid` 不可能是左边界。
* 找右边界的时候，就排除不可能的右边界，比如说 `mid` 不可能为右边界，则更新 `right = mid - 1`，此时 `mid-1` 有可能是右边界，但 `mid` 不可能是右边界。
* `mid = left + (right - left) / 2`:
    * 当数组的长度为 odd 的时候，`mid` 就指向数组的中间
    * 当数组的长度为 even 的时候，`mid` 就指向数组的中间偏左，比如 `[1, 2, 3, 4]`, `mid = 0 + (3 - 0) / 2 = 1`，此时指向 2。
* `mid = left + (right - left + 1) / 2`:
    * 当数组的长度为 odd 的时候，`mid` 就指向数组的中间
    * 当数组的长度为 even 的时候，`mid` 就指向数组的中间偏右，比如 `[1, 2, 3, 4]`, `mid = 0 + (3 - 0 + 1) / 2 = 2`，此时指向 3。
* 当 `(right - left) % 2 == 0` 的时候，没有影响；让而当 `(right - left) % 2 == 1` 的时候，`(right - left) / 2` 就会自动向 0 靠近，因此偏左；
如果是 `(right - left + 1) / 2` 的话，当 `right - left == 0` 的时候，此时有没有 `+1` 并没有影响；
当 `right - left == 1` 的时候，此时有 `+1`，就自动向右靠近。
