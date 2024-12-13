* [286. Walls and Gates](https://leetcode.com/problems/walls-and-gates/)
  * BFS: we initiate breadth-first search (BFS) from all gates at the same time. Since BFS guarantees that we search all rooms of distance d before searching rooms of distance d + 1, the distance to an empty room must be the shortest.
  * BFS, `Deque<int[]> queue = new ArrayDeque<>()`
* [859. Buddy Strings](https://leetcode.com/problems/buddy-strings/)
* [1790. Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/)
* ✅⭐[658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)
  * Binary Search
* [826. Most Profit Assigning Work](https://leetcode.com/problems/most-profit-assigning-work/)
  * Binary Search
  * 目标是找到 ability 范围内最大的 profit
* ✅⭐[1235. Maximum Profit in Job Scheduling](https://leetcode.com/problems/maximum-profit-in-job-scheduling/)
  * DP + Binary Search
* [2008. Maximum Earnings From Taxi](https://leetcode.com/problems/maximum-earnings-from-taxi/)
  * DP + Binary Search
  * 1235 和 2008 是一模一样的题目。
* [1347. Minimum Number of Steps to Make Two Strings Anagram](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/)
  * Count, String manipulation
* [1664. Ways to Make a Fair Array](https://leetcode.com/problems/ways-to-make-a-fair-array/)
  * DP
  * 删除 nums[i] 之后，index i 之后的 oddSum 就变成 evenSum，evenSum 就变成了 oddSum