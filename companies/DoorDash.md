## 技术电面 -- 面经
* [[面试经验] 刀大师 电面过经](https://www.1point3acres.com/bbs/thread-1103788-1-1.html)
* 

* [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
  * Binary Tree
  * 考虑访问每个节点时，应该返回什么。
  * [112. Path Sum](https://leetcode.com/problems/path-sum/)
    * 
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


## Onsite 面经
* [[面试经验] DD 昂赛 面经](https://www.1point3acres.com/bbs/thread-1099442-1-1.html)
* [[面试经验] Doordash EM phone screen](https://www.1point3acres.com/bbs/thread-1103790-1-1.html)




## 1. System Design
* System design： 问了design slack，说两个重要的点要实现，一是很快的可以load history，二是可以看到real time message
  * 第一个是cache，第二个是long pulling+db/cache store recent history吗？每个message有message ID，ID是用hash来计算

## 2. HM Chat: 问过往经历和一些behavior的问题
* HM：基础的BQ。具体问题忘了，但是比较standard，像tell me about a time you disagreed。
* 

## 3. Coding
* 编程1：基本就是貮毋伞。很快写完了。
* 编程2：散饵酒。会者不难，难者不会。
* [Doordash PhoneScreen](https://leetcode.com/discuss/interview-question/1265810/doordash-phonescreen)
* 

## 4. Incident Study