[Amazon | OA 2020 | Nearest City](https://leetcode.com/discuss/interview-question/872961/Amazon-or-OA-2020-or-Nearest-City)

Return a list of strings representing the name of the nearest city that shares either an x or a y coordinate with the queried city.

## Method 1. [HashMap + TreeMap](https://leetcode.com/discuss/interview-question/872961/Amazon-or-OA-2020-or-Nearest-City/791267)
Key Points:
1. Use the HashMap to store the cities which share the same x or y coordinates;
2. Use the TreeMap to sort the distance.
3. Sort: first by distance, then by alphabet

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.TreeSet;

class City {
   String name;
   int x;
   int y;
}

public class NearestCities {
    // First by y; if there have the same y, then by name
    public static Comparator<? super City> Y_COMPARATOR = (a, b) -> {
        int v = Integer.compare(a.y, b.y);
        if (v == 0) {
            v = a.name.compareTo(b.name);
        }
        
        return v;
    };
    
    // First by x; if there have the same x, then by name
    public static Comparator<? super City> X_COMPARATOR = (a, b) -> {
        int v = Integer.compare(a.x, b.x);
        if (v == 0) {
            v = a.name.compareTo(b.name);
        }
        
        return v;
    };

   public static String[] findNearestCities(int numOfPoints, String[] points, int[] xCoordinates, int[] yCoordinates, int numOfQueries, String[] queries) {
      HashMap<Integer, TreeSet<City>> xToYs = new HashMap<>();  // cities sharing the same x; use TreeMap to store this cities and sort by y in ascending order 
      HashMap<Integer, TreeSet<City>> yToXs = new HashMap<>();  // Share the same y
      HashMap<String, City> nameToCity = new HashMap<>();       // city name -> city location (x, y)

      for (int i = 0; i < numOfPoints; i++) { // O(p log(p))
         City c = new City();
         c.name = points[i];
         c.x = xCoordinates[i];
         c.y = yCoordinates[i];

         // Add to maps
         nameToCity.put(c.name, c);
         xToYs.putIfAbsent(c.x, new TreeSet<>(Y_COMPARATOR));   // TreeSet is ordered set, and the order key is Y, then name of city
         xToYs.get(c.x).add(c); // O (log p) in adding to TreeSet
         yToXs.putIfAbsent(c.y, new TreeSet<>(X_COMPARATOR));
         yToXs.get(c.y).add(c); // O (log p) in adding to TreeSet
      }

      String[] result = new String[numOfQueries];
      for (int i = 0; i < numOfQueries; i++) { // O (q log p)
         City c = nameToCity.get(queries[i]);
         if (c == null)
            continue;

         ArrayList<City> neighbors = new ArrayList<City>(); 
         neighbors.add(xToYs.get(c.x).lower(c));    // O(log p)
         neighbors.add(xToYs.get(c.x).higher(c));   // O(log p)
         neighbors.add(yToXs.get(c.y).lower(c));    // O(log p)
         neighbors.add(yToXs.get(c.y).higher(c));   // O(log p)

         result[i] = getClosestCity(c, neighbors);  // At max 4 so O(1)

      }
      return result;
   }

   private static String getClosestCity(City origin, List<City> neighbors) {
      City closestCity = null;
      int closestDistance = Integer.MAX_VALUE;
      for (City c : neighbors) {
         if (c != null) {
            int d = getDistance(origin, c);
            if (d < closestDistance) {
               closestCity = c;
               closestDistance = d;
            }
         }
      }

      return closestCity != null ? closestCity.name : null;
   }

   private static int getDistance(City a, City b) {
      return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
   }

   public static void test(int numOfPoints, String[] points, int[] xCoordinates, int[] yCoordinates, int numOfQueries,
         String[] queries) {
      String[] out = findNearestCities(numOfPoints, points, xCoordinates, yCoordinates, numOfQueries, queries);
      System.out.println(Arrays.toString(out));
   }

   public static void runner() {
      System.out.println("NearestCities");
      test(3, new String[] { "c1", "c2", "c3" }, new int[] { 3, 2, 1 }, new int[] { 3, 2, 3 }, 3,
            new String[] { "c1", "c2", "c3" });
      test(5, new String[] { "p1", "p2", "p3", "p4", "p5" }, new int[] { 10, 20, 30, 40, 50 },
            new int[] { 10, 20, 30, 40, 50 }, 5, new String[] { "p1", "p2", "p3", "p4", "p5" });
      test(5, new String[] { "p1", "p2", "p3", "p4", "p5" }, new int[] { 10, 20, 10, 40, 50 },
            new int[] { 10, 20, 10, 10, 50 }, 5, new String[] { "p1", "p2", "p3", "p4", "p5" });
   }
}
```

Total time to get the closest neighbor for all cities: O(N log N). N is the cities count.
Adding all cities into TreeSet needs O(NlogN) + k*O(1)


## Method 2. HashMap + TreeMap
```java
// "static void main" must be defined in a public class.
public class NearestCities {

    public static String[] nearestDistance1(String[] cities, int[] xs, int[] ys, String[] queries) {
        String[] res = new String[queries.length];
        Map<Integer, TreeMap<Integer, String>> xMap = new HashMap<>();  // share the same x
        Map<Integer, TreeMap<Integer, String>> yMap = new HashMap<>();  // share the same y
        Map<String, int[]> nodeMap = new HashMap<>();   // city name ==> city's position
        
        for(int i=0; i<cities.length; i++) {    // Initialization, 
            nodeMap.put(cities[i], new int[]{xs[i], ys[i]});    // city i and its xy position
            xMap.putIfAbsent(xs[i], new TreeMap<>());
            yMap.putIfAbsent(ys[i], new TreeMap<>());
            xMap.get(xs[i]).put(ys[i], cities[i]);  // x --> y --> city name
            yMap.get(ys[i]).put(xs[i], cities[i]);  // y --> x --> city name
        }
        
        for(int i=0; i<queries.length; i++) {
            int[] node = nodeMap.get(queries[i]);   // the node need to query
            TreeMap<Integer, String> ym = xMap.getOrDefault(node[0], new TreeMap<>());  // share the same x, i.e. ys with the same x
            TreeMap<Integer, String> xm = yMap.getOrDefault(node[1], new TreeMap<>());  // xs with the same y
            Integer yl = ym.lowerKey(node[1]);
            Integer yh = ym.higherKey(node[1]);
            Integer xl = xm.lowerKey(node[0]);
            Integer xh = xm.higherKey(node[0]);
            int dist = Integer.MAX_VALUE;
            if(yl != null && Math.abs(yl - node[1]) <= dist) {
                // if res[i] == null, then use ym.get(yl) directly
                // if res[i] != null, then use the 
                if(Math.abs(yl - node[1]) < dist) {
                    res[i] = ym.get(yl);
                    dist = Math.abs(yl - node[1]);
                } else {    // i.e. Math.abs(yl - node[1]) == dist
                    res[i] = (res[i] == null) ? ym.get(yl) : res[i].compareTo(ym.get(yl)) > 0 ? ym.get(yl) : res[i];
                }
            }
            if(yh != null && Math.abs(yh - node[1]) <= dist) {
                if(Math.abs(yh - node[1]) < dist) {
                    res[i] = ym.get(yh);
                    dist = Math.abs(yh - node[1]);
                } else {
                    res[i] = (res[i] == null) ? ym.get(yh) : res[i].compareTo(ym.get(yh)) > 0 ? ym.get(yh) : res[i];
                }
            }
            if(xl != null && Math.abs(xl - node[0]) <= dist) {
                if(Math.abs(xl - node[0]) < dist) {
                    res[i] = xm.get(xl);
                    dist = Math.abs(xl - node[0]);
                } else {
                    res[i] = (res[i] == null) ? xm.get(xl) : res[i].compareTo(xm.get(xl)) > 0 ? xm.get(xl) : res[i];
                }
            }
            if(xh != null && Math.abs(xh - node[0]) <= dist) {
                if(Math.abs(xh - node[0]) < dist) {
                    res[i] = xm.get(xh);
                    dist = Math.abs(xh - node[0]);
                } else {
                    res[i] = (res[i] == null) ? xm.get(xh) : res[i].compareTo(xm.get(xh)) > 0 ? xm.get(xh) : res[i];
                }
            }
            // if(res[i] == null) {
            //     res[i] = "None";
            // }
        }
        return res;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        String[] cities1 = {"c1", "c2", "c3"};
        int[] xs = {3, 2, 1};
        int[] ys = {3, 2, 3};
        String[] queries = {"c1", "c2", "c3"};
        System.out.println(Arrays.toString(nearestDistance1(cities1, xs, ys, queries)));
    }
}
```