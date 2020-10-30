[Google | OA 2019 | Compare Strings](https://leetcode.com/discuss/interview-question/352458/)

Questions:
1. Strictly smaller: `freq of the smallest char of A` < `freq of the smallest char of B`


Example 1:
```
A = "abcd, aabc, bd"
B = "aaa, aa"
The function should return [3, 2]
Explanation: 
```


[Playground - Google | OA 2019 | Compare Strings](https://leetcode.com/playground/TB9x6Avj)
Key Points: [Ref](https://leetcode.com/discuss/interview-question/352458/Google-or-OA-2019-or-Compare-Strings/319613)
1. Count the frequency of the smallest character of each string, i.e. get `freq`;
2. Count the num of each freq, i.e. `freqs[freq]`, which means the `freq` appears `freqs[freq]` times;
3. Use prefix to count the freq less than a specific times, i.e. `freqs[i] = freqs[0] + freqs[1] + ... + freqs[i]`;
4. Count the freq of the smallest character in string B, if `freq = i`, then there is `freqs[0] + freqs[1] + ... + freqs[i-1]` smaller strings.


```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static int[] compareStrings(String A, String B) {
        String[] strsA = A.split(",");
        String[] strsB = B.split(",");
        int lenA = strsA.length;
        int lenB = strsB.length;
        int[] freqs = new int[11];  // max freq = 10
        int[] res = new int[lenB];
        
        // Count the freq of the smallest character in A
        for(String s: strsA) {
            if(s.length() == 0) {
                continue;
            }
            int[] counts = new int[26];
            int minIdx = Integer.MAX_VALUE;    // Initially value, not 25
            for(char c: s.toCharArray()) {
                counts[c - 'a']++;
                minIdx = Math.min(minIdx, c - 'a');
            }
            int freq = counts[minIdx];
            freqs[freq]++;  // the num of string which has freq
        }
        // Use prefix sum to easily get sum from idx 0 to i
        for(int i=1; i<11; i++) {
            freqs[i] += freqs[i - 1];
        }
        
        // 
        for(int i=0; i<lenB; i++) {
            String s = strsB[i];
            int[] counts = new int[26];
            int minIdx = Integer.MAX_VALUE;
            for(char c: s.toCharArray()) {
                counts[c - 'a']++;
                minIdx = Math.min(minIdx, c - 'a');
            }
            int freq = counts[minIdx];
            res[i] = (freq - 1 >= 0) ? freqs[freq-1] : 0;
        }
        return res;
    }
    
    public static void printArray(int[] arr) {
        for(int i: arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        // Example:
        String[] testcasesA = {"abcd,aabc,bd"};
        String[] testcasesB = {"aaa,aa"};
        for(int i=0; i<testcasesA.length; i++) {
            int[] res = compareStrings(testcasesA[i], testcasesB[i]);
            printArray(res);
        }
    }
}
```


