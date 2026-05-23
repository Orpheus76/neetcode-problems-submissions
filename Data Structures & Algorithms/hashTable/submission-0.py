class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # Initialize the table with None for each slot
        self.table = [None] * self.capacity

    def insert(self, key: int, value: int) -> None:
        index = key % self.capacity
        node = self.table[index]

        if not node:
            # Cas 1 : La case est vide
            self.table[index] = ListNode(key, value)
            self.size += 1

        else:
            # Cas 2 : Collision ou mise à jour
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev = node
                node = node.next
            # Si on arrive ici, la clé n'existait pas : on l'ajoute à la fin
            prev.next = ListNode(key, value)
            self.size += 1

        # Vérification du Load Factor (0.5)
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = key % self.capacity
        curr = self.table[index]

        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity
        curr = self.table[index]
        prev = None

        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[index] = curr.next  # On change la tête
                self.size -= 1
                return True
            prev = curr
            curr = curr.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        # 1. Sauvegarder l'ancien tableau et doubler la capacité
        old_table = self.table
        self.capacity *= 2
        self.size = 0  # On remet à 0 car insert() va l'incrémenter
        self.table = [None] * self.capacity

        # 2. Parcourir chaque emplacement de l'ancien tableau
        for node in old_table:
            # 3. Parcourir la liste chainée à cet emplacement
            curr = node
            while curr:
                # Ré-insérer chaque paire clé-valeur dans le nouveau tableau
                self.insert(curr.key, curr.value)
                curr = curr.next
