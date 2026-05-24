class Node:
    def __init__(self, val: int):
        self.value = val
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = Node(-1)  # dummy node
        self.tail = Node(-1)  # dummy node
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        last_prev = self.tail.prev
        new_node = Node(value)

        last_prev.next = new_node
        new_node.prev = last_prev

        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        last_next = self.head.next
        new_node = Node(value)

        last_next.prev = new_node
        new_node.next = last_next

        new_node.prev = self.head
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        target = self.tail.prev  # Le noeud qu'on veut enlever
        val = target.value  # On sauvegarde sa valeur
        prev_node = target.prev  # Le noeud juste avant celui qu'on enlève

        # On fait "sauter" le noeud cible en reliant prev_node et tail
        prev_node.next = self.tail
        self.tail.prev = prev_node

        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        target = self.head.next
        val = target.value
        next_node = target.next

        next_node.prev = self.head
        self.head.next = next_node

        return val
