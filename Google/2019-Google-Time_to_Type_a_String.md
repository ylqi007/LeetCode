[Google | OA 2019 | Time to Type a String](https://leetcode.com/discuss/interview-question/356477)   

[1165. Single-Row Keyboard](https://leetcode.com/problems/single-row-keyboard/)


## Method 1. My Solution
Notes:
* The keyboard may not alphabetically.

Key Points:
1. Since there are only 26 characters, then we can use an array to store the index of each character: `idx[keyboard.charAt(i) - 'a'] = i`
2. I use two pointers to locate the positions of previous character and current one, and initialize `i = -1, j = 0`, and they will increase every iteration.
3. When `i = -1`, which means our finger at the first position. 
```java
class Solution {
    public int calculateTime(String keyboard, String word) {
        if(word == null || word.length() == 0) {
            return 0;
        }
        int[] idx = new int[26];
        for(int i=0; i<keyboard.length(); i++) {
            idx[keyboard.charAt(i) - 'a'] = i;
        }
        int res = 0;
        for(int i=-1, j=0; j<word.length(); i++, j++) {
            if(i == -1) {
                res += Math.abs(idx[word.charAt(0) - 'a'] - 0);
            } else {
                res += Math.abs(idx[word.charAt(j) - 'a'] - idx[word.charAt(i) - 'a']);
            }
        }
        return res;
    }
}
```
Complexity:
1. Time: O(N), where N is the length of `word`;
2. Space: O(1)












