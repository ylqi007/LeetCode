[Substrings of size K with K distinct chars](https://leetcode.com/discuss/interview-question/370112)


## [Java Sliding Window](https://leetcode.com/playground/LRBxfw5W)
[leetcode - discuss](https://leetcode.com/discuss/interview-question/344976/Amazon-or-OA-2019-or-Substrings-of-size-K-with-K-distinct-chars)
[leetcode - playground](https://leetcode.com/playground/Knis2PNL)

* `Set<Character> window` 记录在 size = k 的 window 之内包含的 unique Character，如果 `window.size() == k` ==> this is a satisfied substring. 
* `Set<String> result` 记录符合要求的 substring，为了避免重复，所以此处用了 `Set<String>`.
* 
*

```java
public class Main {
    
    public static List<String> kSubstring(String s, int k) {
        Set<Character> window = new HashSet<>();
        Set<String> result = new HashSet<>();
        for (int start = 0, end = 0; end < s.length(); end++) {
            for (; window.contains(s.charAt(end)); start++) {
                window.remove(s.charAt(start));
            }

            window.add(s.charAt(end));

            if (window.size() == k) {
                result.add(s.substring(start, end + 1));
                window.remove(s.charAt(start++));
            }
        }
        return new ArrayList<>(result);
    }
    
    public static void main(String[] args) { 
        System.out.println(kSubstring("awaglknagawunagwkwagl", 4));
    }
}
```

* 对于内部 `for-loop` 的分析：
```java
for (; window.contains(s.charAt(end)); start++) {
    window.remove(s.charAt(start));
}
```


## Method 2. [Sliding window](https://leetcode.com/discuss/interview-question/370112/Amazon-or-OA-2019-or-Substrings-of-size-K-with-K-distinct-chars/351761)
```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static List<String> kSubstring(String s, int k) {
        int distinct = 0;   // the number of distinct characters
        int i = 0;          // the index of string s
        int[] memo = new int[26];
        Set<String> set = new HashSet<>();
        for( ; i<k; i++) {  // Initialization, i.e. add the first k characters into memo
            if(memo[s.charAt(i) - 'a'] == 0) {  // a unique character
                distinct++;
            }
            memo[s.charAt(i) - 'a']++;
        }
        if(distinct == k) { // If the first k characters is unique 
            set.add(s.substring(i-k, i));
        }
        while(i < s.length()) {
            if(memo[s.charAt(i) - 'a'] == 0) {
                distinct += 1;
            }
            memo[s.charAt(i) - 'a'] += 1;
            memo[s.charAt(i-k) - 'a'] -= 1;
            if(memo[s.charAt(i-k) - 'a'] == 0) {
                distinct -= 1;
            }
            if(distinct == k) {
                set.add(s.substring(i-k+1, i+1));
            }
            i++;
        }
        return new ArrayList<>(set);
    }
    
    
    public static void main(String[] args) {
        List<String> expected = Arrays.asList("wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag");
        Collections.sort(expected);
        
        List<String> output = kSubstring("awaglknagawunagwkwagl", 4);
        Collections.sort(output);
        
        System.out.println("Output:");
        System.out.println(output);
        
        // System.out.println("Expected:");
        System.out.println(expected);
    }
}
```