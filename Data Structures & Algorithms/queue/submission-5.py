class Node:

    def __init__(self, val: int):
        self.val = val
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
        last_node = self.tail.prev

        new_node.next = self.tail
        new_node.prev = last_node

        last_node.next = new_node
        self.tail.prev = new_node        

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        new_node.next = first_node
        new_node.prev = self.head

        first_node.prev = new_node
        self.head.next = new_node 

    def pop(self) -> int:
        if self.isEmpty():
            return - 1

        node_to_remove = self.tail.prev
        elem = node_to_remove.val

        self.tail.prev = node_to_remove.prev
        node_to_remove.prev.next = self.tail

        return elem

    def popleft(self) -> int:
        if self.isEmpty():
            return - 1
            
        node_to_remove = self.head.next
        elem = node_to_remove.val

        self.head.next = node_to_remove.next
        node_to_remove.next.prev = self.head

        return elem
