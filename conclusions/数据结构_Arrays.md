# Arrays

## 1. Java Arrays
Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

To declare an array, define the variable type with square brackets:
```java
String[] cars;
```

## 2. Loop through an Array
### 2.1 Use index `i`
```java
String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
for (int i = 0; i < cars.length; i++) {
  System.out.println(cars[i]);
}
```

### 2.2 Use for-each loop
```java
for (type variable : arrayname) {
  ...
}

String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
for (String i : cars) {
    System.out.println(i);
}
```

## 3. Multidimensional Arrays
A multidimensional array is an array of arrays.

Multidimensional arrays are useful when you want to store data as a tabular form, like a table with rows and columns.

To create a two-dimensional array, add each array within its own set of curly braces:
```java
int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
```


## Two Pointers
### 1. 同向(i,j都向同一个方向移动，比如都往➡️ or 都往⬅️)
#### LeetCode题目
* [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)
* [1868. Product of Two Run-Length Encoded Arrays](https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/description/)

### 2. 方向()


## Sliding Window
> In any sliding window based problem we have two pointers. One `right` pointer whose job is to expand the current window and then we have the `left` pointer whose job is to contract a given window. At any point in time only one of these pointers move and the other one remains fixed.

在sliding window的问题中，一般有两个pointers: 一个是`right` pointer负责扩展current window，另一个是`left` pointer负责缩小current window。在任何时候，只有一个pointer移动，另一个pointer保持不变。


* [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

#### LeetCode题目
* 344 Reverse String
* 26 Remove duplicates from sorted array
* 11
* 42
* 283
* 80
* 1047