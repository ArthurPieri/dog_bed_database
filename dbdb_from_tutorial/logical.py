"""
    Defines the logical layer. It's an abstract interface to a key/value store.
    - LogicalBase: provides the API for logical updates (like get, set and commit) 
     and defers to a concrete subclass to implement the updates themselves. 
     It also manages storage locking and dereferencing internal nodes
    - ValueRef: is a Python object that refers to a binary blob stored in the database
     The indirection lets us avoid loading the entire data store into memory all at once.
"""
class LogicalBase(object):
    # ...
    def get(self, key):
        # if not self._storage.locked:
        #     self._refresh_tree_ref()
        # return self._get(self._follow(self._tree_ref), key)
        ...

    def _refresh_tree_ref(self):
        # self._tree_ref = self.node_ref_class(
        #     address=self._storage.get_root_address())
        ...
    
    