`Trie`, also called `prefix tree`, is a special form of a `Nary tree`.


## What is Trie?
A `Trie` is a special form of a `Nary tree`. Typically, a trie is used to **store strings**. Each Trie node represents a string (`a prefix`).
Each node might have several children nodes while the paths to different children nodes represent different characters.

One important property of Trie is that all the descendants of a node have a common prefix of the string associated with that node. 
That's why Trie is also called `prefix tree`.

Trie is widely used in various applications, such as **autocomplete**, **spell checker**, etc. We will introduce the practical applications in later chapters.


## How to represent a Trie?
### 1. First Solution - Array
The first solution is to use an `array` to store children nodes.

For instance, if we store strings which only contains letter `a` to `z`, we can declare an array whose size is 26 in each node to store its children nodes. 
And for a specific character `c`, we can use `c - 'a'` as the index to find the corresponding child node in the array.
```java
class TrieNode {
    // change this value to adapt to different cases
    public static final N = 26;
    public TrieNode[] children = new TrieNode[N];
    
    // you might need some extra values according to different cases
};

/** Usage:
 *  Initialization: TrieNode root = new TrieNode();
 *  Return a specific child node with char c: root.children[c - 'a']
 */
```

It is really `fast` to visit a child node. It is comparatively `easy` to visit a specific child since we can easily transfer a character to an index in most cases. 
But not all children nodes are needed. So there might be some `waste of space`.

### 2. Second Solution - Map
The second solution is to use a `hashmap` to store children nodes.

We can declare a hashmap in each node. The key of the hashmap are characters and the value is the corresponding child node.
```java
class TrieNode {
    public Map<Character, TrieNode> children = new HashMap<>();
    
    // you might need some extra values according to different cases
};

/** Usage:
 *  Initialization: TrieNode root = new TrieNode();
 *  Return a specific child node with char c: root.children.get(c)
 */
```
It is even `easier` to visit a specific child directly by the corresponding character. But it might be a little `slower` than using an array. 
However, it `saves some space` since we only store the children nodes we need. It is also more `flexible` because we are not limited by a fixed length and fixed range.


## Basic Operations
### 1. Insertion in Trie
When we insert a target value into a BST, in each node, we need to decide which child node to go according to the relationship between `the value of the node` and `the target value`. 
Similarly, when we insert a target value into a Trie, we will also decide which path to go depending on `the target value` we insert.           
```pseudo-code
1. Initialize: cur = root
2. for each char c in target string S:
3.      if cur does not have a child c:
4.          cur.children[c] = new Trie node
5.      cur = cur.children[c]
6. cur is the node which represents the string S
```
Usually, you will need to build the trie by yourself. Building a trie is actually to call the insertion function several times. 
But remember to `initialize a root node` before you insert the strings.


### 2. Search in Trie
#### Search Prefix
As we mentioned in the introduction to Trie, all the descendants of a node have a common prefix of the string associated with that node. Therefore, it should be easy to search if there are any words in the trie that starts with the given prefix.

Similarly, we can go down the tree depending on the given prefix. Once we can not find the child node we want, search fails. Otherwise, search succeeds. 
```pseudo-code
1. Initialize: cur = root
2. for each char c in target string S:
3.      if cur does not have a child c:
4.          search fails
5.      cur = cur.children[c]
6. search successes
```

#### Search Word
You might also want to know how to search for a specific word rather than a prefix. We can treat this word as a prefix and search in the same way we mentioned above.

1. If search fails which means that no words start with the target word, the target word is definitely not in the Trie.
2. If search succeeds, we need to check if the target word is only a prefix of words in Trie or it is exactly a word. To solve this problem, you might want to modify the node structure a little bit.
    * Hint: A boolean flag in each node might work.


### 3. Implement Trie (Prefix Tree)
[208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
```java
class Trie {
    
    private TrieNode root;
    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode curr = root;
        for(char c: word.toCharArray()) {
            if(curr.next[c - 'a'] == null) {
                curr.next[c - 'a'] = new TrieNode();
            }
            curr = curr.next[c - 'a'];
        }
        curr.isWord = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode curr = root;
        for(char c: word.toCharArray()) {
            if(curr.next[c - 'a'] == null) {
                return false;
            }
            curr = curr.next[c - 'a'];
        }
        return curr.isWord;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        for(char c: prefix.toCharArray()) {
            if(curr.next[c - 'a'] == null) {
                return false;
            }
            curr = curr.next[c - 'a'];
        }
        return true;
    }
}

class TrieNode {
    boolean isWord;
    TrieNode[] next;
    
    public TrieNode() {
        isWord = false;
        next = new TrieNode[26];
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */
```

### 4. Implement Trie - Solution
The key to this problem is to design the Trie node structure. In order to know if the string represented by the node is a word or not, we need an extra `boolean flag`.


## Practical Application I


## Practical Application II
