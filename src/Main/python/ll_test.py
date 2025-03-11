class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

from LinkedListNode import LinkedListNode

def reverse_linked_list(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev    import unittest
    from LinkedListNode import LinkedListNode
    from LinkedListReversal import reverse_linked_list
    
    class TestLinkedListReversal(unittest.TestCase):
        def test_reverse_linked_list(self):
            # Create a sample Linked List: 1 -> 2 -> 3 -> 4 -> 5
            head = LinkedListNode(1)
            head.next = LinkedListNode(2)
            head.next.next = LinkedListNode(3)
            head.next.next.next = LinkedListNode(4)
            head.next.next.next.next = LinkedListNode(5)
    
            reversed_head = reverse_linked_list(head)
    
            # Check if the reversed Linked List is correct: 5 -> 4 -> 3 -> 2 -> 1
            self.assertEqual(reversed_head.value, 5)
            self.assertEqual(reversed_head.next.value, 4)
            self.assertEqual(reversed_head.next.next.value, 3)
            self.assertEqual(reversed_head.next.next.next.value, 2)
            self.assertEqual(reversed_head.next.next.next.next.value, 1)
    
    if __name__ == '__main__':
        unittest.main()