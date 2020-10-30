[Amazon | OA 2019 | Movies on Flight](https://leetcode.com/discuss/interview-question/313719/Amazon-or-Online-Assessment-2019-or-Movies-on-Flight)

**Movies on Flights** 要求两个 numbers 的和 `<= target` 的同时，尽可能的大。

[LeetCode - Playground](https://leetcode.com/playground/8Cs9aGAe)
```java
// "static void main" must be defined in a public class.
public class MoviesOnFlights {
    
    public static int[] get2SumClosest(int[] movies, int target) {
        Map<Integer, List<Integer>> map = new HashMap<>();  // movie duration --> indexes
        for(int i=0; i<movies.length; i++) {
            map.putIfAbsent(movies[i], new ArrayList<>());
            map.get(movies[i]).add(i);
        }
        Arrays.sort(movies);    // ascending order
        int l = 0;
        int r = movies.length - 1;
        int max = 0;
        int[] res = new int[]{-1, -1};
        while(l < r) {
            int sum = movies[l] + movies[r];
            if((sum > max || (sum == max && Math.max(movies[l], movies[r]) > Math.max(res[0], res[1]))) && sum <= target) {
                max = sum;
                res[0] = movies[l];
                res[1] = movies[r];
            }
            if(sum > target) {
                r--;
            } else {
                l++;
            }
        }
        if(map.get(res[0]) == map.get(res[1])) {
            res[0] = map.get(res[0]).get(0);
            res[1] = map.get(res[1]).get(1);
        } else {
            res[0] = map.get(res[0]).get(0);
		    res[1] = map.get(res[1]).get(0);
        }
        return res;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        int d1 = 250;
        int[] movie_duration1 = {90, 85, 75, 60, 120, 150, 125};
        System.out.println(Arrays.toString(get2SumClosest(movie_duration1, d1-30)));
        
        int d2 = 250;
        int[] movie_duration2 = {90, 85, 75, 60, 155, 150, 125};
        System.out.println(Arrays.toString(get2SumClosest(movie_duration2, d2-30)));
        
        int d3 = 250;
        int[] movie_duration3 = {90, 85, 75, 60, 120,110,110, 150, 125};        
        System.out.println(Arrays.toString(get2SumClosest(movie_duration3, d3-30)));
        
        int d4 = 250;
        int[] movie_duration4 = {90, 85, 75, 60, 120,110,110, 150, 125};        
        System.out.println(Arrays.toString(get2SumClosest(movie_duration4, d4-30)));
    }
}
```