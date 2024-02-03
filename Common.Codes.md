[toc]

### 1. Convert `stream<T>` to `T[]`
```Java
// 1. toArray()
Object[] array = stream.toArray();

// 2. toArray(IntFunction<A[]> generator)
// Using Method reference: `String[]::new` calls constructor of `String`
String[] array = stream.toArray(String[]::new);
```

Example 1:
```Java
Stream<Integer> stream = Stream.of(1, 2, 3, 4, 5);
Integer[] intArray = stream.toArray(Integer[]::new);
```

#### 1.1 Convert `stream<Integer>` to `int[]`
Converting a stream of `Integer` objects to a primitive integer array is not straightforward in Java.
```Java
Stream<Integer> stream = Stream.of(1, 2, 3, 4, 5);
int[] array = stream.mapToInt(Integer::intValue).toArray();
```

## Important Classes In Java
在刷LeetCode的过程中，有一些class是常用的，但是不同的它们的method可能还有一些区别。因此，列出来，要重点掌握
* [java.lang.Character](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Character.html)
* [java.lang.String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)
* [Interface java.util.Comparator<T>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Comparator.html)
* [Interface java.util.Deque<E>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Deque.html) [念做dai ke]
* [java.util.ArrayDeque<E>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/ArrayDeque.html) [`implement Deque`]
* [java.util.LinkedList<E>](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/LinkedList.html)  [`implement Deque`, 以后尽量用 `Deque<E> deque = new LinkedList<>()`]
* [java.util.PriorityQueue](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/PriorityQueue.html)
* [java.util.stream.Stream](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html)
* [Summary of regular-expression constructs](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html#sum)


**Reference**
* https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html
* [Convert Stream to an array in Java](https://www.techiedelight.com/convert-stream-array-java/#2)
* [Convert Integer List to an int array in Java](https://www.techiedelight.com/convert-list-integer-array-int/)
* [How can I convert List<Integer> to int[] in Java? [duplicate]](https://stackoverflow.com/questions/960431/how-can-i-convert-listinteger-to-int-in-java)
* [How to convert an ArrayList containing Integers to primitive int array?](https://stackoverflow.com/questions/718554/how-to-convert-an-arraylist-containing-integers-to-primitive-int-array?noredirect=1&lq=1)
