class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next  # On saute le dummy node
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

        if new_node.next is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        while i < index and curr:
            curr = curr.next
            i += 1

        # Si le noeud existe et qu'il y a un noeud après lui à supprimer
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
            res.append(curr.value)
            curr = curr.next

        return res
