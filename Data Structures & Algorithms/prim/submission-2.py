import heapq


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        # 1. Construire le graphe
        adj = {}
        for i in range(n):
            adj[i] = []
        for src, dst, weight in edges:
            adj[src].append([dst, weight])
            adj[dst].append([src, weight])

        # 2. Initialiser le Min-heap
        minHeap = [[0, 0]]  # [vertex, weight]
        visit = set()
        res = 0  # Total weight of the MST

        # 3. Boucle principale
        while minHeap and len(visit) < n:
            w, node = heapq.heappop(minHeap)

            if node in visit:
                continue

            visit.add(node)
            res += w

            for neighbor, weight in adj[node]:
                if neighbor not in visit:
                    heapq.heappush(minHeap, [weight, neighbor])

        return res if len(visit) == n else -1
