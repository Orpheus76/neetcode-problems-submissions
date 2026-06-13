
class Node:

    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        # Dummy Nodes
        self.head = Node(-1)
        self.tail = Node(-1)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        
        target = self.tail.prev
        
        self.tail.prev = new_node
        new_node.prev = target
        new_node.next = self.tail
        target.next = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        
        target = self.head.next
        
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = target
        target.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return - 1
        
        previous = self.tail.prev
        value = previous.val

        self.tail.prev = previous.prev
        previous.prev.next = self.tail

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return - 1

        previous = self.head.next
        value = previous.val

        self.head.next = previous.next
        previous.next.prev = self.head

        return value
