
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

#### 1.2 Convert `List<int[]>` to `int[][]`
```java
import java.util.List;
import java.util.ArrayList;

public class HelloWorld{

     public static void main(String []args){
        List<int[]> result = new ArrayList<>();
        result.add(new int[]{0, 0});
        result.add(new int[]{1, 1});
        result.add(new int[]{2, 2});
        
        int[][] temp = result.toArray(int[][]::new);
        for(int[] value: temp) {
            System.out.println("{" + value[0] + ", " + value[1] + "}");
        }
     }
}
```
* https://stackoverflow.com/questions/5061640/make-arraylist-toarray-return-more-specific-types/77798156#77798156


#### Reference
* [How to convert an ArrayList containing Integers to primitive int array?](https://stackoverflow.com/questions/718554/how-to-convert-an-arraylist-containing-integers-to-primitive-int-array?noredirect=1&lq=1)
* [How can I convert List<Integer> to int[] in Java? [duplicate]](https://stackoverflow.com/questions/960431/how-can-i-convert-listinteger-to-int-in-java)
* [make arrayList.toArray() return more specific types](https://stackoverflow.com/questions/5061640/make-arraylist-toarray-return-more-specific-types/77798156#77798156)
* https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html
* [Convert Stream to an array in Java](https://www.techiedelight.com/convert-stream-array-java/#2)
* [Convert Integer List to an int array in Java](https://www.techiedelight.com/convert-list-integer-array-int/)