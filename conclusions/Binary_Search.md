二分法查找是作用于 **sorted** 序列的。   
首先将要查找的元素与中间元素进行比较，
如果大于中间元素，就在当前序列的后半部分继续查找；
如果小于中间元素，就在当前序列的前半部分继续查找；
直到找到相同的元素为止。


## 2. Binary Search 痛点

### 2.1 溢出
`mid = (left + right) / 2;`
1. 在对两个 signed 32-bit 数字进行相加的时候，有可能出现溢出；比如  `left=1` and `right=Integer.MAX_VALUE`；
2. 当left和right之和超过所在类型的表示范围的话，这个和就是一个很随机的值，那么mid就不会得到正确的值。

所以，更稳妥的做法是
```bash
mid = left + (right - left) / 2;
mid = left + ((right - left) >> 1);
```

### 2.2 边界错误
> 二分法查找法的边界一般来说分为两种情况：左闭右开，即`[left, right)`；左闭右闭，即`[left, right]`。    

> 需要注意的是，循环体外的初始化条件，与循环体内的迭代条件，都必须遵守**一致的区间规则**。
也就是说，如果循环体初始化时，是以左闭右开区间为边界的，那么循环体内部的迭代也应该如此。如果两者不一致, 会造成程序的错误。

#### 2.2.1 Wrong Example
下面是个错误的例子：      
Wrong Example: 
```python
def binarySearch(arr, target):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```
算法初始化的时候，搜索范围是左闭右开 `[l, r)`，
当满足 `target > arr[mid]` 的时候，更新 `l = mid + 1;`，因为 `arr[mid]` 不可能是 `target`，所以继续在 `[mid+1, r)` 中搜索是正确的；
当满足 `target < arr[mid]` 的时候，更新 `r = mid - 1;`，所所范围就变成了 `[l, mid - 1)`，然而从判断条件可以得出 `arr[mid] != target`，但是不能确定 `arr[mid-1]` 是否为 `target`，而新的搜索范围就会跳过 `arr[mid-1]`，这将导致错误。

#### 2.2.2 左闭右闭: [l, r], end inclusive
正确的左闭右闭 `[l, r]` 写法：
```python
def binarySearch(arr, target):
    """
    定义：在[l...r]的范围里寻找target, 因为这里定义是需要将r归入范围区间, inclusive，所以while循环的边界需要包含r
    :param arr:
    :param target:
    :return:
    """
    l = 0               # index of the first element
    r = len(arr) - 1    # index of the last element
    while l <= r:
        mid = l + (r - l) / 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid + 1     # 明确区间的要求，只要使用过的，一律绕过。
        else:
            r = mid - 1     # 明确区间的要求，只要使用过的，一律绕过。
    return -1
```
* 外循环的条件是在 `[l, r]` 范围内寻找，也就是包括 `r`，所以循环条件应该为 `while l <= r`；
* 考虑一个最极端的情况 `[l, r]`, where `l == r`, 此时两个 index 都指向同一个元素，该元素也是需要比较的，因此外循环的条件应该包括 `l == r`；
* 内循环的条件是 `l = mid + 1` 和 `r = mid - 1`，此时 `mid` 不是要找的元素，所以下一轮循环要找的范围不包括 `mid`，但是应该包括 `mid` 旁边的元素，也就是 `[mid+1, r]` and [l, mid-1]。

#### 2.2.3 左闭右开: [l, r), end exclusive
```python
def binarySearch(arr, target):
    """
    定义：在[l...r)的范围里寻找target, 因为这里定义是不需要将end归入范围区间 exclusive，
    所以while循环的边界小于End即可，因为length本身长度会比index大1相对应的，
    每次target的value小于arr[mid]的时候，我们在重新定义新的end时候，也选择exclusive的模式，r = mid即可
    :param arr:
    :param target:
    :return:
    """
    l = 0           # index of the first element
    r = len(arr)    # r-1 is the index of the last element
    while l < r:
        mid = l + (r - l) / 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid + 1     # mid is not the target, so it should be exclusive
        else:
            r = mid         # mid is the right bounday, it is alreay exclusive
    return -1
```
* 外循环的条件是在 `[l, r)` 范围内寻找，也就是不包括 `r`，所以循环条件应该为 `while l < r`；
* 极端情况比如 `[l, l+1)`，此时搜索范围只有一个 element，进入循环内部后 `arr[mid] == arr[l]`，如果此时 `arr[mid] != target`，更新完搜索范围后会有两种情况：`[l+1, l+1)` or `[l, l)`，此时都会终止循环；
* 内循环的条件是 `l = mid` 和 `r = mid`，此时 `mid` 不是要找的元素，所以下一轮循环要找的范围不包括 `mid`，但是应该index 为 `mid` 的元素不在循环范围内，也就是 `[mid+1, r)` and [l, mid-1]。

### 2.3 死循环
> 上面的情况还只是把边界的其中一个写错，也就是右边的边界值写错，如果两者同时都写错的话，可能会造成死循环。
```python
def binarySearch(arr, target):
    """
    只是把边界的其中一个写错，也就是右边的边界值写错，如果两者同时都写错的话，可能会造成死循环。
    :param arr:
    :param target:
    :return:
    """
    l = 0
    r = len(arr) - 1    # inclusive
    while l <= r:
        mid = l + (r - l) / 2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid
        else:
            r = mid
    return -1
```
外循环 `while-loop` 的条件，采用的是左闭右闭 `[l, r]` 的区间，但是
* 当 `target < arr[mid]` 的时候，那么下一次查找的区间应该为 `[l, mid-1]`，而上述代码中却是 `[l, mid]`；
* 当 `target > arr[mid]` 的时候，那么下一次查找的区间应该为 `[mid+1, r]`，而上述代码中却是 `[mid, r]`;
* 如果 `l == r`，并且 `arr[l] == arr[r] == arr[mid] != target`, 此时无论更新左边界或右边界，搜索范围都不会改变，因而出现 Dead Loop。
因此，有可能出现某次查找时始终在这两个范围中轮换，造成了程序的死循环。


## 3. Templates
模板尽量符合一致性的观点；并且要有自己熟悉的模板。

### 3.1 常用模板
95% 的情况下会用这种模板。
```python
def binarySearch4(arr, target):
    """
    采用 [l, r] 的搜索范围。
    :param arr: 
    :param target: 
    :return: 
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) / 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return -1
```
* 此时采用的是 `[l, r]`，左右边界都在搜索范围内，因此当 `arr[mid] != target` 的时候，可以直接跳过 `mid`，采用 `l = mid + 1` or `r = mid - 1`。

### 3.2 备用模板
针对第一个模板的短板
```python
def binarySearch(arr, target):
    """
    [l, r]
    i.e. l <= r,
    :param arr:
    :param target:
    :return:
    """
    l = 0
    r = len(arr) - 1
    while l+1 < r:  # i.e. l < r - 1,
        mid = (l + r) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            l = mid
        else:
            r = mid
    
    if arr[l] == target:
        return l
    if arr[r] == target:
        return r
    return -1
```
第二个模板专门针对的是第一个模板的短板：当要 access 数组边界的数，如果边界的数在运行中出现更改，可能越界。虽然这种情况也可以用 `Edge Case` 来写，但太过麻烦。
* 搜索范围是 `[l, r]`, 终止条件是 `[l, l+1]`；
* 可以用于模糊搜索，如大于 target 的最小的数是多少，小于 target 的最大的数是多少等。


## 4. Binary Search 题型
![Binary Search Questions](images/binary_search.png)

### 4.1 有明确的 Target 的题型
[367.  Valid Perfect Square]()     
[33. Search in Rotated Sorted Array]()


### 4.2 没有明确的 Target 的题型
[边界处理图像化网站](http://pythontutor.com/visualize.html#mode=edit)
这一类的题比较多变，可能会要你找
* 比 Target 大的最小值
* 比 Target 小的最大值
* 满足要求的第一个值
* 不满足要求的最后一个值
* ...

思考下面的模板，在迭代退出的时候，`left` 和 `right` 的位置：  
![example 1](images/binary_ex1.png)

#### case 1: `arr = [1, 2, 3, 5, 6], target = 4`   
![case 1](images/binary_case1.jpeg)     
根据模板代码中对 while-loop 的定义 `while l <= r:`，也就是只用 `l > r` 的时候，while-loop 才会终止。
* Steps:
    1. l=0, r=4, => mid=(0+4)/2=2, target=4 > arr[mid]=3, therefore l=mid+1=3;
    2. l=3, r=4, => mid=(3+4)/2=3, target=4 < arr[mid]=5, therefore r=mid-1=2;
所以迭代结束后，`l` 和 `r` 的位置分别对应两个条件：
* `l`对应的是：第一个比4大的坐标, 根据这道题的定义就是比Target大的最小值，也就是 5；
* `r`对应的是：最后一个比4小的坐标，根据这道题的定义就是比Target小的最大值，也就是 3。

方便的理解：在循环还在进行的时候，`l`总指向比 Target 小的值，`r`总指向比 Target 大的值；当循环停止的时候，`l`第一次指向了比 Target 大的值，同理 `r` 第一次指向了比 Target 小的值。

#### case 2: `arr = [1, 2, 3, 5, 6], target = 7`
根据 while-loop 的特性，有个 edge 的情况是，`l` 最大可以等于 `len(arr)`
![case 2](images/binary_case2.jpeg)   
* Steps:
    1. l=0, r=4, => mid=(0+4)/2=2, target=7 > arr[mid]=3, therefore l=mid+1=3;
    2. l=3, r=4, => mid=(3+4)/2=3, target=7 > arr[mid]=5, therefore l=mid+1=4;
    3. l=4, r=4, => mid=(4+4)/2=4, target=7 > arr[mid]=6, therefore l=mid+1=5; ==> over the bounday
可以看出，如果要返回 `arr[l]` 则会出现系统报错，因为 `l` 已经越界，这就是这个模板的局限性。所以要记住这一点，要对相应的 edge case 处理。

* 返回 `l` 的情况
> 给定一个 Target 值，找到其在 Array 里，Target应该插入的位置：
```python
class Solution:
    def searchInsert(nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l
```

Example：        
`nums = [1, 3, 5, 6], target = 2`, `output = 1`     
1). l=0, r=3, ==> mid=0+(3-0)/2=1, target<nums[mid]=3, ==> r=mid-1=0
2). l=0, r=0, ==> mid=0+(0-0)/2=0, target>nums[mid]=1, ==> r=mid+1=1
3). return `l`

在迭代结束后，
`l` 的下标是 1, 定义是第一个满足条件的最小值；
`r` 的下标是 0, 定义是最后一个不满足条件的最大值。

所以最后返回 `l` 即可。另外，这个模板对这道题而言，不需要考虑当 Target 插入的下标等于 `len(nums)` 的 Edge Case，因为 `l` 本身就自带这个特性。

* 返回 `r` 的情况
[458. Last Position of Target (Lintcode)]()

> 给定一个 Target 值，找到其在 Array 里，Target 出现的最后坐标：
```python
class Solution:
    def lastPosition(self, nums, target):
        if not nums:
            return -1
        l , r = 0 , len(nums) - 1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[r] == target:
            return r
        else:
            return -1
```

Example：            
`nums = [1, 2, 2, 4, 5, 5], target = 2`, `return 2`         
1). l=0, r=5, ==> mid=0+(5-0)/2=2, nums[mid]<=target, ==> l=mid+1=2+1=3
2). l=3, r=5, ==> mid=3+(5-3)/2=4, nums[mid]>target,  ==> r=mid-1=4-1=3
3). l=3, r=3, ==> mid=3+(3-3)/2=3, nums[mid]>target,  ==> r=mid-1=3-1=2
4). r=2, ==> nums[r]==target ==> `return r`

在本题中，Array 出现了重复，去重的方式就是当 `nums[mid] == target` 的时候，对 `l` 进行增值。这样可以去掉左边重复的数。
如果 `mid+1` 不等于 target 呢？此时 `nums[l]` 肯定会比 target 大，因此 `l` 的位置不会发生改变。
在后面的循环中，`r` 会逐步变小，直到 `r=l-1` 时，停止循环，此时再判断 `nums[r] ~ target`。如果相等，则返回 `r`，否则返回 `-1`。

* 上两题的合体
[34. Search for a Range]()      
分别找到地一个位置和最后一个位置，然后返回一个区间。
```python
class Solution:
    def searchRange(self, nums, target):
        l = self.findLeft(nums, target)
        r = self.findRight(nums, target)
        return [l, r] if l <= r else [-1, -1]


    def findLeft(self, nums, target):
        l, mid, r = 0, 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l   


    def findRight(self, nums, target):
        l, mid, r = 0, 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r
```

### 4.3 没有明确的 Target 的题型，可越界类型
这种类型的题目，用 `l <= r` 的模板可能会越界，我们可以填写个别的Edge Case处理，或者套用其他比如 `l < r` 或者 `l + 1 < r`的模板解决。
`l < r`, 要进入循环体的时候，`[l, r)` 中至少有一个元素，所以当循环结束的时候，`l == r` 同时指向一个元素。
`l < r + 1`, 要进入循环体的时候，`[l, r)` 中至少有两个元素，所以当循环结束的时候，`[l, r)` 包含两个元素，也就是 `l` 和 `r` 指向两个相邻的元素。

[162. Find Peak Element](https://leetcode.com/problems/find-peak-element/)     
找峰值，`nums[mid]` 比对的 `nums[mid+1]`。这种情况下，当 `l` 越界等于 `len(nums)` 就会报错，所以可以选择用 `while l+1 < r` 的区间，最终对 `l` 和 `r` 进行对比。
```
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l , mid , r = 0, 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[mid + 1]:
                l = mid
            else:
                r = mid
        if nums[l] > nums[r]: return l
        else: return r
```

[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
> 这道题最终要求返回的是 `nums[l]`。同样，可以写成 Edge Case 处理，也可以使用 `while l < r` or `while l+1 < r` 来解。
```
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])
```


## 5. Other's conclusion
### 5.1 Conclusion 1
> 可以自己推一下，如果遵循下面的基本原则，就只需要一种写法。推导过程就省略了，建议大家举几个例子帮助理解，以免理解错误，毕竟自然语言是有歧义的。
> 
> 基本原则就是：
> 1. 使用闭区间 `[L, R]` (用左闭右开区间也可以，只不过要相应地修改下面的几个原则)
> 2. 永远使用 `while(L <= R)`
> 3. 永远使用 `L = mid + 1; R = mid - 1`
> 4. 退出 `while` 循环之后，`L` 和 `R` 一定满足 `L = R + 1`
> 5. `return L` 或者 `return R`
>
> 第5条需要自己现场稍微推一下，但是不难。基本规律是, 如果是按照下面的代码（假设数组 a 是单调递增序列）
```C++
if(a[mid] < target)  
    L = mid + 1;
else   
    R = mid - 1;
```
> 那么，退出 while-loop 之后，`L` 的位置一定在所有 `＜ target` 的数的右边；`R` 的位置一定在所有 `≥ target` 的熟的左边。也就是说，`a[R] <= target < a[L]`.         
> 换言之，使得 `L = mid  + 1` 的 if 语句用了什么条件，在退出 while-loop 之后，所有满足这个条件的数全都在 `L` 的左边；使得 `R = mid - 1` 的 if 语句用了什么条件，在退出 while-loop 之后，所有满足这个条件的数全都在 `R` 的右边。并且 `L = R + 1`.
> 
> 所以，如果把上面的代码改成
```C++
if(a[mid] <= target)  
    L = mid + 1;
else   
    R = mid - 1;
```
退出while循环之后，最后会得到，`a[R] < target <= a[L]，L = R + 1` 如果知道这样的表达式，最后应该 `return L` 还是 `return R`，就根据题目的具体要求来看了。


## 5.1 
> 里面把重点写出来了，我感觉主要是理解这三种模板的不同
> 1. `start, end`
> 2. loop condition, `start <= end`, `start < end`, `start + 1 < end`
> 3. move `start` or `end`, this is the key, if array have duplicate number, how to move?  这个如果不理解就很难应用好
> 4. Process the left elements(处理剩下的 elements). 

## 5.2 From  Reference 2 [二分查找学习札记](http://www.cppblog.com/converse/archive/2009/10/05/97905.aspx)
```
int search4(int array[], int n, int v)
{
    int left, right, middle;

    left = -1, right = n;

    while (left + 1 != right)
    {
        middle = left + （right － left) / 2;

        if (array[middle] < v)
        {
            left = middle;
        }
        else
        {
            right = middle;
        }
    }

    if (right >= n || array[right] != v)
    {
        right = -1;
    }

    return right;
}
```


## Reference:
1. [Binary Search的总结帖](https://www.1point3acres.com/bbs/thread-432793-1-1.html)
2. [二分查找学习札记](http://www.cppblog.com/converse/archive/2009/10/05/97905.aspx)
3. [Search in Rotated Sorted Array 解题报告 ](http://fisherlei.blogspot.com/2013/01/leetcode-search-in-rotated-sorted-array.html)
4. [Binary Search 总结帖 (更新完)](https://github.com/yuzhoujr/leetcode/issues/8)
5. [总结1](https://github.com/yuzhoujr/leetcode/issues/8#issuecomment-401414085)
6. Bilibili: [二分查找 红蓝染色法](https://www.bilibili.com/video/BV1AP41137w7/?vd_source=bd5e1cdd20d83feef8e77a781b33f083)
