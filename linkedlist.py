import unittest


class LinkedListNode(object):
    def __init__(self, prev, next):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.root = None
        self.tail = None

    def push_back(self, x):
        if self.tail is None:
            assert self.root is None
            self.root = self.tail = LinkedListNode(x, prev=None, next=None)
        elif self.root is self.tail:
            self.root.next = self.tail = LinkedListNode(x, prev=self.root, next=None)
        else:
            self.tail = LinkedListNode(x, prev=self.tail, next=None)

    def push_front(self, x):
        if self.root is None:
            assert self.tail is None
            self.root = self.tail = LinkedListNode(x, prev=None, next=None)
        elif self.root is self.tail:
            self.root = LinkedListNode(x, prev=None, next=self.tail)
        else:
            self.root = LinkedListNode(x, prev=None, next=self.root)

    def __iter__(self):
        cur = self.root
        while cur is not None:
            yield cur.value
            cur = cur.next


class TestLinkedList(unittest.TestCase):
    def test_default_constructor_is_empty_list(self):
        lst = LinkedList()
        self.assertEqual(list(iter(lst)), [])


if __name__ == '__main__':
    unittest.main()

        
        
        
        
