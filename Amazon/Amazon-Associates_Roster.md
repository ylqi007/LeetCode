[ [面试经验] 亚麻 新鲜OA2 NG全职 08/21/2020 ](https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=662496&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3046%5D%5Bvalue%5D%3D5%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline)

[Playground - AssociatesRosterWays](https://leetcode.com/playground/X7YCu9Dy)

```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static long getAssociateWays(int num, List<Integer> skills, int minAssociates, int minLevel, int maxLevel) {
        int m = 0;
        for(int i=0; i<skills.size(); i++) {
            if(skills.get(i) >= minLevel && skills.get(i) <= maxLevel) {
                m++;
            }
        }
        if(m < minAssociates) {
            return 0;
        }
        long[] factors = new long[m+1];
        factors[0] = 1;
        for(int i=1; i<=m; i++) {
            factors[i] = factors[i-1] * i;
        }
        long res = 0;
        for(int n=minAssociates; n<=m; n++) {
            res = res + factors[m] / factors[m-n] / factors[n];
        }
        return res;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        /*
        * Example 1
        */
        int num1 = 6;
        List<Integer> skills = Arrays.asList(12, 4, 6, 23, 5, 10);
        System.out.println(getAssociateWays(num1, skills, 3, 4, 10));
    }
}
```

