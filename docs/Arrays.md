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

#### LeetCode题目
* 344 Reverse String
* 26 Remove duplicates from sorted array
* 11
* 42
* 283
* 80
* 1047