[Amazon | OA 2019 | Min Cost to Connect Ropes](https://leetcode.com/discuss/interview-question/344677)  

```java
class Solution {
    public static int minCost(List<Integer> ropes) {
        Queue<Integer> pq = new PriorityQueue<>(ropes);
        int totalCost = 0;
        while (pq.size() > 1) {
            int cost = pq.poll() + pq.poll();
            pq.add(cost);
            totalCost += cost;
        }
        return totalCost;
    }
}
```


```java
class Solution {
    public int connectSticks(int[] sticks) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        int res = 0;
        
        for(int stick: sticks) {
            queue.offer(stick);
        }
        
        while(queue.size() > 1) {
            int cost = queue.poll() + queue.poll();
            queue.offer(cost);
            res += cost;
        }
        return res;
    }
}
```



