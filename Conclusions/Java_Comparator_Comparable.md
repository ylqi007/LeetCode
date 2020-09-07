
* Example 1 from [Ref 1](https://blog.csdn.net/yongh701/article/details/44131051)
```java
import java.util.*;
//以下是学生类Student定义，有点类似C语言的结构体啊！^_^
class Student {
	public int s_no;
	public String s_name;
	public int s_class;
}
 
public class compareTest {
	public static void main(String[] args) {
		//存放学生类的动态数组的初始化
		ArrayList<Student> studentArr = new ArrayList<Student>();
		Student s1 = new Student();
		s1.s_no = 3;
		s1.s_name = "a";
		s1.s_class = 102;
		studentArr.add(s1);
		Student s2 = new Student();
		s2.s_no = 2;
		s2.s_name = "b";
		s2.s_class = 101;
		studentArr.add(s2);
		Student s3 = new Student();
		s3.s_no = 1;
		s3.s_name = "c";
		s3.s_class = 103;
		studentArr.add(s3);
		//初始化之后先打印以下这个动态数组
		System.out.println("排序前：");
		for (int i = 0; i < studentArr.size(); i++) {
			System.out
					.println("我是" + studentArr.get(i).s_class + "班的"
							+ studentArr.get(i).s_name + "学号是"
							+ studentArr.get(i).s_no);
		}
		//对于Comparator接口的重写
		//这个接口就一个抽象函数，给出的参数与返回值都是定死的。
		Collections.sort(studentArr, new Comparator<Object>() {
			public int compare(Object o1, Object o2) {
				//你首先设置你要比较的东西
				//具体是把参数中的Object强制转换成你要比较的东西，这里是两个Student类
				//这里的s1,s2与上面的s1,s2一点关系都没有，只是抽象的前者与后者的关系
				Student s1 = (Student) o1;
				Student s2 = (Student) o2;
				//如果前者的学号大于后者的学号，就是前者大于后者，返回1系统就会识别是前者大于后者
				if (s1.s_no > s2.s_no) {
					return 1;
				}
				//小于同理
				if (s1.s_no < s2.s_no) {
					return -1;
				}
				//如果返回0则认为前者与后者相等
				return 0;
			}
		});
		//比较完毕再输出以学号排序之后的结果
		System.out.println("按学号排序后：");
		for (int i = 0; i < studentArr.size(); i++) {
			System.out
					.println("我是" + studentArr.get(i).s_class + "班的"
							+ studentArr.get(i).s_name + "学号是"
							+ studentArr.get(i).s_no);
		}
		//以下是以班级排序的过程
		Collections.sort(studentArr, new Comparator<Object>() {
			public int compare(Object o1, Object o2) {
				Student s1 = (Student) o1;
				Student s2 = (Student) o2;
				if (s1.s_class > s2.s_class) {
					return 1;
				}
				if (s1.s_class < s2.s_class) {
					return -1;
				}
				return 0;
			}
		});
		System.out.println("按班级排序后：");
		for (int i = 0; i < studentArr.size(); i++) {
			System.out
					.println("我是" + studentArr.get(i).s_class + "班的"
							+ studentArr.get(i).s_name + "学号是"
							+ studentArr.get(i).s_no);
		}
	}
}
```

* Exampel 2 from [Ref 2](https://blog.csdn.net/zhangjq520/article/details/54313269?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)
```java
Collections.sort(books, new Comparator<Book>() {
    @Override
    public int compare(Book o1, Book o2) {
        // o1 和 o2 反过来决定升序和降序
        return o1.getId().compareTo(o2.getId());升序
        // return o2.getId().compareTo(o1.getId());降序
        // return o1.getName().compareTo(o2.getName());
        // return o2.getName().compareTo(o1.getName());
        // return o1.getTime().compareTo(o2.getTime());
        // return o2.getTime().compareTo(o1.getTime());
    }
    
});
```

### `Comparable` v.s. `Comparator`
1. `Comparable` interface: 如果想用 `java.util.Arrays.sort()` 对数组进行排序，则对象所在的 class 必须实现 `Comparable` interface，用于指定排序接口；
若一个类实现了Comparable接口，就意味着“该类支持排序”。
    * `Comparable` 接口定义如下：
```java
public  interface  Comparable<T>{
   public int compareTo(T  o);    
}
```

    * `Comparable` 接口用法：
```java
class Student implements Comparable<Student> {
    private String name;
    private int age;
    private float score;
    
    @Override
    public int compareTo(Student stu) {  //覆写compareTo方法实现排序规则的应用
        if(this.score>stu.score){
            return -1;
        }else if(this.score<stu.score){
            return 1;
        }else{
            if(this.age>stu.age){
                return 1;
            }else if(this.age<stu.age){
                return -1;
            }else{
                return 0;
            }
        }
    }
}
```

2. `Comparator`
如果一个类已经开放完成，但是在此类建立的初期并没有实现Comparable接口，此时肯定是无法进行对象排序操作的，所以为了解决这一的问题，java又定义了另一个比较器的操作接口 Comparator 此接口定义在java.util包中，接口定义如下：
```java
public  interface  Comparator<T>{
    public  int  compare(T o1, T o2);

    boolean  equals(Object  obj);

}
```

### 比较器
那么正确的排序器写法是什么样的呢？ 如果不考虑装箱的性能问题，那么最靠谱的方式如下：
```java
class SmsComparator implements Comparator<SmsItem> {
    @Override
    public int compare(SmsItem lhs, SmsItem rhs) {
        Long rDate = rhs.mDate;
        Long lDate = lhs.mDate;
        return rDate.compareTo(lDate);
    }
}
```

不过这样依然多此一举了，JDK已经考虑到了这一点，Long类型有一个静态方法，compareTo，直接使用即可；最简单又最靠谱的方式如下：
```java
public static int compare(long lhs, long rhs) {
    return Long.compareTo(rhs.mDate, lhs.mDate);
}
```

### Comparator 和 Comparable 比较
* Comparable是排序接口；若一个类实现了Comparable接口，就意味着“该类支持排序”。
* 而Comparator是比较器；我们若需要控制某个类的次序，可以建立一个“该类的比较器”来进行排序。

我们不难发现：Comparable相当于“内部比较器”，而Comparator相当于“外部比较器”。

## Reference:
1. [【Java】Collections中sort方法Comparator的重写](https://blog.csdn.net/yongh701/article/details/44131051)
2. [java list集合使用Collections中的sort方法进行排序（Comparator），超实用](https://blog.csdn.net/zhangjq520/article/details/54313269?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)
3. [【java】Comparator的用法](https://blog.csdn.net/u012250875/article/details/55126531)
    * Sort
    * Group
4. [java学习笔记13--比较器(Comparable、Comparator)](https://blog.csdn.net/itmyhome/article/details/8952722)
    * `Comparable` interface: 
    * `Comparator`
5. [浅谈 java 自定义排序之 Comparator](https://my.oschina.net/amstrong/blog/753990)
6. [你会写比较器么？](https://zhuanlan.zhihu.com/p/20637498)
7. [Java 排序](http://jverson.com/thinking-in-java/tools/comparator-sort.html)
8. [Java 中 Comparable 和 Comparator 比较](https://www.cnblogs.com/skywang12345/p/3324788.html)
9. [ Comparable和Comparator对比 ](https://blog.yangx.site/2018/03/09/java-array-sort/)
