[Showing binary search correct using strong induction](http://www.cs.cornell.edu/courses/cs211/2006sp/Lectures/L06-Induction/binary_search.html)

[Overflow bug](https://en.wikipedia.org/wiki/Binary_search_algorithm#Implementation_issues)

The recipe for strong induction(强推理) is as follows:
1. State the proposition P(n) that you are trying to prove to be true for all n.
2. Base case: Prove that the proposition holds for n = 0, i.e., prove that P(0) is true.
3. Inductive step: Assuming the induction hypothesis that P(n) holds for all n between 0 and k, prove that P(k+1) is true.
4. Conclude by strong induction that P(n) holds for all n ≥ 0. 







