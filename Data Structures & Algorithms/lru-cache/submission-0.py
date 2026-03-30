class LRUCache:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = self.prev = None


    def __init__(self, capacity: int):
        self.cap = capacity
        self.node_map = {}
        self.dhead = self.Node(0,0)
        self.dtail = self.Node(0,0)

        self.dhead.next = self.dtail
        self.dtail.prev = self.dhead


    def _remove_from_dll(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_front(self, node):
        temp = self.dhead.next
        self.dhead.next = node
        node.prev = self.dhead
        node.next = temp
        temp.prev = node


   
    def get(self, key: int) -> int:
        if key in self.node_map:
            temp = self.node_map[key]
            self._remove_from_dll(temp)
            self._add_to_front(temp)
            return temp.val
        else: return -1
    

    
        

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            temp = self.node_map[key]
            temp.val = value
            self._remove_from_dll(temp)
            self._add_to_front(temp)
        else:
            if len(self.node_map) == self.cap:
                lru = self.dtail.prev
                self._remove_from_dll(lru)
                del self.node_map[lru.key]
            
            n = self.Node(key, value)
            self.node_map[key] = n
            self._add_to_front(n)