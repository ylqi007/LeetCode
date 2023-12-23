
## switch 语句
`if...else...`语句可以用来描述一个“二岔路口”，我们只能选择其中一条路来继续走，然而生活中经常会碰到“多岔路口”的情况。`switch`语句提供了 if语句的一个变通形式，可以从多个语句块中选择其中的一个执行。

```Java
switch(表达式) {
    case 值1:
        语句块1;
        break;
    case 值2:
        语句块2;
        break;
    ...
    case 值n:
        语句块n;
        break;
    default:
        语句块n+1;
    break;
}
```
**⚠️Note:**
1. 不要忘记`break` and `default`
2. `switch(A)`,括号中`A`的取值只能是整型或者可以转换为整型的数值类型，比如byte、short、int、char、还有枚举；需要强调的是：long和String类型是不能作用在switch语句上的。


* [Java switch case语句详解](https://c.biancheng.net/view/738.html)
* [java switch基础介绍及具体使用方法](https://www.w3cschool.cn/java/java-switch.html)
* [Java switch case 语句](https://www.runoob.com/java/java-switch-case.html)
* [What is Switch Case in Java and How to Use Switch Statement in Java](https://www.simplilearn.com/tutorials/java-tutorial/switch-case-in-java#:~:text=There%20are%20some%20things%20to,constant%20but%20not%20a%20variable.)
