## 1. Brute Force


## 2. KMP(Knuth-Morris-Pratt) 算法


## 3. BM(Boyer-Moore) 算法
BM 算法**从右向左**扫描模式字符串(pattern)，并将它和文本字符串(text)比较。BM 算法的效率比 KMP 算法高很多，常用于文本编辑器中的搜索匹配功能。
* 坏字符: 所谓坏字符，就是模式串与文本串在从右往左的匹配过程中，出现的第1个不匹配的文本字符。
* 好后缀: 所谓好后缀，就是模式串与文本串在从右往左的匹配过程中，出现的部分匹配的文本字符串后缀

综上所述，在匹配过程中，如果当前字符匹配失败，则：
`模式字符串右移位数 = Max { shift(坏字符) , shift(好后缀) }`


## 4. Rabin-Karp 算法

 

## Reference:
1. [面试算法之字符串匹配算法，Rabin-Karp算法详解](https://blog.csdn.net/tyler_download/article/details/52457108)
2. [Rabin-Karp算法：字符串匹配问题](https://blog.csdn.net/lucylove3943/article/details/83491416?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.nonecase)
3. [子字符串查找（1）](https://www.jianshu.com/p/9828bf488a39)
4. [子字符串查找（2）——KMP算法](https://www.jianshu.com/p/fe107b4e4271)
5. [子字符串查找（3）——BM算法](https://www.jianshu.com/p/c9300c34adbb)
6. [子字符串查找（4）——Rabin-Karp算法](https://www.jianshu.com/p/24895aca0459)




