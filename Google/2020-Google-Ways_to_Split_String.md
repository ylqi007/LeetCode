[Google | OA 2020 | Ways to Split String](https://leetcode.com/discuss/interview-question/553399/)  

Questions:
1. Split string `S` into 2 strings: `S1` and `S2`;
2. Make sure that the number of unique characters between `S1` and `S2` are the same;
3. Return how many ways can achieve this.


Example 1:
```
Input: "aaaa"
Output: 3
Explanation: we can get a - aaa, aa - aa, aaa- a
```

Example 2:
```
Input: "bac"
Output: 0
```

Example 3:
```
Input: "ababa"
Output: 2
Explanation: ab - aba, aba - ba
```


Analysis 1:       
将 String split 成两个 substring，然后分别用一个 Set 记录 unique characters，然后比较 Set 的 size 是否相同。


Analysis 2: [Ref](https://leetcode.com/discuss/interview-question/553399/Google-or-OA-2020-or-Min-Amplitude-and-Ways-to-Split-String/534227)
1. Splitting a string `s` into `s1` and `s2`;
2. In the first loop, `s1 = ""` and `s2 = s`;
3. In the second loop, remove character from `s2` and add to `s1`. Then, compare the keySet of `s1` and `s2`.

[Playground - Google | OA 2020 | Ways to Split String](https://leetcode.com/playground/S2DxgRHn)

```java
// https://leetcode.com/discuss/interview-question/553399/
public class Main {
    
    public static int splitStringUniqueChars(String s) {
        Map<Character, Integer> left = new HashMap<>();
        Map<Character, Integer> right = new HashMap<>();
        
        int res = 0;
        // Init: s1 = "", s2 = s
        for(char c: s.toCharArray()) {
            right.put(c, right.getOrDefault(c, 0) + 1);
        }
        
        // Move character from right substring to left substring
        for(char c: s.toCharArray()) {
            // Remove from right
            right.put(c, right.get(c) - 1);
            // Add to left
            left.put(c, left.getOrDefault(c, 0) + 1);
            
            if(right.get(c) == 0) {
                right.remove(c);
            }
            if(right.keySet().size() == left.keySet().size()) {
                res++;
            }
        }
        return res;
    }
    
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        // Example 1: expected 3
        System.out.println(splitStringUniqueChars("aaaa"));
        
        // Example 2: expected 0
        System.out.println(splitStringUniqueChars("abc"));
        
        // Example 3: expected 2
        System.out.println(splitStringUniqueChars("ababa"));
        
        
    }
}
```
