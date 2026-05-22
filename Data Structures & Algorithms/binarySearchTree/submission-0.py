class Node:
    
    def __init__(self, key: int, val: int):
        self.left = None
        self.right = None
        self.key = key
        self.value = val


class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = Node(key, val)
            return
        
        curr = self.root
        while True:
            if key < curr.key:
                if curr.left is None:
                    curr.left = Node(key, val)
                    return
                curr = curr.left

            elif key > curr.key:
                if curr.right is None:
                    curr.right = Node(key, val)
                    return
                curr = curr.right

            else:
                # La clé existe déjà, on met à jour la valeur
                curr.value = val
                return

    def get(self, key: int) -> int:
        if not self.root:
            return - 1
        
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            
            elif key > curr.key:
                curr = curr.right
            
            else:
                return curr.value
        
        return -1


    def getMin(self) -> int:
        if not self.root:
            return -1

        curr = self.root
        while curr.left:
            curr = curr.left

        return curr.value


    def getMax(self) -> int:
        if not self.root:
            return -1
        
        curr = self.root
        while curr.right:
            curr = curr.right
        
        return curr.value


    def remove(self, key: int) -> None:
        self.root = self._removeHelper(self.root, key)
    
    def _removeHelper(self, curr, key):
        if not curr:
            return None
        
        if key < curr.key:
            curr.left = self._removeHelper(curr.left, key)
        
        elif key > curr.key:
            curr.right = self._removeHelper(curr.right, key)
        
        else:
             # Cas 1 & 2 : Zéro ou un enfant
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left

            # Cas 3 : Deux enfants
            # On cherche le min du côté droit
            min_node = curr.right
            while min_node.left:
                min_node = min_node.left
            
            curr.key = min_node.key
            curr.value = min_node.value

            # On supprime le noeud dont on vient de copier les données
            curr.right = self._removeHelper(curr.right, min_node.key)
        
        return curr


    def getInorderKeys(self) -> List[int]:
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if not node:
            return
        self._inorder(node.left, result)  # Visite gauche
        result.append(node.key)           # Visite racine
        self._inorder(node.right, result) # Visite droite

