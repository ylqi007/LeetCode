[Google | OA 2019 | Maximum Time](https://leetcode.com/discuss/interview-question/396769/)      


Intuition: 分别确认每位最大值。

Analysis:
1. if `s.charAt(1) == '?' || Integer.valueOf(s.charAt(1)) < 4`, then `s.charAt(0) = 2` else `1`;
2. if `s.charAt(0) == '?' || Integer.valueOF(s.charAt(0)) < 2`, then `s.charAt(1) = 9` else `3`;
    * 此时不用考虑 `s.charAt(0) == '?'`, 因为在此之前已经改变了。
3. `s.charAt(3) = 5`
4. `s.charAt(4) = 9`

[Playground - Google | OA 2019 | Maximum Time](https://leetcode.com/playground/PKEKjSDY)   
```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static void getMaxTime(String str) {
        char[] cs = str.toCharArray();
        
        if(cs[0] == '?') {
            cs[0] = (cs[1] == '?' || cs[1] < '4') ? '2' : '1';
        }
        if(cs[1] == '?') {
            cs[1] = (cs[0] == '2') ? '3' : '9';
        }
        
        cs[3] = (cs[3] == '?') ? '5' : cs[3];
        cs[4] = (cs[4] == '?') ? '9' : cs[4];
        
        System.out.println(new String(cs));
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        getMaxTime("23:5?");// 23:59
        getMaxTime("2?:22");// 23:22
        getMaxTime("0?:??");// 09:59
        getMaxTime("1?:??");// 19:59
        getMaxTime("?4:??");// 14:59
        getMaxTime("?3:??");// 23:59
        getMaxTime("??:??");// 23:59
        getMaxTime("?4:5?"); //14:59
        getMaxTime("?4:??"); //14:59
        getMaxTime("?3:??"); //23:59
        getMaxTime("23:5?"); //23:59
        getMaxTime("2?:22"); //23:22
        getMaxTime("0?:??"); //09:59
        getMaxTime("1?:??"); //19:59
        getMaxTime("?4:0?"); //14:09
        getMaxTime("?9:4?"); //19:49
    }
}
```
