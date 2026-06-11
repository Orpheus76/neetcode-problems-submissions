class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(-1)  # Dummy node
        self.tail = self.head  # Pointer

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0

        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next

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
        curr = self.head  # On commence au dummy node
        i = 0

        # On avance jusqu'au nœud PRÉCÉDANT l'index souhaité
        while curr and i < index:
            curr = curr.next
            i += 1

        # Conditions de validité :
        # 1. curr existe
        # 2. curr.next existe (c'est le nœud à supprimer)
        if curr and curr.next:
            # Si le noeud à supprimer est le tail, on recule le tail
            if curr.next == self.tail:
                self.tail = curr

            # On "saute" le noeud à supprimer
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
