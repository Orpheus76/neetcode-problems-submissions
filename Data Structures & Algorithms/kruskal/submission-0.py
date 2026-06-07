import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.edges_count = 0

    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.edges_count += 1
            return True
        return False


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        # 1. Sort edges by weight
        # You can use edges.sort(key=lambda x: [2]) or a Min-Heap
        edges.sort(key=lambda x: x[2])

        uf = UnionFind(n)
        mst_weight = 0

        # 2. Process edges
        for u, v, weight in edges:
            if uf.union(u, v):
                mst_weight += weight

        # 3. Validation
        # If edges in MST == n - 1, it's a valid spanning tree
        return mst_weight if uf.edges_count == n - 1 else -1
