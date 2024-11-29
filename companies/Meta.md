

## Quick Select
Quick Select 可以选择前 k 个元素，但是并不能保证这前 k 个元素是有序的。

适用情况：对于一个无序数组，
* 求第 k 大、小的元素
* 求前 k 大、小的元素集合
* 求满足某种条件的前 k 或者第 k 个元素

- [ ] [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) [QuickSelect]
- [ ] [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) [QuickSelect, Bucket Sort]
- [ ] [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) [QuickSelect, Bucket Sort]








## Reference
* [[面试经验] 元 intern vo 神奇的挂经](https://www.1point3acres.com/bbs/thread-1099103-1-1.html)
  * 题: 叁死骑, 吾寺散, 347, 543
  * 3开头那道题目问如果 1<k <<N(nums长度), 就是需要的k比N要少很多很多该怎么办, 我最早觉得用heap 这样space会很低 所以先写了heap,沟通follow up后感觉面试官希望用bucket sort那个方法 time ON, 于是两种方法都写了, 也dry run了
    * 她可能想要的是quick select + bucket sort，我完全没听说过quick select,所以写了heap + bucket
  * 5开头写完之后,follow up问如果要算diameter的同时还要记录valid path 怎么办, time complexity 是多少, 只需要我说time,也说了也还是ON, 还把psedo code 的if 判断也大概写了 + dryrun
* [[面试经验] meta 全套挂经](https://www.1point3acres.com/bbs/thread-1099010-1-1.html)
  * - Phone screen
      - 耳洞起, 207
      - 闪耀时, 314
  * - onsite
    - coding 1.a 要粮食酒 optimize performance again, 1249
    - coding 1.b 就删别, 983
    - coding 2.a 尔山流, how to solve using iteration, 236
    - coding 2.b merge 3 sorted arrays, optimize like better readability
  * - bq
      - most proud
      - any conflict
      - hot decision
      - growth area: future, what has grown
      - ambiguity
  * - system design
      - 输入是当前位置，返回数据库里离当前位置最近的k个landmark
* [[面试经验] 买它 电面挂经 求大米](https://www.1point3acres.com/bbs/thread-1098986-1-1.html)
  * 1）幺迩夭，follow up 指定交易次数, 121
  * 2) 夭幺灸漆 变种，多了obstacles list, 1197
  * 幺疤疤 zszs, 188
* [[面试经验] meta 2025 sde intern vo](https://www.1point3acres.com/bbs/thread-1098933-1-1.html)
  * 两道tag
    * 妖〇久妖, 1091
    * 叁幺肆, 314
* [[面试经验] Meta intern奇怪vo](https://www.1point3acres.com/bbs/thread-1098725-1-1.html)
  * dry run test?
* [[面试经验] meta SWE NG 新鲜 vo 面经](https://www.1point3acres.com/bbs/thread-1098720-1-1.html)
  * Q1 非常easy 有手就行 不说了
  * Q2 肆鲮魃, 408?
  * Q1 鸸庑霰, 253
    * 是的，我用的heap
  * Q2 鲕迩祁 space O(1)的解法不是很熟练，写得很狼狈，勉强完成 简单过了一个case, 227
* [[面试经验] META 25NG SWE VO 基本挂经](https://www.1point3acres.com/bbs/thread-1098667-1-1.html)
  * VO1:
    * 一道2D Array的Find Min的二分。最开始Code有点紧张，忘记处理边界判断了，dry run的时候自己改正了。后续Test大概说明了一下为什么一定有解，面试官姐姐貌似比较满意，说是意识到这个情况能让test更容易。
    * 玖弎泗，DFS BFS结合题，虽然刷到了，但是代码量对我来说还是有点大，刚好写完，简单得Test了一下就到时间了。感觉可能藏了Bug没检查出来。934
  * VO2:
    * (1249)最高频噫尔泗玖，写完后Follow up了一下Java StringBuilder的实现对我算法的影响，楞了下意识到是在提醒我最坏情况动态数组收缩的edge case没考虑到，最后口述了一下优化方案。刷leetcode的时候大意了，以为beat 98%之后就最优了...
    * (938) 玖弎芭变形，先快速说完了原题思路,然后直接上follow up: 假设对于同一个BST，有无数多个range query，怎么优化query效率。首先就想到了BST的inorder遍历构建有序序列，然后用二分找边界。后续开始写那个类，写的时候发现还需要用到前缀和优化。。反正边写边改，最后还是写完了，简单run了一下讨论了一下复杂度就刚好结束。（面试官最开始还掉线了几分钟）
  * 两轮基本上都是卡死40分钟，后续五分钟都在闲聊。感觉面试官态度还挺好，就是感觉题不简单...
* [[面试经验] 买它 热乎 screening](https://www.1point3acres.com/bbs/thread-1098634-1-1.html)
  * 啾伞芭 我给了深搜O(n)
    * 佛罗啊噗如何优化time(懵住要了hint)
  * 嗣伶耙
* [[面试经验] 买它新鲜挂经](https://www.1point3acres.com/bbs/thread-1098578-1-1.html)
  * 药酒 (19), 还有一题忘了（也是Medium）
  * coding 1:
    find 2nd largest number from a permutation
    [1,2,3,4,5] -> [5,4,3,1,2]
  * 散气霸 (378)
  * System Design:
    * design leetcode contest
    * coding 2:
      merge 3 sorted list with duplicates.
  * system 2:
    Design game ranking board (output global ranking list and friends' ranking list)
    bq:
      most proud of
      lead others
      need improvement
      reject others
* [[面试经验] 买它 电面 挂经](https://www.1point3acres.com/bbs/thread-1098525-1-1.html)
  * 第一题是 久尔衣， 第二题是 散散久，非常高频的题目了。921, 339
  * 第二题需要自己写全数据结构，不像leetcode那样是现成的，写的时候懵了好一会儿。
* ✅ [[面试经验] 买它电面](https://www.1point3acres.com/bbs/thread-1098518-1-1.html)
  * 姚唔起灵, 1570
  * 幺玖泠, 190?
* [[面试经验] 买它面筋+面试迟到能加面吗😭](https://www.1point3acres.com/bbs/thread-1098506-1-1.html)
  * 力扣 要久久 妖灵九妖 斯妖舞, 199, 1091, 415
* ✅[[面试经验] 买它VO+经验总结](https://www.1point3acres.com/bbs/thread-1098493-1-1.html)
  * 第一天: [[面试经验] 买它VO](https://www.1point3acres.com/bbs/thread-1096455-1-1.html)
    * 第一题是鎏霰硫换了一下input，把function的数字用string代替了, 636?
  * 霸拔，鳍镏，两题都有follow up，会问edge case，第一题问了为什么从后往前等等，第二题忘记了，但是基本上都是为了看你是不是真的懂了而不是背答案。
    * 88
    * 76?
* [[面试经验] 买它 VO 牛嘎达](https://www.1point3acres.com/bbs/thread-1098492-1-1.html)
  * 代码轮1： 中国小姐姐超级nice，中间我脑子突然卡壳了，耐心提醒我最终完成了code但是没时间dry run，希望不会扣太多分
    * 舞瘤羚，变形，如果有return true，没有return false。佛罗啊普，如果有复数怎么办, 560
    * 伞私企, 变形，只要给定频率的所有元素, 347
  * 代码轮2：印度帅小伙，人也很nice
    find the maximum sum of any two elements that are not adjacent.
    叄嗣捌，佛罗啊普，让make code cleaner, 348
* [[面试经验] Meta挂](https://www.1point3acres.com/bbs/thread-1098474-1-1.html)
  * 317. Shortest Distance from All Buildings ？
  * 合并intervals, 不能用sort
* [[面试经验] 买它店面 新鲜挂经](https://www.1point3acres.com/bbs/thread-1098439-1-1.html)
  * 给定一个排序的整数数组，找到和最接近 K 的一对数。
  * 蠡口 幺漆伞, 173
* [[面试经验] 买它昂塞](https://www.1point3acres.com/bbs/thread-1098384-1-1.html)
  * 二叉树每个节点连接邻居节点
  * 基本计算器
  * 简单哈希表 找两个数对 x1 y1, x2 y2, x1+x2 = y1+y2, find matching pairs
  * 滑动窗口内的最大值, 239 Sliding Window Maximum 是hard问题，抽到有点倒霉哈哈，不过其他几题都是高频不算很为难的了
* [[面试经验] Meta Research Scientist Machine Learning面经](https://www.1point3acres.com/bbs/thread-1098164-1-1.html)
  * 第一轮coding，一道valid parentheses，一道lowest common ancester，45分钟给出最优解
  * 第二轮vo，一共四个section分两次面完，前两个section全部coding，都是tag题，一道嗣霸旧，其他不太记得了，有印象的是一道用union find解的题目，一道divide and conquer，目测有一到两个hard，面试官很nice会给提示，感觉对coding style有要求
  * 感谢面经救命，建议有时间过完面经，没时间也至少刷完blind 75: https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions
* [ [面试经验] Meta 店面](https://www.1point3acres.com/bbs/thread-1098079-1-1.html)
  * 遗留物灵, 1650
  * 伞斯刘, 346
* [[面试经验] Meta Production System Engineer](https://www.1point3acres.com/bbs/thread-1098016-1-1.html)
  * 括号题变形
* [[面试经验] Meta sde ng 面经](https://www.1point3acres.com/bbs/thread-1097947-1-1.html)
  * 第一轮： 棂鲅，抑鸠鸠 变形, 08, 199?
    第二轮 ：抑迩嗣韭，坞咝霰 变形, 1294, 543?
* [[面试经验] meta vo bit manipulation](https://www.1point3acres.com/bbs/thread-1097945-1-1.html)
  * ?
* ✅ [[面试经验] Meta 11月Coding, SD, BQ总结 （更新中）](https://www.1point3acres.com/bbs/thread-1097935-1-1.html)
* [[面试经验] Meta NG VO](https://www.1point3acres.com/bbs/thread-1097863-1-1.html)
  * Coding 1: 榴扒凌 妖榴贰 （变成找local minimum), 680, 162
  * Coding 2: 伍肆叁 幺儿肆玖, 534, 1249
  * meta基本都是高频tag题，都刷了就问题不大。写完后口头跑test case时间很短，只用几分钟
* [[面试经验] meta 25ng 挂经](https://www.1point3acres.com/bbs/thread-1097847-1-1.html)
  *  憇䧱刈 用了map, 791?
  * 🈚️囸沕 简单版 只要左右看 从上绕
  * 1. 🌰口: 憇䧱刈 用了map
  * 2.🈚️囸沕 简单版 只要左右看 从上绕
  * 3.㒃鰩沕 给了题解的后两种解法 写出来以后面试官想让我继续优化 就说了大小堆分情况用(感觉没有达到他心中想要的)
  * 4.鋈翏䉹
  * bq忘了但都是常规问题
  * 560, 791, 125, 545
* [[面试经验] Meta 25NG 挂经](https://www.1point3acres.com/bbs/thread-1097789-1-1.html)
  * coding 1
    利口 幺尔就 秒, 129
    利口 武尔就 (529)（简化版，要求先initialize board然后random埋雷，followup要求在没有雷的grid计算出8个方向有多少雷）这轮表现一般 因为没见过这题 也一直在和面试官保持communication 最后超时了10分钟写完了 结束后发现漏了一个if checking...（如果pos有雷就不再计算）不知道是不是这一轮red flag了
  * coding 2
    利口 近似尔尔漆 (224) （只需要加乘）秒
    利口 幺令就幺 (1091) 变种 要求print所有能到的path，dfs
* ✅[[面试经验] 买它 全套](https://www.1point3acres.com/bbs/thread-1097783-1-1.html)
  * 全部4轮Coding:
    窈浏武陵
    窈灵祀契
    琉霸陵
    霰耳玖
    鳍鳐
    咝棂鲅
    韭芜岜
    灞钯
  * SD: Leetcode coding contest platform
  * BQ: 都是常规的题目，conflict, challenges, etc.
* [[面试经验] 买它vo 3轮coding](https://www.1point3acres.com/bbs/thread-1097782-1-1.html)
* [[面试经验] Meta 吐血整理近几个月所有coding 题目 刷完就过！PDF版 顺序整理好了。](https://www.1point3acres.com/bbs/thread-1097728-1-1.html)
* [[面试经验] meta intern vo](https://www.1point3acres.com/bbs/thread-1097709-1-1.html)
  *  LC 163
* [[面试经验] PHD NG Meta店面挂经【求米】](https://www.1point3acres.com/bbs/thread-1097700-1-1.html)
  * 第一题：霰耀似。这题太常见了 我两年前面intern的时候就出的这道题。。但当时有点小紧张，我说dfs？然后他说为什么dfs，我缓过神来说不对应该是bfs，然后开始写。就用的defaultdict()方法，最后用一下sort就写完了。然后他问我复杂度，我又卡了一下说N，后来想起来应该是nlogn因为用了sort。然后他：就说不排序怎么做，follow up了一下。
  * 第二题：尔尔漆简化版。只有加法乘法。直接用stack一遍过了。
  * 霰耀似bfs dfs都可以做，但是bfs有个可以不sort的解法
  * 尔尔漆有不用stack的解法但是用stack比较易懂
  * meta 面试都有培训 有详细的视频和文档 你显然没怎么仔细看 他们要求的很明确 要跟面试官沟通好思路 让你开始写再开始写
* [ [面试经验] Meta 25NG Timeline](https://www.1point3acres.com/bbs/thread-1097666-1-1.html)
  * coding 都是tag题，medium-hard
    利口 尔霰，变种，不给用linked list
    利口 霸（简化版，没有那么多edge cases）
    利口 近似尔尔漆
    面试官follow up问了很多complexity的分析和trade off，但都非常supportive。建议面试的时候一定要多communication！
  * 利口 尔霰，变种，不给用linked list, 请问这题的意思是input是array不是linked list吗？
  * 




1. [207. Course Schedule](https://leetcode.com/problems/course-schedule/)
2. [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
3. [1331. Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/description/)
4. [953. Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/description/)
5. [1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/)
6. [1424. Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/description/)
7. [2060. Check if an Original String Exists Given Two Encoded Strings](https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/description/)
8. [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/)
9. ✅ [269. Alien Dictionary](https://leetcode.com/problems/alien-dictionary/)