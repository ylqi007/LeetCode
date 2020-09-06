[Google | OA 2019 | Watering Flowers 2.0](https://leetcode.com/discuss/interview-question/394347/)

* Both of the watering cans are large enough to fully water any single plant.

## Method 1. Two Pointers
[Playground - Google | OA 2019 | Watering Flowers 2.0](https://leetcode.com/playground/Bn9sHVX5)
Key Points:
1. Corner case, i.e. `plants.length == 0`, return 0
2. Corner case, i.e. `plants.length == 1`, if `plants[0] <= Math.max(capacity1, capacity2)`, then just one refill is needed.
3. About the mid of an array:
    * `len / 2 == 0` ==> `[0, 1, 2, 3]`, `mid = len / 2 = 2`, then `left = [0, 2)` and `right = [2, len)`
        * `for(int i=0; i<len/2; i++) {}` and `for(int i=len-1; i>=mid; i--)`
    * `len / 2 == 1` ==> `[0, 1, 2, 3, 4]`, `mid = len / 2 = 2`, then `left = [0, 2)` and `right = [2+1, len)`, `mid = len / 2`
        * `for(int i=0; i<len/2; i++) {}` and `for(int i=len-1; i>=mid+1; i--)` 
4. According the length of array, adjust the position of middle point.
```java
// you can also use imports, for example:
// import java.util.*;
// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");
class WateringFlowers {
    public int waterFlowers(int[] plants, int capacity1, int capacity2) {
        // write your code in Java SE 8
        if(plants == null || plants.length == 0){
            return 0;
        }
        //To handle the case when there is exactly one plant with capacity = one of the two can's capacity 
        if(plants.length==1 && (plants[0] <= Math.max(capacity1, capacity1))){
            return 1;
        }
        
        //Water first half of the plants
        int count =2;
        int water_cap = capacity1;
        for(int i =0;i<plants.length/2;i++){
            
            //water when possible
            if(water_cap >= plants[i])
                water_cap -= plants[i];
            else{
                //increase the count and refill the can
                count++;
                water_cap = capacity1;
                water_cap -= plants[i];
                
            }
        }
        
        //Water second half of the plants
        int water_cap2 = capacity2;
        int x = plants.length/2;
        if(plants.length%2==0){
            x = (plants.length/2)-1;
        }
        for(int i =plants.length-1;i>x;i--){
            
            //water when possible
            if(water_cap2 >= plants[i])
                water_cap2 -= plants[i];
            else{
                //increase the count and refill the can
                count++;
                water_cap2 = capacity2;
                water_cap2 -= plants[i];
                
            }
        }
        
        //To check the middle flower
        if(plants.length%2 == 1){
            if(water_cap + water_cap2<plants[plants.length/2]){
                count++;
            }
        }
        
        return count;
    }

    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        int[] plants = {2, 4, 5, 1, 2};
        int capacity1 = 5;
        int capacity2 = 7;
        System.out.println(waterFlowers(plants, capacity1, capacity2));
    }
}
```


## Method 2. One Loop
[Playground - Google | OA 2019 | Watering Flowers 2.0_2](https://leetcode.com/playground/frUbdqUi)
```java
// "static void main" must be defined in a public class.
public class WateringFlowers {
    
    public static int waterFlowers(int[] plants, int capacity1, int capacity2) {
        if(plants == null || plants.length == 0) {
            return 0;
        }
        
        // To handle the case when there is exactly one plant with capacity
        if(plants.length == 1 && (plants[0] <= Math.max(capacity1, capacity2))) {
            return 1;
        }
        
        int count = 2;
        int waterCap1 = capacity1;
        int waterCap2 = capacity2;
        int i = 0;
        int j = plants.length - 1;
        while(i < j) {
            // Water from left if possible else refill and then water
            if(waterCap1 >= plants[i]) {
                waterCap1 -= plants[i];
            } else {
                waterCap1 = capacity1;  // refill
                waterCap1 -= plants[i];
                count++;
            }
            
            // Water from right if possible else refill and then water
            if(waterCap2 >= plants[j]) {
                waterCap2 -= plants[j];
            } else {
                waterCap2 = capacity2;  // refill
                waterCap2 -= plants[j];
                count++;
            }
            
            i++;
            j--;
        }
        
        // Process the middle one
        if(i == j) {
            if(waterCap1 + waterCap2 < plants[i]) {
                count++;
            }
        }
        return count;
        
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        // Example 1
        int[] plants = {2, 4, 5, 1, 2};
        int capacity1 = 5;
        int capacity2 = 7;
        System.out.println(waterFlowers(plants, capacity1, capacity2));
        
        // Example 2
        int[] plants2 = {2, 4, 5, 1};
        // int capacity1 = 5;
        // int capacity2 = 7;
        System.out.println(waterFlowers(plants2, capacity1, capacity2));
        
        // Example 3
        int[] plants3 = {2, 4, 6, 1, 2};
        // int capacity1 = 5;
        // int capacity2 = 7;
        System.out.println(waterFlowers(plants3, capacity1, capacity2));
    }
}
```




