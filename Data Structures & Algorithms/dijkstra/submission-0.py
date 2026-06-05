import heapq


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        # 1. Préparer le graphe (liste d'adjacence)
        graph = {i: [] for i in range(n)}
        for source, target, weight in edges:
            graph[source].append((target, weight))

        # 2. Initialiser les structures de données
        shortest_distances = {}
        priority_queue = [[0, src]]  # [distance, node]

        # 3. La boucle principale
        while priority_queue:
            current_dist, current_node = heapq.heappop(priority_queue)

            if current_node in shortest_distances:
                continue

            shortest_distances[current_node] = current_dist

            for neighbor, weight in graph[current_node]:
                if neighbor not in shortest_distances:
                    new_dist = current_dist + weight
                    heapq.heappush(priority_queue, [new_dist, neighbor])

        # 4. Remplir les noeuds manquants
        for i in range(n):
            if i not in shortest_distances:
                shortest_distances[i] = -1

        return shortest_distances
