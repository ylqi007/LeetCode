# Quick Select & Quick Sort

Quick Select主要用于在未排序的数组中寻找k-th数字的问题。


### Quick Sort (快速排序) + Quick Select (快速选择)
快速排序（QuickSort）是一种常用的排序算法，采用分治法（Divide and Conquer）策略。其基本思想是通过一个"基准"元素（pivot）将待排序序列分为两部分，其中一部分比基准小，另一部分比基准大，然后递归地对这两部分继续排序。

**快速排序的步骤:**
1. 选择基准元素（pivot）：通常选择数组的第一个元素、最后一个元素，或者随机选择一个元素作为基准。
2. 分割操作：将数组重新排列，使得基准元素左边的元素都小于基准，右边的元素都大于基准。这个操作被称为“分区”。
3. 递归排序：对基准元素左边和右边的子数组进行递归排序。

**快速排序的时间复杂度:**
* 平均时间复杂度：`O(n log n)`，这发生在每次划分后，子问题大小大致相等时。
    * 最坏时间复杂度：`O(n²)`，当每次选择的基准元素是数组中的最大或最小值时，性能会退化到O(n²)。
* 空间复杂度：O(log n)，由于递归调用的栈空间。

**优缺点:**
* 优点：
    * 平均情况下表现良好，时间复杂度为`O(n log n)`。
    * 排序效率较高，特别是在数据较大时。
* 缺点：
    * 最坏情况下时间复杂度为`O(n²)`，通常可以通过选择合适的基准元素（如随机选择基准）来避免。
    * 不稳定排序：相等元素的顺序可能会改变。

## Quick Select 🆚 Quick Sort
LeetCode 215, 347 and 973，我都用了自己的模板。要记住！！！

## Quick Sort


## LeetCode Problems
* ✅⭐ [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/) 的讲解不错，其中提到的实现简单易理解。
* ✅⭐ [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)
* ✅⭐ [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)



## Reference
* ✅⭐LeetCodeCN: [使用快排但是慢的看过来](https://leetcode.cn/problems/kth-largest-element-in-an-array/solutions/307351/shu-zu-zhong-de-di-kge-zui-da-yuan-su-by-leetcod-2/comments/2352693)
* ✅⭐ [双路快速排序](https://www.runoob.com/data-structures/2way-quick-sort.html#:~:text=%E5%8F%8C%E8%B7%AF%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95,%E5%8F%B3%E8%BE%B9%EF%BC%8Cv%20%E4%BB%A3%E8%A1%A8%E6%A0%87%E5%AE%9A%E5%80%BC%E3%80%82)