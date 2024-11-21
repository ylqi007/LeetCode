# 对象比较
**基础数据类型**（除了boolean类型）可以直接用比较运算符比较大小，但是**引用数据类型**不能直接使用比较运算符比较大小。


对数组(Arrays)或集合(Collections)中的元素进行排序时，经常会使用到`Arrays.sort()`或者`Collections.sort()`。

* 接口`interface java.lang.Comparable<T>`中有一个`int compareTo(T o)`方法，用于与其他对象的比较。一个类只要实现了这个接口，就意味着该类支持自然排序。所谓的自然排序，就是按照一定的默认规则进行排序。
* 接口`interface java.util.Comparator<T>`是util包中的**比较器接口**，比较器(Comparator)可以用于对类进行排序，但是类本身并不要求实现其他接口。


## Comparable: 自然排序
* `interface java.lang.Comparable<T>`: https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/lang/Comparable.html
* 实现`Comparable`的类必须实现`compareTo(Object obj)`方法，两个对象即通过`compareTo(Object obj)`方法的返回值来比较大小。
  * 如果当前对象`this`大于形参对象`obj`，则返回正整数，
  * 如果当前对象`this`小于形参对象`obj`，则返回负整数，
  * 如果当前对象`this`等于形参对象`obj`，则返回零。

```java
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.ToString;

@AllArgsConstructor
@ToString
@Getter
public class Product implements Comparable {
    private String name;
    private double price;

    /**
     * Product类需要实现 Comparable 接口中的抽象方法compareTo(Object o)
     *  按照价格高低排序（从小到大, or 从大到小）
     *
     * @param o the object to be compared.
     * @return
     *  返回正数(+): 当前对象大，i.e. this
     *  放回负数(-): 当前对象小
     *  放回0: 两者一样大
     */
    @Override
    public int compareTo(Object o) {
        if(this == o) {
            return 0;
        }

        if(o instanceof Product) {
            Product p = (Product) o;
            // 比较价格大小
            int value = Double.compare(this.price, p.price); // 注意this和o的前后有要求
            if(value != 0) {
                return -value;  // Price 从大到小
            }

            return this.name.compareTo(p.name);
        }
        throw new RuntimeException("类型不匹配");
    }
}
```

## Comparator: 定制排序
* `interface java.util.Comparator<T>`: https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Comparator.html
* Comparator的使用场景:
  * 当对象类型没有实现`Comparable`接口，又不方便修改代码。比如，调用第三方类，但是该类又没有实现`Comparable`接口，我们又无法修改源代码
  * 虽然对象实现了`Comparable`接口，但是不想按照预定以的方法比较大小

```java
import java.util.Arrays;
import java.util.Comparator;

public class ComparatorTest {

    @Test
    public void test01() {
        Product[] products = {
                new Product("Apple1", 100),
                new Product("Apple199", 200),
                new Product("Apple200", 200),
                new Product("Apple201", 200),
                new Product("Apple3", 300),
                new Product("Apple4", 40),
        };

        // 创建一个实现了Comparator接口的实现类对象
        Comparator comparator = new Comparator() {
            // 比较两个对象o1，o2的大小
            @Override
            public int compare(Object o1, Object o2) {
                if(o1 instanceof Product && o2 instanceof Product) {
                    Product p1 = (Product) o1;
                    Product p2 = (Product) o2;
                    return -Double.compare(p1.getPrice(), p2.getPrice());   // 价格从高到低

                }
                throw new RuntimeException("类型不匹配");
            }
        };

        Comparator<Product> comparator1 = new Comparator<Product>() {
            @Override
            public int compare(Product o1, Product o2) {
                return o1.getName().compareTo(o2.getName());
            }
        };

        Arrays.sort(products, comparator1);
        for(Product p: products) {
            System.out.println(p);
        }
    }
}
```

## 对比
1. 角度一
    1. 自然排序是单一的，唯一的
    2. 定制排序，灵活的，多样的
2. 角度二
    1. 一旦实现Comparable接口，一劳永逸
    2. 定制的，临时的，需要
3. 角度三
    1. 自然排序: Comparable接口，compareTo(Object obj)
    2. 定制排序: Comparator接口， compare(Object o1, Object o2)


## Reference
* [Java Comparable 和 Comparator 接口详解](https://www.cnblogs.com/Yee-Q/p/13729929.html)
* 宋红康: [《Java从入门到精通（JDK17版）》 Chapter 11.5](../books/《Java从入门到精通(JDK17版)》_尚硅谷电子书.pdf)
* 宋红康: https://www.bilibili.com/video/BV1PY411e7J6?spm_id_from=333.788.videopod.episodes&vd_source=bd5e1cdd20d83feef8e77a781b33f083&p=149
* 宋红康: https://www.bilibili.com/video/BV1PY411e7J6?spm_id_from=333.788.videopod.episodes&vd_source=bd5e1cdd20d83feef8e77a781b33f083&p=150
