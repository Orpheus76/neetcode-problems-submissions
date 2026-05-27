class Node:
    def __init__(self, total: int, L: int, R: int):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L  # Start of this node's range
        self.R = R  # End of this node's range


class SegmentTree:
    def __init__(self, nums: List[int]):
        # Build the tree starting from the full range of the array
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, L, R):
        # Base case: leaf node representing a single element
        if L == R:
            return Node(nums[L], L, R)

        M = (L + R) // 2
        root = Node(0, L, R)
        # Recursively build left and right children
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M + 1, R)

        # Internal node sum is the sum of its children
        root.sum = root.left.sum + root.right.sum
        return root

    def update(self, index: int, val: int) -> None:
        self._update_helper(self.root, index, val)

    def _update_helper(self, root, index, val):
        # Base case: Found the leaf node to update
        if root.L == root.R:
            root.sum = val
            return

        M = (root.L + root.R) // 2
        # Decide whether to go left or right based on the index
        if index <= M:
            self._update_helper(root.left, index, val)
        else:
            self._update_helper(root.right, index, val)

        # After updating the child, update the current node's sum
        root.sum = root.left.sum + root.right.sum

    def query(self, L: int, R: int) -> int:
        return self._query_helper(self.root, L, R)

    def _query_helper(self, root, L, R):
        # Case 1: Node range is completely within the query range [L, R]
        if L <= root.L and root.R <= R:
            return root.sum

        # Case 2: Node range is completely outside the query range [L, R]
        if R < root.L or L > root.R:
            return 0

        # Case 3: Node range partially overlaps; query both children
        return self._query_helper(root.left, L, R) + self._query_helper(root.right, L, R)
