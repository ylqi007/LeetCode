# Map

Java 的集合类主要由两个接口派生而出：`Collection` 和 `Map`，`Collection` 和 `Map`是 Java 集合框架的根接口，这两个接口又包含了一些接口或实现类。

本节主要分析`Map`。`Map`是一个映射接口，其中的每个元素都是一个`key-value`键值对，抽象类`AbstractMap`通过适配器模式实现了Map接口中的大部分函数。

## HashMap
* `HashMap`根据键的`hashCode`值存储数据，大多数情况下可以直接定位到它的值，因而具有很快的访问速度，但**遍历顺序却是不确定的**。 
* `HashMap`最多只允许一条记录的键为null，允许多条记录的值为null。
* `HashMap`是**非线程安全**的，即任一时刻可以有多个线程同时写HashMap，可能会导致数据的不一致。如果需要满足线程安全，可以用`Collections`的`synchronizedMap`方法使`HashMap`具有线程安全的能力，或者使用`ConcurrentHashMap`。


## LinkedHashMap
* `LinkedHashMap`直接继承自`HashMap`，所以`LinkedHashMap`拥有`HashMap`的大部分特性，最多只允许一个key为null，可以有多个value为null。
* 一些主要的方法和属性也直接继承自`HashMap`，并对其中某些方法进行了重写。
* `LinkedHashMap`与`HashMap`最大的不同在于`LinkedHashMap`保持了元素的有序性，即遍历`LinkedHashMap`的时候，得到的元素的顺序与添加元素的顺序是相同的，可以按照**插入顺序** (insertion-order)或**访问顺序** (access-order)来对哈希表中的元素进行遍历。

* [java.util.LinkedHashMap<K,V>](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/LinkedHashMap.html)
  * Type Parameters:
    * K - the type of keys maintained by this map
    * V - the type of mapped values
  * Default `accessOrder = false;`，即默认顺序为**插入顺序**



## TreeMap


## LeetCode
- [ ] [146. LRU Cache](https://leetcode.com/problems/lru-cache/) (LinkedHashMap)

## Reference
* [Java集合框架之HashMap详解](https://yanglukuan.github.io/2017/08/31/java/HashMap%E8%AF%A6%E8%A7%A3/)
* [Java集合框架之LinkedHashMap详解](https://yanglukuan.github.io/2017/09/05/java/Java%E9%9B%86%E5%90%88%E6%A1%86%E6%9E%B6%E4%B9%8BLinkedHashMap%E8%AF%A6%E8%A7%A3/)
* [源于 LinkedHashMap源码](https://leetcode.cn/problems/lru-cache/solutions/1/yuan-yu-linkedhashmapyuan-ma-by-jeromememory/)