class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        old_last = self.tail.prev

        new_node.prev = old_last
        new_node.next = self.tail
        old_last.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        next_node = self.head.next
        
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = next_node
        next_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return - 1

        target = self.tail.prev
        val = target.value

        before_target = target.prev
        before_target.next = self.tail
        self.tail.prev = before_target

        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return - 1

        target = self.head.next
        val = target.value

        after_target = target.next
        self.head.next = after_target
        after_target.prev = self.head

        return val
        
