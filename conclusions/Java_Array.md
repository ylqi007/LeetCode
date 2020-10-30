# 关于 Java Array 常见问题的一些说明和总结

* 内存一旦分配就不能改变，所以说数组(array)的长度是固定

---
## Java数组应用十大技巧攻略
### 0. Declare an array ()
```java 
String[] aArray = new String[5];
String[] bArray = {"a", "b", "c", "d", "e"};
String[] cArray = new String[]{"a", "b", "c", "d", "e"}; 
```

创建数组的三种方式：静态和动态
```java
public static void main(String[] args) {
	// 1.方式一：声明、分配空间并赋值。在声明的时候就已经分配空间，并赋值。
	int[] arr1 = {1,2,3};

	// 2.方式二：显示初始化
	int[] arr2;
	arr2 = new int[]{1,2,3}; 

	// 3.方式三 显示初始化()
	int[] arr3;
	arr3 = new int[3];
}
```
* 方法一：在声明的时候就已经分配空间，并赋值。
* 方法二、三：声明和内存分配是分开的，i.e. `int[] arr2;` and `int[] arr3` 都只是在栈空间分配一个引用空间，存放引用 `null`。
* 方法二：`arr2 = new int[]{1, 2, 3};` 此时 JVM 才开始在内存堆空间分配空间并直接进行赋值。
* 方法三：`arr3 = new int[3];` 此时采用的是默认初始化，因为 `arr3` 是基本类型(int)的 Array，所以默认值是 0。如果是 boolean 类型的，则默认值是 `false`。
* 动态初始化：数组定义与为数组分配空间和赋值的操作分开进行。
* 静态初始化：在定义数字的同时就为数组元素分配空间并赋值。
* 默认初始化：数组是引用类型，它的元素相当于类的成员变量，因此数组分配空间后，每个元素也按照成员变量的规则被隐式初始化。

### 1. Print an array in Java ()
```java 
package org.test;
import java.util.Arrays;
public class Test1 {
    public static void main(String args[]) {
        int[] intArray = {1, 2, 3, 4, 5};  
        
        //数组输出，方法一
        int i=0;
        for(i=0; i<5; i++){
            System.out.println(intArray[i]);
        }

        //数组输出，方法二
        for (int shuzu : intArray) {
            System.out.println(shuzu);
        }
             
        String intArrayString = Arrays.toString(intArray);  
        // print directly will print reference value   
        System.out.println(intArray);        // [I@7150bd4d   
        System.out.println(intArrayString);  // [1, 2, 3, 4, 5]
    }
}
```


### 2. Create an ArrayList from an array
```java 
String[] stringArray = {"a", "b", "c", "d", "e"};
ArrayList<String> arrayList = new ArrayList<String>(Arrays.asList(stringArray));
System.out.println(arrayList);      //输出： [a, b, c, d, e] 
```
* `public static <T> List<T> asList(T... a)`: Returns a fixed-size list backed by the specified array.


### 3. Check if an array contains a certain value ()
```java 
String[] stringArray = { "a", "b", "c", "d", "e" };
boolean b = Arrays.asList(stringArray).contains("a");
System.out.println(b);      // true 
```
* 通过 `Arrays.asList()` 将 Array 转换为 ArrayList，然后调用 List 的 `contains()` method。


### 4. Concatenate two array ()
```java 
int[] intArray = {1, 2, 3, 4, 5};
int[] intArray2 = {6, 7, 8, 9, 10};
// Apache Commons Lang library（ArrayUtils 是 Apache 提供的 class）
int[] combinedIntArray = ArrayUtils.addAll(intArray, intArray2); 
```


### 5. Declare an array inline ()
```java 
method(new String[]{"a", "b", "c", "d", "e"});
```
 

### 6. Joins the elements of the provided array into a single String
```java 
// containing the provided list of elements
// Apache common lang
String j = StringUtils.join(new String[] { "a", "b", "c" }, ", ");
System.out.println(j);
// a, b, c 
```
* 将 `String[]` 中的元素添加到独立的字符串(String)中。


### 7. Convert an ArrayList to an array
```java 
String[] stringArray = { "a", "b", "c", "d", "e" };
ArrayList<String> arrayList = new ArrayList<String>(Arrays.asList(stringArray));
String[] stringArr = new String[arrayList.size()];
arrayList.toArray(stringArr);
for (String s : stringArr) {
    System.out.println(s);
}
```
> `public <T> T[] toArray(T[] a)`: Returns an array containing all of the elements in this list in proper sequence (from first to last);
> the runtime type of the returned array is that of the specified array.         
> [根据提供的 array 类型返回特定的类型的 array]

### 8. Convert an array to a set ()
```java 
Set<String> set = new HashSet<String>(Arrays.asList(stringArray));
System.out.println(set);//[d, e, b, c, a] 
```
> `HashSet(Collection<? extends E> c`: Constructs a new set containing the elements in the specified collection.        
> [构造器可以根据一个 Collection 对象直接创建 Set 对象。]


### 9. Reverse an array ()
```java 
int[] intArray = {1, 2, 3, 4, 5 };
ArrayUtils.reverse(intArray);
System.out.println(Arrays.toString(intArray));  //[5, 4, 3, 2, 1] 
```
* `ArrayUtils.reverse()`


### 10. Remove element of an array ()
```java 
int[] intArray = {1, 2, 3, 4, 5};
int[] removed = ArrayUtils.removeElement(intArray, 3);  //create a new array
System.out.println(Arrays.toString(removed)); 
```
* Array 长度不可改变


### 11. Convert into byte array ()
```java 
byte[] bytes = ByteBuffer.allocate(4).putInt(8).array();
for (byte t : bytes) {
    System.out.format("0x%x ", t);
} 
```


---
## JDK1.8源码解读之 Arrays

## Reference:
1. [Java数组应用十大技巧攻略](https://blog.csdn.net/zolalad/article/details/11757743)
2. [java 创建数组的三种方式及区别](https://blog.csdn.net/xu511739113/article/details/52350519)
3. [Class Arrays](https://docs.oracle.com/javase/8/docs/api/)
4. [JDK1.8源码解读之 Arrays](https://juejin.im/post/5e906a0f51882573c46782ba)
5. []()
