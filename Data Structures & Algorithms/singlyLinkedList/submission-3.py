class Node:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:

        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        
        return - 1


    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head.next
        self.head.next = new_head

        if new_head.next == None:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = Node(val)
        self.tail.next = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False


    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res