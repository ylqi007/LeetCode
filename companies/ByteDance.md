# ByteDance

## Coding
> 两轮coding都是lc medium（是代码比较好写的那种medium，多练经典题就可以），没有要求一遍ac，写完自己对着test case能修好就行，面试官也会帮着一起看。coding结束向面试官提问也聊得很开心。
> 
>


### LeetCode
- [x] [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [x] [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- [x] [539. Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/description/)
- [x] [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)
- [x] [924. Minimize Malware Spread](https://leetcode.com/problems/minimize-malware-spread/)
- [x] [694. Number of Distinct Islands](https://leetcode.com/problems/number-of-distinct-islands/)
- [x] [3043. Find the Length of the Longest Common Prefix](https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/)
  - [x] [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
- [x] 🟨🌟[1530. Number of Good Leaf Nodes Pairs](https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/)
- [x] [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
- [x] [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)
- [ ] [468. Validate IP Address](https://leetcode.com/problems/validate-ip-address/description/)
  - 🔴String的长度判断很重要。比如empty string `str = ""`, `str.charAt(0)` 会报错
- [x] [252. Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)
- [x] [253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [x] [1094. Car Pooling](https://leetcode.com/problems/car-pooling/)
- [x] [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [x] [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
  - [x] [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)
- [x] 🌟[146. LRU Cache](https://leetcode.com/problems/lru-cache/)
- [x] 🌟[460. LFU Cache](https://leetcode.com/problems/lfu-cache/)
- [x] [278. First Bad Version](https://leetcode.com/problems/first-bad-version/) [Binary Search]
  - [ ] [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [ ] 🟥🌟[787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/)
- [x] [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) [BFS]
- [ ] 🟥[84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
  - [ ] [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)
- [ ] 🟥🌟Basic Calculator
  - [ ] [224. Basic Calculator](https://leetcode.com/problems/basic-calculator/) [`+-()`]
  - [ ] [227. Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii/) [`+-*/`]
  - [ ] [772. Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii/) [`+-*/()`]


- [ ] [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)
- [ ] 2 Sum, 3 Sum
- [ ] [442. Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)
- [ ] [140. Word Break II](https://leetcode.com/problems/word-break-ii/)




tt第二轮 一道js的  closure的题
第二题是用俩个stack做一个queue



~~LeetCode 3~~
~~LeetCode 128~~
~~雾散酒, 539~~
~~厮药Ⅶ, 417~~
现在您有10个桶，其中9个桶的球都是10克的正品，而1个桶的球是次品，次品的球重量是未知的整数，可能是1到9克中的某个值，而且次品桶内的所有球质量是相同的。问题要求设计一种最少次数称重的方法来找出装有次品球的桶。最少次数？
~~酒兒寺, 924~~
~~榴旧丝, 694~~
~~散铃寺伞, 3043~~, 14
2421
~~衣舞弎灵, 1530~~
~~义乌三菱, 1530~~
~~利口1妖舞酒, 1159~~
~~餌妖玲, 210~~
~~而要领, 210~~
~~蠡口二幺凌, 210~~
~~丝留吧, 468~~
~~李叩56, 56, "物流, 56~~
~~耳午餐, 253?~~
~~妖妖斯伞, 1143~~
~~刷题王耀灵酒丝,1094~~
leetcode 2850
~~耀司流, 146~~
~~LFU, 460~~
~~LRU, 146~~
🟥利蔻琦霸戚(Bellman-Ford), 787
Given an array of integers and a target number, find the indices of all pairs of numbers in the array that sum up to the target, and output these pairs of indices
~~278加强版, 278~~
~~Rotting Oranges, 994~~
第一轮题目就是给了一个长字符串，然后一个listof字符串。这个list的字符串里的每一个比如 abc, 如果在长字符串里找到他的变形，就输出。变形就是abc, bac,cab...这样
~~巴斯, 84~~ [以及相似的85]
DAG 找最短路径?
收银"?
Candy problem?

十六进制转换为八进制
琪琪尔, 772. Basic Calculator III
斯物流, 456,
"1642, 1642
68", 68


第一题类似于一个最小生成树
第二题是有三个排好序的array,找第k大的数，要求logn



"给定一个二维数组，每个单元格的值表示它拥有多少奶酪，每次可以移动一块奶酪，问将奶酪传播到每个单元格所需的最少步骤数。
例如，对于数组 [[1 1 0] [1 1 1] [1 2 1]]，输出将是 3
[[1 0 0] [1 0 0] [ 1 3 3]], 输出将是 4"


## System Design

## BQ



## Reference
* ❇️ [[面试经验] tiktok 最近题目汇总 求加米 加米不扣米](https://www.1point3acres.com/bbs/thread-1088921-1-1.html)
* [[面试经验] TT e-commerce 第二轮店面](https://www.1point3acres.com/bbs/thread-1094079-1-1.html)
* [[面试经验] Tiktok 第二轮 VO 悲剧](https://www.1point3acres.com/bbs/thread-1092186-1-1.html) [第一轮问题很深，7-8年经验]
* [[面试经验] TT e-commerce店面](https://www.1point3acres.com/bbs/thread-1091065-1-1.html) [2-1]
  * 2 Sum
  * 3 Sum
    * 首先把所有数字放入HashMap, 其次Two Level Nested For Loop来选取两个不同的位置的数字，求和之后看看HashMap里面有没有对应的negated数字。记住这两个当下选取的数字，需要暂时从HashMap里面删掉，之后再加回来。
* [[面试经验] Titok电面](https://www.1point3acres.com/bbs/thread-1090931-1-1.html), E-commerce
  * LC 140, 易思玲
* [[面试经验] Titok电面](https://www.1point3acres.com/bbs/thread-1089760-1-1.html)
  * LC 253
* [[面试经验] 温哥华TT第二轮电面](https://www.1point3acres.com/bbs/thread-1088507-1-1.html)
* [[面试经验] TikTok Backend 电面](https://www.1point3acres.com/bbs/thread-1088062-1-1.html)
  * 200, 694
* [[面试经验] tt vo 1面拒](https://www.1point3acres.com/bbs/thread-1087473-1-1.html)
  * 224, 227, 基本计算器
* [[面试经验] tt 电面](https://www.1point3acres.com/bbs/thread-1086099-1-1.html)
  * sd 红包系统，只要求 抢的人很多需要保证服务流程，同时金额恒定不能抢多了
* [[面试经验] TikTok Phone](https://www.1point3acres.com/bbs/thread-1085960-1-1.html)
* [[面试经验] 抖音电商 面试题](https://www.1point3acres.com/bbs/thread-1083924-1-1.html)
  * 现在您有10个桶，其中9个桶的球都是10克的正品，而1个桶的球是次品，次品的球重量是未知的整数，可能是1到9克中的某个值，而且次品桶内的所有球质量是相同的。问题要求设计一种最少次数称重的方法来找出装有次品球的桶。最少次数？
* [[面试经验] TikTok 一轮游](https://www.1point3acres.com/bbs/thread-1083209-1-1.html)
  * LC 207
* [[面试经验] tt backend 一轮](https://www.1point3acres.com/bbs/thread-1083192-1-1.html)
  * 算法考了一道二叉树找符合要求的所有路径，不熟悉平台没有debug出。没准备好估计一轮游。
* ❇️[[面试经验] TikTok 挂经](https://www.1point3acres.com/bbs/thread-1083100-1-1.html)
  * LC 1530
* ❇️[[面试经验] tiktok MLE 最新店面 求米 > <](https://www.1point3acres.com/bbs/thread-1082927-1-1.html)
  * 一开始先问了离口斯就灵，手写一个LFU cache. 应该是460？
    * LFU用DLL写代码量太大 用LinkedHashSet容易些
  * merge two BST into sorted list 还不让开额外空间
    那是要用morris 遍历来做吗  ....
* [[面试经验] TT 吐槽一轮游](https://www.1point3acres.com/bbs/thread-1081981-1-1.html)
  * 第一题， 舅儿已
  * 第二题，伞令已
* 🟥 [[面试经验] 字节24后端一年经验新鲜面经 新人求大米](https://www.1point3acres.com/bbs/thread-1081884-1-1.html)
* [[面试经验] 字节大概率挂经](https://www.1point3acres.com/bbs/thread-1081403-1-1.html)
  * 利口 斯物流
* [[面试经验] 字节电面面经](https://www.1point3acres.com/bbs/thread-1080884-1-1.html)
  * 酒兒寺, 924
  * 榴旧丝, 694
    散铃寺伞, 3043
* [[面试经验] TT 三轮挂经](https://www.1point3acres.com/bbs/thread-1080076-1-1.html)
  * course scheduler
  * SD题目，job scheduler
  * 10W QPS
* [[面试经验] TT 店面](https://www.1point3acres.com/bbs/thread-1080056-1-1.html)
  * 妖妖斯伞
* ❇️[[面试经验] 题课逃课面筋](https://www.1point3acres.com/bbs/thread-1078737-1-1.html)
  * leetcode 2850
* [[面试经验] tt一轮挂经](https://www.1point3acres.com/bbs/thread-1078309-1-1.html)
  * 李叩56
* [[面试经验] tt字节店面](https://www.1point3acres.com/bbs/thread-1078257-1-1.html)
* [[面试经验] tt 一轮挂经](https://www.1point3acres.com/bbs/thread-1078014-1-1.html)
  * 耀司流, 146
  * 设计：给个机器（带硬盘），设计一个key value storage
  * 问过往项目经历
* ❇️ [[面试经验] tt 店面](https://www.1point3acres.com/bbs/thread-1077766-1-1.html)
  * 利蔻琦霸戚, 787
* [[面试经验] tt 7月面经 估计挂了](https://www.1point3acres.com/bbs/thread-1077719-1-1.html)
  * 1道js的题，1道用俩个stack做queue.
* [[面试经验] 字节 三轮 VO](https://www.1point3acres.com/bbs/thread-1074473-1-1.html)
  * 物流和 巴斯, 56和84？
  * 第二轮 DAG 找最短路径
  * 第三轮 收银
* [[面试经验] Bytedance 第一轮面经](https://www.1point3acres.com/bbs/thread-1074202-1-1.html)
  *  lc medium binary search
* ❇️ [[面试经验] 字节面经 经典题目深挖](https://www.1point3acres.com/bbs/thread-1074169-1-1.html)