[Amazon | OA 2020 | Maximum Units](https://leetcode.com/discuss/interview-question/793606/)

题意：
All of the products in the warehouse are in boxes of the same size. [所有产品都放在相同大小的 boxes 中。]         
Each product is packed in some number of unit per box. [每个产品以每箱一定数量的单位包装]       

Given the number of boxes the truck can hold, write an algorithm to determine the maximum of units of any mix of products that can be shipped. 


输入&输出：
Input:
* `num`: An integer representing number of products [代表 products 的个数]; 
* `boxes`: A list of integers representing the number of available boxes for products [每个 products 有几个箱子可以用];
* `unitSize`: An integer representing size of `unitPerBox` [每个箱子的 size];
* `unitsPerBox`: A list of integers representing the number of units packed in each box [每个箱子可以装多少个 unit 的 product];
* `truckSize`: An integer representing the number of **boxes** the truck can carry [].

Output:
* Return an integer representing the maximum units that can be carried by the truck.


Example:

    num = 3
    boxes = [1, 2, 3]
    unitSize = 3
    unitPerBox = [3, 2, 1]
    truckSize = 3
    
    * boxes = [1, 2, 3] : procut0 有 1 个箱子，product1 有 2 个箱子，product2 有 3 个箱子。
    * unitPerBox = [3, 2, 1] : 装 produt0 的箱子，每个箱子有 3 个 units；装 product1 的箱子，没给箱子有 2 个 units.
    * truckSize = 3 : truck can only hold 3 boxes.
    
    
分析(Analysis)：
题目既然要求 truck 可以装载最多的 units，那么首先按照 unitSize of per box 进行排序，首先装载 unit size 大的 box。
[Amazon - MaximumUnits](https://leetcode.com/playground/6ASjnouU)
```java
// "static void main" must be defined in a public class.
public class MaximumUnits {
    
    public static int maximumUnits(int num, List<Integer> boxes, int unitSize, List<Integer> unitsPerBox, int truckSize) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (b[1] - a[1])); // Sort by unitsPerBox, des
        for(int i=0; i<num; i++) {
            pq.offer(new int[]{boxes.get(i), unitsPerBox.get(i)});
        }
        
        int max = 0;
        while(truckSize > 0) {
            int[] cur = pq.remove();    // the box with the max unitsPerBox
            int box = cur[0];   // the number of boxes
            int units = cur[1]; // the units per box
            max += units * Math.min(truckSize, box);
            truckSize -= Math.min(truckSize, box);
        }
        return max;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        // =================================================================
        // Example 1
        // =================================================================
        int num1 = 3;
        List<Integer> boxes1 = Arrays.asList(1, 2, 3);
        List<Integer> unitsPerBox1 = Arrays.asList(3, 2, 1);
        int truckSize1 = 3;
        System.out.println(maximumUnits(num1, boxes1, 3, unitsPerBox1, truckSize1));
        
        // =================================================================
        // Example 2
        // =================================================================
        int num2 = 2;
        ArrayList<Integer> boxes2 = new ArrayList<>(List.of(2, 2));
        int unitSize2 = 2;
        ArrayList<Integer> unitsPerBox2 = new ArrayList<>(List.of(3, 2));
        int truckSize2 = 3;
        System.out.println(maximumUnits(num2, boxes2, 3, unitsPerBox2, truckSize2));
        
    }
}
```



