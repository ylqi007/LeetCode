[Amazon | OA 2019 | Distance Between Nodes in BST](https://leetcode.com/discuss/interview-question/376375/)


```java
// "static void main" must be defined in a public class.
public class Main {
    
    public int bstDistance(int[] nums, int node1, int node2) {
        TreeNode root = buildBST(nums, node1, node2);
        if(root == null) {
            return -1;
        }
        TreeNode lca = lca(root, node1, node2); // least common ancestor
        return getDistance(lca, node1) + getDistance(lca, node2);
    }
    
    public TreeNode buildBST(int[] nums, int node1, int node2) {
        TreeNode root = null;
        boolean found1 = false;
        boolean found2 = false;
        for(int val: nums) {
            if(val == node1) found1 = true;
            if(val == node2) found2 = true;
            
            TreeNode node = new TreeNode(val);
            if(root == null) {
                root = node;
                continue;
            }
            addToBST(root, node);   // Add node to BST
        }
        if(!found1 || !found2) {
            return null;
        }
        return root;
    }
    
    private void addToBST(TreeNode root, TreeNode node) {
        for(TreeNode curr = root; true; ) {
            if(node.val < curr.val) {
                if(curr.left == null) {
                    curr.left = node;
                    break;  // i.e. return
                } else {
                    curr = curr.left;
                }
            } else {
                if(curr.right == null) {
                    curr.right = node;
                    break;
                } else {
                    curr = curr.right;
                }
            }
        }
    }
    
    // Find the lowest common ancestor
    private TreeNode lca(TreeNode root, int node1, int node2) {
        while(true) {
            if(node1 < root.val && node2 < root.val) {
                root = root.left;
            } else if(root.val < node1 && root.val < node2) {
                root = root.right;
            } else {
                return root;
            }
        }
    }
    
    private int getDistance(TreeNode src, int dest) {
        if(src.val == dest) {
            return 0;
        }
        TreeNode node = src.left;
        if(src.val < dest) {
            node = src.right;
        }
        return 1 + getDistance(node, dest);
    }
    
    public static void main(String[] args) {
        System.out.println("Hello World!");
        
        Main obj = new Main();
        
        // Example
        int[] nums1 = {2, 1, 3};
        System.out.println(obj.bstDistance(nums1, 1, 3));
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    public TreeNode(int v) {
        this.val = v;
        this.left = null;
        this.right = null;
    }
}
```

Complexity:
1. Time complexity: O(n * h), where n is the number of nodes and h is the height of the tree. In the worst case tree is not balanced (elements are already in sorted order) and complexity will be O(n^2).
2. Space complexity: O(n).

