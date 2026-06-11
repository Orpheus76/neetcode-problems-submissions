class Node:

    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        # On crée deux sentinelles (dummy nodes) pour simplifier les insertions/suppressions
        self.head = Node(-1)    
        self.tail = Node(-1)    
        # On les connecte entre eux 
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        
        last = self.tail.prev

        last.next = new_node
        new_node.prev = last
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        
        first = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first
        first.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        # Le nœud à supprimer est juste avant tail
        target = self.tail.prev
        val = target.val
        
        # On reconnecte l'avant-dernier nœud avec tail
        before_target = target.prev
        before_target.next = self.tail
        self.tail.prev = before_target
        
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        target = self.head.next
        val = target.val

        after_target = target.next
        self.head.next = after_target
        after_target.prev = self.head

        return val
