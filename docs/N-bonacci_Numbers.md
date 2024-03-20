# [N-bonacci Numbers](https://www.geeksforgeeks.org/n-bonacci-numbers/)

You are given two Integers N and M, and print all the terms of the series upto M-terms of the N-bonacci Numbers. For example, when N = 2, the sequence becomes Fibonacci, when n = 3, sequence becomes Tribonacci.

In general, in N-bonacci sequence, we use sum of preceding N numbers from the next term. For example, a 3-bonacci sequence is the following:
0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81


对于 Fibonacci 数列，每一项都是前两项之和；
对于 N-bonacci 数列，每一项都是前 N 项之和。

* Method 1: Based on memorization
* Method 2: Sliding window, a[i] = a[i-1] + a[i-1] - a[i-n-1] = 2 * a[i-1] - a[i-n-1]
