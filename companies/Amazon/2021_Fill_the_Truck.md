[1710. Maximum Units on a Truck](https://leetcode.com/problems/maximum-units-on-a-truck/)


## Method 1. Using Array Sort
Key Points:
1. Try to fill the truck with the boxes which have the largest number of units.

```java
class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        Arrays.sort(boxTypes, (a, b) -> (b[1] - a[1])); // Descending order according to units in each type of box
        int unitCount = 0;
        for(int[] boxType: boxTypes) {
            int boxCount = Math.min(truckSize, boxType[0]); // How many box positions left for box
            unitCount += boxCount * boxType[1];
            truckSize -= boxCount;
            if(truckSize == 0) {
                break;
            }
        }
        return unitCount;
    }
}
```

Complexity Analysis:
1. Time Complexity : `O(nlogn)`, where `n` is the number of elements in array boxTypes.
Sorting the array boxTypes of size `n` takes `(nlogn)` time. Post that, we iterate over each
element in array boxTypes and in worst case, we might end up iterating over all the elements in
the array. This gives us time complexity as `O(nlogn)+O(n)=O(nlogn)`.  
2. Space Complexity: `O(1)`, as we use constant extra space.


## Method 2. Using Priority Queue
There is yet another way to get the maximum units in constant time by using the Heap data
 structure. We could build Max Heap where the value at the root node of the heap is always the
  maximum value among all its children. So we could build a max heap based on the number of units.  

```java
class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        PriorityQueue<int[]> queue = new PriorityQueue<>((a, b) -> (b[1] - a[1]));
        queue.addAll(Arrays.asList(boxTypes));
        int unitCount = 0;
        while(!queue.isEmpty()) {
            int[] top = queue.poll();
            int boxCount = Math.min(truckSize, top[0]);
            unitCount += boxCount * top[1];
            truckSize -= boxCount;
            if(truckSize == 0) {
                break;
            }
        }
        return unitCount;
    }
}
```

Complexity Analysis
1. Time Complexity : `O(nlogn)`, where `n` is the number of elements in array boxTypes.
We are adding all the elements of the array boxTypes in the priority queue, which takes `O(n)` time.
Post that, we would continue iteration until queue is not empty or remaining truck size is
greater than 0. In worst case, we might end up iterating nnn times. Also, removing elements from
queue would take `(logn)` time. This gives us time complexity as `O(nlogn)+O(n)=O(nlogn)`.
2. Space Complexity: `O(n)`, as we use a queue of size `n`.


## Method 3. [counting/bucket sort O(n) - faster than 100%.](https://leetcode.com/problems/maximum-units-on-a-truck/discuss/1000343/countingbucket-sort-O(n)-faster-than-100)
Key Points:
1. Create an array where the indices represent the units and the values represents the number of
 boxes with indices of boxes. For example, `arr[10] = 19` represents that there are 19 boxes with
  units 10.
```java
class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        int[] buckets = new int[1001];
        int res = 0;
        for(int[] box: boxTypes) {
            buckets[box[1]] += box[0];  // there are buckets[i] boxes which has unit i
        }
        
        for(int i=buckets.length-1; i>=0; i--) {
            if(buckets[i] == 0) {   // No boxes with units i
                continue;
            }
            int boxCount = Math.min(truckSize, buckets[i]);
            res += boxCount * i;
            truckSize -= boxCount;
            if(truckSize == 0) {
                break;
            }
        }
        return res;
    }
}
```
Complexity:
1. Time: O(n)
2. space: O(1001)=O(1). we create an array of 1001 buckets.
