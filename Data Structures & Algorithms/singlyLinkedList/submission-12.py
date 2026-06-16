class Node:
    def __init__(self, val: int):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(-1)  # Dummy Node
        self.tail = self.head  # Pointer

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr:
            if i == index:
                return curr.value

            curr = curr.next
            i += 1

        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)

        new_node.next = self.head.next
        self.head.next = new_node

        if new_node.next == None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)

        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        while curr and i < index:
            curr = curr.next
            i += 1

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr

            curr.next = curr.next.next
            return True

        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []

        while curr:
            res.append(curr.value)
            curr = curr.next
        return res
