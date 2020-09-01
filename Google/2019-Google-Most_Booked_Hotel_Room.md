[Google | OA 2019 | Most Booked Hotel Room](https://leetcode.com/discuss/interview-question/421787/) 


To find which room is booked maximum number of times. Return the lexographically smaller room.

Analysis:
1. Use a `HashMap` to record the freq of each room.
2. We can also use an array: `3E` has index of `('E' - 'A') * 10 + 3`

[Playground - Google | OA 2019 | Most Booked Hotel Room](https://leetcode.com/playground/8oNR4w8H) 

```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static String getMaxFreqRooms(String[] floors) {
        int[] map = new int[260];
        int max = 0;
        String currMax = floors[0];
        
        for(int i=0; i<floors.length; i++) {
            String curr = floors[i];
            if(curr.charAt(0) == '-') {
                continue;
            }
            int idx = (curr.charAt(2) - 'A') * 10 + (curr.charAt(1) - '0');
            map[idx]++;
            if(map[idx] > max) {
                max = map[idx];
                currMax = curr;
            } else if(map[idx] == max) {
                currMax = currMax.compareTo(curr) < 0 ? currMax : curr;
            }
        }
        return currMax.substring(1);
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        // Example 1:
        String[] floors1 = {"+1A", "+3E", "-1A", "+4F", "+1A", "-3E"};
        System.out.println(getMaxFreqRooms(floors1));
    }
}
``` 

