"""
    Defines a concrete binary tree algorithm underneath the logical interface
    - BinaryTree: provides a concrete implementation of a binary tree,
     with methods for getting, inserting and deleting key/value pairs.
    - BinaryTree: representes an immutable tree; 
     updates are performed by returning a new tree which shares common structure with the old one.
    - BinaryNode: implements a node in the binary tree.
    - BinaryNodeRef: is a specialised ValueRef which knows how to 
     serialise and deserialise a BinaryNode.
"""

class BinaryTree():# (LogicalBase):
# ...
    # def _get(self, node, key):
    #     while node is not None:
    #         if key < node.key:
    #             node = self._follow(node.left_ref)
    #         elif node.key < key:
    #             node = self._follow(node.right_ref)
    #         else:
    #             return self._follow(node.value_ref)
    #     raise KeyError
        ...