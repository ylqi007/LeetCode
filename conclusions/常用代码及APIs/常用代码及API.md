[toc]

## Important Concepts
* [Subsequence Vs Substring](https://www.naukri.com/code360/library/subsequence-vs-substring)
* Stack, Monotonic Stack


## 常用Java API
### `java.lang.Character`
* https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Character.html
  * `static boolean isLetterOrDigit(char ch)   Determines if the specified character is a letter or digit.`
  * `static char toLowerCase(char ch)   Converts the character argument to lowercase using case mapping information from the UnicodeData file.`

### `java.lang.String`
* `java.lang.String`: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html
  * `public String substring(int beginIndex)`:  Returns a string that is a substring of this string. The substring begins with the character at the specified index and extends to the end of this string.
  * `public String substring(int beginIndex, int endIndex)`: Returns a string that is a substring of this string. The substring begins at the specified beginIndex and extends to the character at index endIndex - 1. Thus the length of the substring is endIndex-beginIndex.
* `java.lang.Integer`: https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Integer.html
  * `public static int parseInt(String s) throws NumberFormatException`

### `java.util.Arrays`
* https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Arrays.html
* `static int[] copyOfRange(int[] original, int from, int to) 	Copies the specified range of the specified array into a new array.`

### `java.lang.Math`
* https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Math.html
* `static double random() 	Returns a double value with a positive sign, greater than or equal to 0.0 and less than 1.0.`

### ArrayDeque
* Java11: https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/ArrayDeque.html
    > * Array deques have no capacity restrictions; they grow as necessary to support usage.
    > *  They are not thread-safe; in the absence of external synchronization, they do not support concurrent access by multiple threads
    > * Null elements are prohibited. 不能添加`null` object
    > * This class is likely to be faster than Stack when used as a stack, and faster than LinkedList when used as a queue.
  * Stack: push/pop/peek, 可以用`push
* ArrayDeque (Stack, Queue)
  * 🟩🌟二哥的Java进阶之路: [Java集合框架全面解析](https://javabetter.cn/collection/gailan.html)
  * [ArrayDeque介绍&&不推荐使用Stack类](https://blog.csdn.net/weixin_45713992/article/details/127574159)
  * [为什么JDK建议使用ArrayDeque而不是Stack和LinkedList实现栈和队列](https://www.cnblogs.com/jiading/articles/12452830.html)
  * [详解 Java 中的双端队列（ArrayDeque附源码分析）](https://javabetter.cn/collection/arraydeque.html)
  * [Java中的栈Stack、Deque、ArrayDeque、LinkedList](https://blog.csdn.net/linysuccess/article/details/109038453)

### `java.util.PriorityQueue<E>`
* https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/PriorityQueue.html
  * An unbounded priority queue based on a priority heap. The elements of the priority queue are ordered according to their natural ordering, or by a Comparator provided at queue construction time, depending on which constructor is used.
    * 基于queue，自然排序(即从小到大)
  * A priority queue does not permit null elements.
    * 不能存放null
  * `boolean add(E e) 	Inserts the specified element into this priority queue.`
  * `boolean remove(Object o) 	Removes a single instance of the specified element from this queue, if it is present.`
* `PriorityQueue`和`Queue`的区别在于，它的出队顺序与元素的优先级有关，对`PriorityQueue`调用`remove()`或`poll()`方法，返回的总是优先级最高的元素。
* [10 张手绘图详解Java 优先级队列PriorityQueue](https://javabetter.cn/collection/PriorityQueue.html)

**Reference:**
* [Difference Between == and equals() in Java](https://www.linkedin.com/pulse/difference-between-equals-java-babar-shahzad/)
* [String.equals versus == [duplicate]](https://stackoverflow.com/questions/767372/string-equals-versus)
* [How do I compare strings in Java?](https://stackoverflow.com/questions/513832/how-do-i-compare-strings-in-java)
* [java中的==和equals有什么区别](https://worktile.com/kb/p/37775#:~:text=java%E4%B8%AD%E7%9A%84%3D%3D%E5%92%8Cequals()%E6%9C%80%E5%A4%A7%E7%9A%84%E5%8C%BA%E5%88%AB,%E5%AD%98%E5%9C%A8%E4%BA%8EObject%E7%B1%BB%E4%B8%AD%E3%80%82)
* [Java 最常见的面试题：== 和 equals 的区别是什么](https://developer.aliyun.com/article/1169773)
* [Java语法----Java中equals和==的区别](https://www.cnblogs.com/qianguyihao/p/3929585.html)
* [== 和 equals 的区别是什么？](https://zhuanlan.zhihu.com/p/338350987)


## Important Classes In Java
在刷LeetCode的过程中，有一些class是常用的，但是不同的它们的method可能还有一些区别。因此，列出来，要重点掌握
* [java.lang.Character](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Character.html)
* [java.lang.String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)
* [Interface java.util.Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html)
* [Interface java.util.Comparator<T>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)
* [Interface java.lang.Comparable<T>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)
* [Interface java.util.Deque<E>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Deque.html) [念做dai ke]
* [Class java.util.Random](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Random.html)
* [Class java.util.Arrays](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Arrays.html)
* [java.util.ArrayDeque<E>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayDeque.html) [`implement Deque`]
* [java.util.LinkedList<E>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedList.html)  [`implement Deque`, 以后尽量用 `Deque<E> deque = new LinkedList<>()`]
* [java.util.PriorityQueue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/PriorityQueue.html)
* [java.util.stream.Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)
* [Summary of regular-expression constructs](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html#sum)

**Note:**
* Removed from JDK11: [Class javafx.util.Pair<K,V>](https://docs.oracle.com/javase%2F9%2Fdocs%2Fapi%2F%2F/javafx/util/Pair.html)
* [Removed from JDK 11, JavaFX 11 arrives as a standalone module](https://www.infoworld.com/article/3308400/removed-from-jdk-11-javafx-11-arrives-as-a-standalone-module.html)
* [Five Alternatives To Pair Class In Java](https://xperti.io/blogs/java-pair-class-alternatives/)


**Reference**
* https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html
* [Convert Stream to an array in Java](https://www.techiedelight.com/convert-stream-array-java/#2)
* [Convert Integer List to an int array in Java](https://www.techiedelight.com/convert-list-integer-array-int/)
* [How can I convert List<Integer> to int[] in Java? [duplicate]](https://stackoverflow.com/questions/960431/how-can-i-convert-listinteger-to-int-in-java)
* [How to convert an ArrayList containing Integers to primitive int array?](https://stackoverflow.com/questions/718554/how-to-convert-an-arraylist-containing-integers-to-primitive-int-array?noredirect=1&lq=1)


## 常见错误
### `error: no suitable method found for toArray(int[]::new)`
```java
List<Integer> res = new ArrayList<>();
res.toArray(int[]::new);

error: no suitable method found for toArray(int[]::new)
```
**Case 1: If you're using a Stream<Integer>:**
* If the stream contains Integer objects (autoboxed integers), you can use toArray(int[]::new) like this:
* ```java
  Stream<Integer> integerStream = Stream.of(1, 2, 3, 4, 5);
  int[] array = integerStream.mapToInt(Integer::intValue).toArray();
  ```

**Case 2: If you're using a Stream<int> (primitive int values):**
* For a stream of primitive int values, you don’t need the `int[]::new` reference at all because toArray() can handle primitive ints directly. Just do:
* ```java
  IntStream intStream = IntStream.of(1, 2, 3, 4, 5);
  int[] array = intStream.toArray();
  ```

**In summary:**
* Use `mapToInt(Integer::intValue)` if you're starting with a `Stream<Integer>`.
* Directly use `toArray()` for a `Stream<int>`.