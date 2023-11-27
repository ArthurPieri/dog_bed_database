# Trees

## Types of Trees

### Binary Search Tree

- Each node has at most 2 children
- Left child is less than parent
- Right child is greater than parent
- No duplicates

### AVL Tree

- Self-balancing binary search tree
- Height of left and right subtrees of any node differ by at most 1
- Insertion and deletion operations may cause the tree to become unbalanced

### Red-Black Tree

- Self-balancing binary search tree
- Each node is either red or black
- Root node is always black
- New nodes are always red
- No two adjacent red nodes
- Every path from a node to a null node has the same number of black nodes

### B-Tree

- Self-balancing tree
- Each node can have more than 2 children
- Used in databases and file systems
- Each node contains a list of keys and a list of children
- Keys are sorted in ascending order
- Keys in the left child are less than the keys in the parent node
- Keys in the right child are greater than the keys in the parent node
- All leaves are at the same level

### Splay Tree

- Self-balancing binary search tree
- Recently accessed nodes are moved closer to the root
- Used in caches and memory allocators

## Big O Notation

| Tree | Insert | Search |
| --- | --- | --- |
| BST | O(log n) | O(n) |
| AVL | O(log n) | O(log n) |
| RBT | O(log n) | O(log n) |
| B-tree| O(log n) | O(log n) |
| Splay | O(log n) | O(log n) |

## AVL vs RedBlack

| AVL | RedBlack |
| --- | --- |
| More rigid | More flexible |
| Faster searching | Faster insertion |
| Slower insertion | Slower searching |
| Used in databases | Used in libraries |
