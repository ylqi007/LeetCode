[Amazon | OA 2020 | Top K Frequently Mentioned Keywords](https://leetcode.com/discuss/interview-question/542597/)  

* [Amazon | OA 2020 | Top K Frequently Mentioned Keywords](https://leetcode.com/playground/mVZ4uyeQ)
* [Amazon | OA 2020 | Top K Frequently Mentioned Keywords_2](https://leetcode.com/playground/o7Ebw9bn)
* [Amazon | OA 2020 | Top K Frequently Mentioned Keywords_3](https://leetcode.com/playground/EpDekJq7)   


Key Points:
1. The comparison of strings is case-insensitive. ==> `s.toLowerCase()`;
2. Split the string by using `\\W` as a delimiter for **non word character** in `string.split()` function of java;  
3. 在一个 `review` 中出现过的 `keyword` 只能按出现一次算; 
4. Sort: 
    * Sort in descending order by frequency: high freq --> low freq;
    * Sort alphabetically for strings with the same freq;

```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static List<String> findTopKKeywords(List<String> keywords, List<String> reviews, int k) {
        List<String> res = new ArrayList<>();
        if(keywords == null || reviews == null) {
            return res;
        }
        if(keywords.size() * reviews.size() == 0) {
            return res;
        }
        
        Set<String> set = new HashSet<>(keywords);
        Map<String, Integer> map = new HashMap<>();
        for(String review: reviews) {
            // String[] strs = review.split("\\W");
            String[] strs = review.split("\\W+");
            for(String str: strs) {
                System.out.println("word: " + str);
            }
            
            Set<String> added = new HashSet<>();
            for(String s: strs) {
                s = s.toLowerCase();
                if(set.contains(s) && !added.contains(s)) {
                    map.put(s, map.getOrDefault(s, 0) + 1);
                    added.add(s);
                }
            }
        }
        Queue<Map.Entry<String, Integer>> maxHeap = new PriorityQueue<>((a, b) -> (a.getValue() == b.getValue()) ? a.getKey().compareTo(b.getKey()) : b.getValue() - a.getValue());
        maxHeap.addAll(map.entrySet());
        while(!maxHeap.isEmpty() && k-- > 0) {
            res.add(maxHeap.poll().getKey());
        }
        return res;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        System.out.println("================= Example 1 =====================");
        int k1 = 2;
        List<String> keywords1 = Arrays.asList(new String[]{ "anacell", "cetracular", "betacellular" });
        List<String> reviews1 = Arrays.asList(new String[]{
            "Anacell provides the best services in the city", 
            "betacellular has awesome services", 
            "Best services provided by anacell, everyone should use anacell",
            "id-INT, ,name-STRING,"});
        System.out.println(findTopKKeywords(keywords1, reviews1, k1));
        
        System.out.println("================= Example 2 =====================");
        int k2 = 2;
        List<String> keywords2 = Arrays.asList(new String[]{"anacell", "betacellular", "cetracular", "deltacellular", "eurocell"});
        List<String> reviews2 = Arrays.asList(new String[]{
            "I love anacell Best services; Best services provided by anacell",
			"betacellular has great services", "deltacellular provides much better services than betacellular",
            "cetracular is worse than anacell", "Betacellular is better than deltacellular."});
        System.out.println(findTopKKeywords(keywords2, reviews2, k2));
    }
}
```


## Method 2. 
[Amazon | OA 2020 | Top K Frequently Mentioned Keywords_2](https://leetcode.com/playground/o7Ebw9bn)

* Use the `s.indexOf(sub) >= 0` ==> to find if a keyword exists in a review or not.

```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static List<String> findTopKKeywords(List<String> keywords, List<String> reviews, int k) {
        List<String> res = new ArrayList<>();
        if(keywords == null || reviews == null) {
            return res;
        }
        if(keywords.size() * reviews.size() == 0) {
            return res;
        }
        
        Map<String, Integer> map = new HashMap<>();
        for(String review: reviews) {
            review = review.toLowerCase();
            for(String key: keywords) {
                if(review.indexOf(key) >= 0) {
                    map.put(key, map.getOrDefault(key, 0) + 1);
                }
            }
        }
        Queue<Map.Entry<String, Integer>> maxHeap = new PriorityQueue<>((a, b) -> (a.getValue() == b.getValue()) ? a.getKey().compareTo(b.getKey()) : b.getValue() - a.getValue());
        maxHeap.addAll(map.entrySet());
        while(!maxHeap.isEmpty() && k-- > 0) {
            res.add(maxHeap.poll().getKey());
        }
        return res;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        System.out.println("================= Example 1 =====================");
        int k1 = 2;
        List<String> keywords1 = Arrays.asList(new String[]{ "anacell", "cetracular", "betacellular" });
        List<String> reviews1 = Arrays.asList(new String[]{
            "Anacell provides the best services in the city", 
            "betacellular has awesome services", 
            "Best services provided by anacell, everyone should use anacell",
            "id-INT, ,name-STRING,"});
        System.out.println(findTopKKeywords(keywords1, reviews1, k1));
        
        System.out.println("================= Example 2 =====================");
        int k2 = 2;
        List<String> keywords2 = Arrays.asList(new String[]{"anacell", "betacellular", "cetracular", "deltacellular", "eurocell"});
        List<String> reviews2 = Arrays.asList(new String[]{
            "I love anacell Best services; Best services provided by anacell",
			"betacellular has great services", "deltacellular provides much better services than betacellular",
            "cetracular is worse than anacell", "Betacellular is better than deltacellular."});
        System.out.println(findTopKKeywords(keywords2, reviews2, k2));
    }
    
}
```

## Method 3.
```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static List<String> findTopKKeywords(List<String> keywords, List<String> reviews, int k) {
        List<String> res = new ArrayList<>();
        if(keywords == null || reviews == null) {
            return res;
        }
        if(keywords.size() * reviews.size() == 0) {
            return res;
        }
        
        Map<String, Integer> map = new HashMap<>();
        for(String review: reviews) {
            Set<String> added = new HashSet<>();
            String[] rs = review.toLowerCase().split("\\s+");
            for(String s: rs) {
                if(keywords.contains(s) && !added.contains(s)) {
                    map.put(s, map.getOrDefault(s, 0) + 1);
                    added.add(s);
                }
            }
        }
        res.addAll(map.keySet());
        Collections.sort(res, (a, b) -> (map.get(a)).equals(map.get(b)) ? a.compareTo(b) : map.get(b) - map.get(a));
        return res.subList(0, k);
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        System.out.println("================= Example 1 =====================");
        int k1 = 2;
        List<String> keywords1 = Arrays.asList(new String[]{ "anacell", "cetracular", "betacellular" });
        List<String> reviews1 = Arrays.asList(new String[]{
            "Anacell provides the best services in the city", 
            "betacellular has awesome services", 
            "Best services provided by anacell, everyone should use anacell",
            "id-INT, ,name-STRING,"});
        System.out.println(findTopKKeywords(keywords1, reviews1, k1));
        
        System.out.println("================= Example 2 =====================");
        int k2 = 2;
        List<String> keywords2 = Arrays.asList(new String[]{"anacell", "betacellular", "cetracular", "deltacellular", "eurocell"});
        List<String> reviews2 = Arrays.asList(new String[]{
            "I love anacell Best services; Best services provided by anacell",
			"betacellular has great services", "deltacellular provides much better services than betacellular",
            "cetracular is worse than anacell", "Betacellular is better than deltacellular."});
        System.out.println(findTopKKeywords(keywords2, reviews2, k2));
    }
    
}
```


