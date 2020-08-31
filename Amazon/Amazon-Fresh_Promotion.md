[Amazon | OA 2020 | Amazon Fresh Promotion](https://leetcode.com/discuss/interview-question/762546/)

* [392.Is Subsequence](https://leetcode.com/problems/is-subsequence/)

题意：生鲜促销
Input：
1. `codeList`：代表中奖必须包含的水果列表和相应的顺序。
2. `shoppingCart`：代表客户购买水果的顺序。
* `anything`：It cannot be "nothing" and must represent one and only one fruit.
* If secret code list is empty then it is assumed that the customer is a winner.
 

Example 1.

    Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [orange, apple, apple, banana, orange, banana]
    Output: 1
    Explanation:
    codeList contains two groups - [apple, apple] and [banana, anything, banana].
    The second group contains 'anything' so any fruit can be ordered in place of 'anything' in the shoppingCart. The customer is a winner as the customer has added fruits in the order of fruits in the groups and the order of groups in the codeList is also maintained in the shoppingCart.
1. `shoppingCart` 包含 `codeList` 中的两个 groups；
2. 第二个 group 中的 anything 可以代替任何 fruit。


Example 4: 反面例子

    Input: codeList = [[apple, apple], [apple, apple, banana]] shoppingCart = [apple, apple, apple, banana]
    Output: 0
    Explanation:
    The customer is not a winner as the first 2 fruits form group 1, all three fruits would form group 2, but can't because it would contain all fruits of group 1.


## [Solution 1](https://leetcode.com/discuss/interview-question/762546/Amazon-or-OA-2020-or-Amazon-Fresh-Promotion/641640)
> Intuitive Java solution inspired by `392. Is subsequence`. 
> Use two pointers i and j respectively for an element in two given lists. 
> For a specific code `codelist[i]`, check the subarray with the same length of `codelist[i]` starting from `j` in `shoppingcart`.

双指针：
1. Pointer `i` 是 `codeList` 中某个 group, i.e. `codeList[i]` 的 index。
2. Pointer `j` 是 `shoppingCart` 中某个 fruit 的 index，也是与 `codeList[i]` 开始匹配的第一个 fruit 的 index。
3. 如果 `codeList[i][k]` 不是 `anything` && 与 `shoppingCart[j]` 不匹配的时候，则 `codeList[i]` 没有被 match。
4. 如果 `codeList[i]` 已经被 match 了，就从 `shoppingCart` 中跳过 `codeList[i]`， 因为 `codeList[i+1]` 不能有重叠。

```java
public class FindFruitCombs {
    /**
     * Aug/03/2020
     * Amazon OA 2020
     * https://leetcode.com/discuss/interview-question/762546/
     */

    public static int winPrize(String[][] codeList, String[] shoppingCart) {
        // checking corner cases
        if(codeList == null || codeList.length == 0)
            return 1;
        if(shoppingCart == null || shoppingCart.length == 0)
            return 0;

        int i = 0, j = 0;
        //int codeLen = codeList[i].length;
        while (i < codeList.length && j + codeList[i].length <= shoppingCart.length) {
            boolean match = true;
            for (int k = 0; k < codeList[i].length; k++) {
                if (!codeList[i][k].equals("anything") && !shoppingCart[j+k].equals(codeList[i][k])) {
                    match = false;
                    break;
                }
            }
            if (match) {
                j += codeList[i].length;
                i++;
            } else {
                j++;
            }
        }
        return (i == codeList.length) ? 1 : 0;
    }

    public static void test(String[][] codeList, String[] shoppingCart, int expect) {
        System.out.println(winPrize(codeList, shoppingCart) == expect);
    }

    public static void main(String[] args) {
        // test cases
        String[][] codeList1 = { { "apple", "apple" }, { "banana", "anything", "banana" } };
        String[] shoppingCart1 = {"orange", "apple", "apple", "banana", "orange", "banana"};
        String[][] codeList2 = { { "apple", "apple" }, { "banana", "anything", "banana" } };
        String[] shoppingCart2 = {"banana", "orange", "banana", "apple", "apple"};
        String[][] codeList3 = { { "apple", "apple" }, { "banana", "anything", "banana" } };
        String[] shoppingCart3 = {"apple", "banana", "apple", "banana", "orange", "banana"};
        String[][] codeList4 = { { "apple", "apple" }, { "apple", "apple", "banana" } };
        String[] shoppingCart4 = {"apple", "apple", "apple", "banana"};
        String[][] codeList5 = { { "apple", "apple" }, { "banana", "anything", "banana" } };
        String[] shoppingCart5 = {"orange", "apple", "apple", "banana", "orange", "banana"};
        String[][] codeList6 = { { "apple", "apple" }, { "banana", "anything", "banana" }  };
        String[] shoppingCart6 = {"apple", "apple", "orange", "orange", "banana", "apple", "banana", "banana"};
        String[][] codeList7= { { "anything", "apple" }, { "banana", "anything", "banana" }  };
        String[] shoppingCart7 = {"orange", "grapes", "apple", "orange", "orange", "banana", "apple", "banana", "banana"};
        String[][] codeList8 = {{"apple", "orange"}, {"orange", "banana", "orange"}};
        String[] shoppingCart8 = {"apple", "orange", "banana", "orange", "orange", "banana", "orange", "grape"};
        String[][] codeList9= { { "anything", "anything", "anything", "apple" }, { "banana", "anything", "banana" }  };
        String[] shoppingCart9 = {"orange", "apple", "banana", "orange", "apple", "orange", "orange", "banana", "apple", "banana"};

        // test
        test(codeList1, shoppingCart1, 1);
        test(codeList2, shoppingCart2, 0);
        test(codeList3, shoppingCart3, 0);
        test(codeList4, shoppingCart4, 0);
        test(codeList5, shoppingCart5, 1);
        test(codeList6, shoppingCart6, 1);
        test(codeList7, shoppingCart7, 1);
        test(codeList8, shoppingCart8, 1);
        test(codeList9, shoppingCart9, 1);
    }
}
```

Complexity:
* O(MN) solution where `M` is the average number of items in each code group, and `N` is the number of items in the shopping cart. 
The idea is to consider each item in the `shoppingCart` as the start of the current code group we are processing. 
If the current cart item did not match with the current code group, then move to the next cart item and try to match that with the current code group. 
Return true if you can match all code groups before hitting end of the cart.


## Reference:
1. [Code with Comments](https://leetcode.com/playground/eEatKB4z)




