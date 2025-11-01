```python
class ListNode:
    __slots__ = ('key', 'val', 'prev', 'next')
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    """
    Design a Least-Recently-Used (LRU) cache that supports get() and put()
    in O(1) time.
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.head = ListNode(0, 0)   # dummy
        self.tail = ListNode(0, 0)   # dummy
        self.head.next, self.tail.prev = self.tail, self.head
        self.cache: dict[int, ListNode] = {}

    def _remove(self, node: ListNode) -> None:
        """Remove node from the doubly-linked list."""
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add_to_head(self, node: ListNode) -> None:
        """Insert node right after dummy head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
            return
        if self.size == self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
            self.size -= 1
        new_node = ListNode(key, value)
        self.cache[key] = new_node
        self._add_to_head(new_node)
        self.size += 1
```