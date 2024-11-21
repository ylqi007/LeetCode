# Random

## `java.util.Random`
* https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Random.html

**用法:**
```java
import java.util.Random;

public class RandomTest {
    public static void main(String[] args) {
        Random random = new Random();
        for(int i=0; i<10; i++) {
            System.out.println(random.nextInt(5));
        }
    }
}
```

## Reference
* [Java.util.Random类](https://codegym.cc/zh/groups/posts/zh.825.java-util-random-lei)