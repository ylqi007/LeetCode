```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static int cutOffRank(int cutOffRank, int num, int[] scores) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for(int score: scores) {
            queue.add(score);
            if(queue.size() > cutOffRank) {
                queue.poll();
            }
        }
        Set<Integer> keep = new HashSet<>();
        while(!queue.isEmpty()) {
            keep.add(queue.poll());
        }
        
        int res = 0;
        for(int score: scores) {
            if(keep.contains(score)) {
                res++;
            }
        }
        return res;
    }
    
    public static int cutOffRank1(int cutOffRank, int num, int[] scores) {
        if(scores == null || scores.length == 0 || cutOffRank == 0) {
            return 0;
        }
        
        int[] count = new int[101]; // Since the 0<=scores[i]<=100, we can use the bucket sort
        for(int score: scores) {
            count[score]++;
        }
        
        int rank = 1;   // Since the rank starts from 1
        int res = 0;
        for(int i=100; i>=0; i--) {
            if(rank > cutOffRank) {
                break;
            }
            if(count[i] != 0) {
                res += count[i];
                rank = res + 1;
            }
        }
        return res;
        
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        int res = cutOffRank1(4, 5, new int[]{2, 2, 3, 4, 5});
        System.out.println(res);    // should be 5
        
        int res1 = cutOffRank1(3, 4, new int[]{100, 50, 50, 25});
        System.out.println(res1);
    }
}
```