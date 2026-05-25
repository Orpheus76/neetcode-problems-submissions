from typing import List


class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        # Case 1: no root
        if not self.root:
            self.root = Node(key, val)
            return

        # Case 2: General Case --> Look at the tree
        curr = self.root
        while curr:
            # Go left
            if key < curr.key:
                if not curr.left:
                    curr.left = Node(key, val)
                    return
                curr = curr.left

            # Go right
            elif key > curr.key:
                if not curr.right:
                    curr.right = Node(key, val)
                    return
                curr = curr.right

            # Key already exists, update the value
            else:
                curr.val = val
                return

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            # Go left
            if key < curr.key:
                curr = curr.left

            # Go right
            elif key > curr.key:
                curr = curr.right

            # Key found
            else:
                return curr.val

        # Key not found
        return -1

    def getMin(self) -> int:
        # If tree is empty
        if not self.root:
            return -1

        # Smallest key is the leftmost node
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        # If tree is empty
        if not self.root:
            return -1

        # Largest key is the rightmost node
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        self.root = self._remove_helper(self.root, key)

    def _remove_helper(self, curr: Node, key: int) -> Node:
        if not curr:
            return None

        if key < curr.key:
            curr.left = self._remove_helper(curr.left, key)
        elif key > curr.key:
            curr.right = self._remove_helper(curr.right, key)
        else:
            # Case 1 & 2: Zero or one child
            if not curr.left:
                return curr.right
            elif not curr.right:
                return curr.left

            # Case 3: Two children
            # 1. Find the min node of the right subtree (successor)
            min_node = self._find_min(curr.right)
            # 2. Replace current node's data with successor's data
            curr.key = min_node.key
            curr.val = min_node.val
            # 3. Delete the successor from the right subtree
            curr.right = self._remove_helper(curr.right, min_node.key)

        return curr

    def _find_min(self, node: Node) -> Node:
        # Helper to find the node with the minimum key in a subtree
        while node.left:
            node = node.left
        return node

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: Node, result: List[int]) -> None:
        # Recursive In-order Traversal: Left -> Root -> Right
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
