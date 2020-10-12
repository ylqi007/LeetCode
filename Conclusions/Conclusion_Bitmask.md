在很多用 DFS 和 backtracking 算法解决的问题中，其实还可以用 DP + Bit Masking 进行优化。

Mask in *bitmask* means hiding something. Bitmask is nothing but a binary number
that represents something.

For example, consider a set `A = {1, 2, 3, 4, 5}`. We can represent any subsets of
`A` using a bitmask of length 5, with an assumption that if `i-th` (0<=i<=4) bit is
set(i.e. is 1) then it means `i-th` element is present in the subset. So the
bitmask `01010` represents the subset `{2, 4}`.

As for the benefit of using bitmask, we can set and unset `i-th` bit and check
if `i-th` bit is set in just one step each.         
Let's say the bitmask `mask = 01010`:
1. Set the `i-th` bit by `mask | (1 << i)`. Let `i = 0`, so,
`(1 << i) = 00001`,     
`01010 | 00001 = 01011`. 
So the subset includes `0-th` element now and the subset is `{1, 2, 4}`.
2. Unset the `i-th` bit by `mask & !(1 << i)`. Let `i=1`, so,
`1 << i = 00010`, then `!(1 << i) = 11101`,
`01010 & 11101 = 01000`. 
So the subset does not include the `1-th` element and the subset is `{4}`.
3. Check if the `i-th` bit is set or not by `mask & (1 << i)`. If the `i-th` bit is
set, we get a non zero, otherwise we get zero. Let `i=3`, so,
`1 << i == 01000`,
`01010 & 01000 = 01000`.
Since the current result is non-zero, so that means 3rd element is present in the 
subset.




[DP with Bit Masking Solution :- Best for Interviews](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/335668/dynamic-programming-with-bit-masking-solution-best-for-interviews)
