[Largest Item Association](https://leetcode.com/discuss/interview-question/782606/)

题意：
* If an item `A` is ordered by a customer, then item `B` is also likely to be ordered by the same customer. []
* All items that are linked together by an item association can be considered to be in the same group.
* An item without any association to any other item can be considered to be in its own item association group of size 1.

要求：
* Output the largest item association group.
* If two groups have the same number of items then select the group which contains the item that appears first in the lexicographic order.


## [Java Solution: Works with more than one association per element](https://leetcode.com/discuss/interview-question/782606/Amazon-or-OA-2020-or-Largest-Item-Association/653137)
[LeetCode - Playground](https://leetcode.com/playground/new/empty)
```java
// "static void main" must be defined in a public class.
public class LargestItemAssociation {
    
    public List<String> largestItemAssociation(List<PairString> itemAssociation) {
        Map<String, List<String>> assomap = new HashMap<>();
        //Map with all items and child association of every item 1->2, 2-> , 3->4, 4->5 ,5->
        for(PairString p: itemAssociation) {
            if(!assomap.containsKey(p.first)) {
                assomap.put(p.first, new ArrayList<>());
            }
            assomap.get(p.first).add(p.second);
            if(!assomap.containsKey(p.second)) {
                assomap.put(p.second, new ArrayList<>());
            }
        }
        
        //DFS for every item: Resultant map 1->{5},{2} 2->{1,2},{4,5} 3->{3,4,5}
        Map<Integer, List<List<String>>> sizeMap = new HashMap<>();
        int maxAssoc = Integer.MIN_VALUE;
        for(String key: assomap.keySet()) {
            Queue<String> q = new LinkedList<>();
            TreeSet<String> tmp = new TreeSet<>();
            q.offer(key);
            while(!q.isEmpty()) {
                String head = q.poll();
                tmp.add(head);
                List<String> tail = assomap.get(head);
                for(String t: tail) {
                    q.offer(t);
                }
            }
            int size = tmp.size();
            maxAssoc = Math.max(maxAssoc, size);
            if(!sizeMap.containsKey(size)) {
                sizeMap.put(size, new ArrayList<>());
            }
            sizeMap.get(size).add(new ArrayList<>(tmp));
        }
        
        // Retrieve the maximum size lists and sort them lexiographically
        List<List<String>> maxAssocList = sizeMap.get(maxAssoc);
        
        Collections.sort(maxAssocList, new Comparator<List<String>>() {
            @Override
            public int compare(List<String> o1, List<String> o2) {
                int res = 0;
                for(int i=0; i<o1.size() && res==0; i++) {
                    res = o1.get(i).compareTo(o2.get(i));
                }
                return res;
            }
        });
        
        return maxAssocList.get(0);
    }
    
public static void main(String[] args) {
        LargestItemAssociation s = new LargestItemAssociation();
        /**
         * Example 1
         */
        List<PairString> input = Arrays.asList(
                new PairString[]{
                        new PairString("item1", "item2"),
                        new PairString("item3", "item4"),
                        new PairString("item4", "item5")
                }
        );
        /**
         * Testing equal sized arraylist. 1->2->3->7 4->5->6->7
         */
    List<PairString> input2 =  Arrays.asList(
         new PairString[] {
         new PairString("item1","item2"),
         new PairString("item2","item3"),
         new PairString("item4","item5"),
         new PairString("item6","item7"),
         new PairString("item5","item6"),
         new PairString("item3","item7")
                         }
     );
        List<String> lst = s.largestItemAssociation(input);
        for (String sa : lst) System.out.print(" " + sa);
        System.out.println();
        List<String> lst2 = s.largestItemAssociation(input2);
        for (String sa : lst2) System.out.print(" " + sa);
        System.out.println();
        /**
         * Testing duplicates: 1->2->3->7 , 5->6
         */
        List<PairString> input3 =  Arrays.asList(
                new PairString[] {
                        new PairString("item1","item2"),
                        new PairString("item1","item3"),
                        new PairString("item2","item7"),
                        new PairString("item3","item7"),
                        new PairString("item5","item6"),
                        new PairString("item3","item7")
                }
        );

        List<String> lst3 = s.largestItemAssociation(input3);
        for (String sa : lst3) System.out.print(" " + sa);
    }
}


class PairString {
    String first;
    String second;
    
    public PairString(String f, String s) {
        this.first = f;
        this.second = s;
    }
}
```


## [Java UnionFind, prabhjot2](https://leetcode.com/discuss/interview-question/782606/Amazon-or-OA-2020-or-Largest-Item-Association/653288)
[Largest Item Association, UF, 2](https://leetcode.com/playground/Zfd7tWrW)
```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static List<String> largestItemAssociation(List<PairString> itemAssociation) {
        UnionFind uf = new UnionFind(itemAssociation);  // Initialize
        for(PairString p: itemAssociation) {    // Union
            uf.union(p.first, p.second);
        }
        
        String largest = "";
        int max = Integer.MIN_VALUE;
        for(Map.Entry<String, Group> entry: uf.map.entrySet()) {
            if(entry.getValue().items.size() > max) {
                max = entry.getValue().items.size();
                largest = entry.getKey();
            } else if(entry.getValue().items.size() == max) {
                String key = String.join("", uf.map.get(largest).items);
                if(String.join("", uf.map.get(entry.getKey()).items).compareTo(key) < 0) {
                    largest = entry.getKey();
                }
            }
        }
        
        return uf.map.get(largest).items;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        /**
         * Example 1: 3 -> 4 -> 5
         */
        List<PairString> input1 = Arrays.asList(
            new PairString[]{
                new PairString("Item1", "Item2"),
                new PairString("Item3", "Item4"),
                new PairString("Item4", "Item5")
            }
        );
		System.out.println(largestItemAssociation(input1));
        
        /**
         * Testing equal sized arraylist. 1->2->3->7 4->5->6->7
         */
        List<PairString> input2 =  Arrays.asList(
            new PairString[] {
                new PairString("item1","item2"),
                new PairString("item2","item3"),
                new PairString("item4","item5"),
                new PairString("item6","item7"),
                new PairString("item5","item6"),
                new PairString("item3","item7")
             }
        );
        System.out.println(largestItemAssociation(input2));
        
        /**
         * Testing duplicates: 1->2->3->7 , 5->6
         */
        List<PairString> input3 =  Arrays.asList(
            new PairString[] {
                new PairString("item1","item2"),
                new PairString("item1","item3"),
                new PairString("item2","item7"),
                new PairString("item3","item7"),
                new PairString("item5","item6"),
                new PairString("item3","item7")
            }
        );
        System.out.println(largestItemAssociation(input3));

        /**
         * Testing duplicates: 1->2->3->7 , 5->6
         */
        List<PairString> input4 =  Arrays.asList(
            new PairString[] {
                new PairString("item3","item4"),
                new PairString("item1","item2"),
                new PairString("item5","item6"),
                new PairString("item4","item5"),
                new PairString("item2","item7"),
                new PairString("item7","item8"),
                new PairString("item2","item3"),
                new PairString("item6","item7"),
                new PairString("item0","item2"),
            }
        );
        System.out.println(largestItemAssociation(input4));

    }
}


class PairString {
    String first;
    String second;
    
    PairString(String f, String s) {
        this.first = f;
        this.second = s;
    }
}


class Group {
    String parent;
    List<String> items;
    
    public Group(String parent) {
        this.parent = parent;
        this.items = new ArrayList<>();
    }
}

class UnionFind {
    Map<String, Group> map = new HashMap<>();
    
    public UnionFind(List<PairString> pairs) {
        for(PairString pair: pairs) {
            Group first = new Group(pair.first);
            Group second = new Group(pair.second);

            first.items.add(pair.first);
            second.items.add(pair.second);
            
            map.put(pair.first, first);
            map.put(pair.second, second);
        }
    }
    
    public void union(String a, String b) {
        String parA = find(a);
        String parB = find(b);
        
        if(!parA.equals(parB)) {
            map.get(parB).parent = parA;
            map.get(parA).items.addAll(map.get(parB).items);
        }
    }
    
    public String find(String a) {
        if(map.get(a).parent.equals(a)) {
            return a;
        }
        
        return find(map.get(a).parent);
    }
}
```

## [Java solution using union-find. fmrailgun](https://leetcode.com/discuss/interview-question/782606/Amazon-or-OA-2020-or-Largest-Item-Association/653222)
```java
// "static void main" must be defined in a public class.
public class Main {
    
    public static List<String> largestItemAssociation(List<PairString> itemAssociation) {
        List<String> res = new ArrayList<String>();
        if(itemAssociation == null || itemAssociation.size() == 0) {
            return res;
        }
        
        UnionFind uf = new UnionFind();
        for(PairString p: itemAssociation) {
            uf.union(p.first, p.second);
        }
        
        // print map
        for(Map.Entry<String, Node> entry: uf.map.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue().boss);
        }
        System.out.println();
        return uf.largestComponent;
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        Main s = new Main();
        /**
         * Example 1
         */
        List<PairString> input = Arrays.asList(
                new PairString[]{
                        new PairString("item1", "item2"),
                        new PairString("item3", "item4"),
                        new PairString("item4", "item5")
                }
        );
        List<String> lst = s.largestItemAssociation(input);
        for (String sa : lst) System.out.print(" " + sa);
        System.out.println();
        /**
         * Testing equal sized arraylist. 1->2->3->7 4->5->6->7
         */
        List<PairString> input2 =  Arrays.asList(
             new PairString[] {
             new PairString("item1","item2"),
             new PairString("item2","item3"),
             new PairString("item4","item5"),
             new PairString("item6","item7"),
             new PairString("item5","item6"),
             new PairString("item3","item7")
                 }
         );
        // List<String> lst = s.largestItemAssociation(input);
        // for (String sa : lst) System.out.print(" " + sa);
        // System.out.println();
        List<String> lst2 = s.largestItemAssociation(input2);
        for (String sa : lst2) System.out.print(" " + sa);
        System.out.println();
    }
}


class PairString {
    String first;
    String second;
    
    public PairString(String first, String second) {
        this.first = first;
        this.second = second;
    }
}


class Node {
    String item;
    String boss;
    int size;
    LinkedList<String> component;
    
    Node(String s) {
        item = s;
        boss = s;
        size = 1;
        component = new LinkedList<>();
        component.add(s);
    }
}


class UnionFind {
    Map<String, Node> map;
    int maxSize;
    List<String> largestComponent;
    
    UnionFind() {
        map = new HashMap<>();
        maxSize = 0;
        largestComponent = new LinkedList<>();
    }
    
    public void union(String item1, String item2) {
        if(!map.containsKey(item1)) {
            map.put(item1, new Node(item1));
        }
        if(!map.containsKey(item2)) {
            map.put(item2, new Node(item2));
        }
        
        if(isConnected(item1, item2) || item1.equals(item2)) {
            return;
        }
        
        Node boss1 = map.get(find(item1));
        Node boss2 = map.get(find(item2));
        // Always choose lexicographically smaller item to be the boss of connected component
        if(boss1.component.get(0).compareTo(boss2.component.get(0)) < 0) {
            connect(boss1, boss2);
        } else {
            connect(boss2, boss1);
        }
    }
    
    public void connect(Node n1, Node n2) {
        n1.size += n2.size;
        n1.component.addAll(n2.component);
        n2.component = null;    // for saving space
        n2.boss = n1.item;
        
        if(n1.size > maxSize) {
            maxSize = n1.size;
            largestComponent = n1.component;
        } else if(n1.size == maxSize) {
            // if new component is the same size but lexicographically smaller, update
            if(largestComponent.get(0).compareTo(n1.component.get(0)) > 0) {
                largestComponent = n1.component;
            }
        }
    }
    
    public boolean isConnected(String s1, String s2) {
        String boss1 = find(s1);
        String boss2 = find(s2);
        
        return boss1.equals(boss2);
    }
    
    public String find(String item) {
        Node node = map.get(item);
        while(!node.boss.equals(node.item)) {
            node = map.get(node.boss);
        }
        Node tail = map.get(item);
        while(!tail.boss.equals(node.item)) {
            String next = tail.boss;
            tail.boss = node.item;
            tail = map.get(next);
        }
        return node.item;
    }
       
}
```


## 
https://leetcode.com/discuss/interview-question/782606/Amazon-or-OA-2020-or-Largest-Item-Association/653222
