[turnstile](https://leetcode.com/discuss/interview-question/798231/)

Inputs:
1. `numCustomers` 
2. `arrTime`: A list of integers where the value at index `i` is the time in seconds when the ith customer will come to the turnstile, `arrTime[i]` 是 ith customer 到达的时间。
    * They are ordered by the time when they came to the turnstile, 到达的时间是已经排序的。  
3. `direction`: A list of integers where the value at index `i` is the direction of the ith customer, `direction[i]` 是 ith customer 的方向。

Requirements：
1. Passing through the turnstile takes 1 second, 
2. If the arrival time of two customers are equal:
    * If in the previous second the turnstile was not use (maybe it was used before, but not at the previous second), then the customer who wants to exit goes first，如果在此之前 turnstile 没有用，则 exit 有更高的优先级。
    * If in the previous second the turnstile was used as an exit/entrance, then the customer who wants to leave/enter goes first, 如果前一秒是 exit，则 exit 先走；如果前一秒是 enter，则 enter 先走。
3.

Example 1:
    
    numCustomers = 4
    arrTime = [0, 0, 1, 5]
    direction = [0, 1, 1, 0]
    
    output = [2, 0, 1, 5]
    
Explanation:
At time 0, `customer 0` wants to enter, `customer 1` wants to leave at the same time. Since the turnstile wat not used in the previous second, so the priority is on the side of `customer 1(exit)`.
At time 1, `customer 0` and `customer 1` want to pass through the turnstile. Since at time 0, the turnstile was exit, therefore `customer 2` will exit first.
At time 2, `customer 0` will enter.
At tiem 5, `customer 5` will enter.
Therefore, `output = [2, 0, 1, 5]`


Example 2:

    int[] arrTime2 = new int[]{0, 1, 1, 10, 15};
    int[] direction2 = new int[]{0, 1, 0, 0, 1};
    int[] expected2 = new int[]{0, 2, 1, 10, 15};

Analysis:
At time 0, `customer 0` enter first, then `status = 0`, `time = 1`
At time 1, `arrTime[1] = 1, dir=1`, `arrTime[2] = 1, dir=0`, `time = 1`, `status = 0` ==> `return -1` 
...


Example 3:

    int[] arrTime2 = new int[]{0, 2, 2, 10, 15};
    int[] direction2 = new int[]{0, 1, 0, 0, 1};
    int[] expected2 = new int[]{0, 2, 3, 10, 15};

Analysis:
At time 0, `customer 0` enter first, then `status = 0`, `time = 1`
At time 1, `arrTime[1] = 2, dir=1`, `arrTime[2] = 2, dir=0`, `time = 1`, `status = 0` ==> enter=1, exit=1, 
...

## Method 1. [wuxuanyi27](https://leetcode.com/discuss/interview-question/798231/Amazon-or-OA-2020-or-Turnstile/661481)
[leetcode - playground](https://leetcode.com/playground/new/empty)
1. `compare(int enter, int exit, int time, int status)`: 根据 customers 到达的时间、当前时间和前一秒 turnstile 的状态，确定 enter first / exit first。
    * 
```java
public class Turnstile {
    
    public static int compare(int enter, int exit, int time, int status) {
        enter -= time;
        exit -= time;
        if(enter < 0) {
            enter = 0;
        }
        if(exit < 0) {
            exit = 0;
        }
        if(enter < exit) {  // -1 means enter first
            return -1;
        }
        if(enter == exit) { // i.e. the arrTime[i] == exitTime[j]
            if(status == 1) {
                return 1;
            } else {
                return -1;
            }
        }
        return 1;
    }
    
    // https://leetcode.com/discuss/interview-question/798231/Amazon-or-OA-2020-or-Turnstile/661481
    public static int[] turnstile(int numCustomers, int [] arrTime, int [] direction){
        //1: exit, 0: enter
        int [] res = new int[numCustomers];
        Arrays.fill(res, -1);
        Queue<Pair<Integer, Integer>> exit = new LinkedList<>();
        Queue<Pair<Integer, Integer>> enter = new LinkedList<>();

        for(int i = 0; i < numCustomers; i++){
            if (direction[i] == 0){
                enter.offer(new Pair<>(i, arrTime[i]));
            }
            else {
                exit.offer(new Pair<>(i, arrTime[i]));
            }
        }

        int status = 1; //default exit
        int time = 0;

        while(!exit.isEmpty() && !enter.isEmpty()){
            int exitTime = exit.peek().getValue();
            int enterTime = enter.peek().getValue();
            if(time < Math.min(exitTime, enterTime)) {
                status = 1;
            }
            int comp = compare(enterTime, exitTime, time , status);
            if (comp == 1){     //exit pass
                int index = exit.peek().getKey();
                int val = exit.poll().getValue();
                res[index] = Math.max(time, val);
                time = Math.max(time, val) + 1;
                status = 1;
            } else {            //enter pass
                int index = enter.peek().getKey();  // i.e. index
                int val = enter.poll().getValue();  // enter time
                res[index] = Math.max(time, val);
                time = Math.max(time, val) + 1;
                status = 0;
            }
        }

        while(!exit.isEmpty()){
            int index = exit.peek().getKey();
            int val = exit.poll().getValue();
            res[index] = Math.max(time, val);
            time = Math.max(time, val) + 1;
            status = 1;
        }

        while(!enter.isEmpty()){
            int index = enter.peek().getKey();
            int val = enter.poll().getValue();
            res[index] = Math.max(time, val);
            time = Math.max(time, val) + 1;
            status = 0;
        }

        return res;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        /*
        * Example 1:
        */
        int[] arrTime1 = new int[]{0, 0, 1, 5};
        int[] direction1 = new int[]{0, 1, 1, 0};
        int[] expected1 = new int[]{2, 0, 1, 5};
        int[] output1 = turnstile(arrTime1.length, arrTime1, direction1);
        System.out.println("Example 1");
        for(int time: output1) {
            System.out.print(time + " ");
        }
        System.out.println();
        for(int time: expected1) {
            System.out.print(time + " ");
        }
        System.out.println("\n");
        
        /*
        * Example 2:
        */
        int[] arrTime2 = new int[]{0, 1, 1, 10, 15};
        int[] direction2 = new int[]{0, 1, 0, 0, 1};
        int[] expected2 = new int[]{0, 2, 1, 10, 15};
        int[] output2 = turnstile(arrTime2.length, arrTime2, direction2);
        System.out.println("Example 2");
        for(int time: output2) {
            System.out.print(time + " ");
        }
        System.out.println();
        for(int time: expected2) {
            System.out.print(time + " ");
        }
        System.out.println("\n");
 
        /*
        * Example 3:
        */
        int[] arrTime3 = new int[]{0, 2, 2, 10, 15};
        int[] direction3 = new int[]{0, 1, 0, 0, 1};
        int[] expected3 = new int[]{0, 2, 3, 10, 15};
        int[] output3 = turnstile(arrTime3.length, arrTime3, direction3);
        System.out.println("Example 3");
        for(int time: output3) {
            System.out.print(time + " ");
        }
        System.out.println();
        for(int time: expected3) {
            System.out.print(time + " ");
        }
        System.out.println("\n");
        
        /*
        * What if the first two arrive at the same time and both want to enter [0, 0, 1, 5] [0, 0, 1, 0]?
        * Example 4:
        */
        int[] arrTime4 = new int[]{0, 0, 1, 5};
        int[] direction4 = new int[]{0, 0, 1, 0};
        int[] expected4 = new int[]{0, 1, 2, 5};
        int[] output4 = turnstile(arrTime4.length, arrTime4, direction4);
        System.out.println("Example 4");
        for(int time: output4) {
            System.out.print(time + " ");
        }
        System.out.println();
        for(int time: expected4) {
            System.out.print(time + " ");
        }
        System.out.println("\n");
    }
}
```
