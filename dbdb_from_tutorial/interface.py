"""
    defines a class (DBDB) which implements the Python dictionary API using the concrete BinaryTree implementation.
    This is how you'd use DBDB inside a python program
"""
class DBDB(object):
    def __init__(self, f):
        # TODO: implement storage
        # self._storage = Storage(f)
        # TODO: implement binary tree
        # self._tree = BinaryTree(self._storage.get_root_address())
        ...

    def __getitem__(self, key):
        # self._assert_not_closed()
        # return self._tree.get(key)
        ...

    def _assert_not_closed(self):
        #if self._storage.closed:
            #raise ValueError('Database closed.')
        ...