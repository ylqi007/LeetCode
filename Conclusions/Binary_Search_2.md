# [二分查找有几种写法？它们的区别是什么？]


### [二分查找有几种写法？它们的区别是什么？ - Jason Li的回答 - 知乎](https://www.zhihu.com/question/36132386/answer/530313852)
* 搜索区间**左开右闭** `[left, right)` 
* 


### 遍历长度为 `n` 的数组，下标 `i` 该怎么写？
通常来说使用的是左闭右开的区间，也就是 `[0, n)`。这样一来循环执行的次数为 `n`，`for-loop` 结束时 `i == n`，一目了然，且无需对多余边界进行 `+/-1` 的调整。
```
for(int i=0; i<n; i++) {
    // i is in [0, n)
}
```

### 数组下标的表示方法
假设有一个长度为 4 的数组，用整数边界表示它的下标 0, 1, 2, 3：`[0, 4)` 最为合适和人道，避免了负数出现在范围表示中。

这样做的优点有：
1. 区间两端的差正好是数组的长度，如 `[0, 4)` 中的 `4 - 0 = 4` 正好是数组的长度 4。
2. 刚好相邻的区间，如 `[0, 2)` and `[2, 4)`，中间值 (即 2) 相同，一眼可见。

[off-by-one error](https://en.wikipedia.org/wiki/Off-by-one_error)


### 中点选择
```python
def lower_bound(array, first, last, value):
    while first < last:                     # Search range [first, last) is not empty.
        mid = first + (last - first) // 2   # Avoid overflow
        if array[mid] < value:
            first = mid + 1
        else:
            last = mid
    return first                            # or last, because the first and last are the same point
```

* If we use `mid = (first + last) / 2`, it may overflow in C++ or Java.
```python
mid = (first + last) / 2
    = (2 * first + last - first) / 2
    = first + (last - first) / 2
    = first + length / 2
```
其中 `length = last - first` 为区间 `[first, last)` 为区间长度。

另外，中点的选择并不唯一：
1. 上位中位数：`upperMid = first + length / 2` (不用 `-1`)
2. 下位中位数：`lowerMid = first + (length - 1) / 2`


### while-loop 的循环不变量 - loop invariants
怎样缩小区间才不会出错？        
首先要理解 `while` 循环里的 `loop invariants`(循环不变量)，也就是**代码跑到 `while` 里面时一定成立的条件**：
1. 搜索范围 `[first last)` 不为空，即 `first < last`； ==> 当 `first < last` 时，则有 `[first, last)` 不为空；
2. 搜索范围 `[first last)` 左侧，即 `[first0, first)` 内所有元素(若存在)，都小于 `value`，其中 `first0` 是 `first` 的初始值；
3. 搜索范围 `[first last)` 右侧，即 `[last, last0)` 内所有元素(若存在)，都大于等于 `value`，其中 `last0` 是 `last` 的初始值。

[example](https://www.zhihu.com/question/36132386/answer/530313852)


### 
