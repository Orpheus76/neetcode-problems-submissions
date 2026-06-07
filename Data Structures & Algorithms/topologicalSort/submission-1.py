from collections import defaultdict


class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        # 1. Construction du graphe
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)

        # 2. Initialisation des états
        visited = set()
        visiting = set()
        top_sort = []

        # 3. Lancer le DFS pour chaque sommet
        for i in range(n):
            if i not in visited:
                if not self.has_cycle_dfs(i, adj, visited, visiting, top_sort):
                    return []

        return top_sort[::-1]

    def has_cycle_dfs(self, u, adj, visited, visiting, top_sort):
        # Si le noeud est dans 'visiting', on a bouclé (cycle)
        if u in visiting:
            return False
        # Si déjà 'visited', tout est bon pour ce chemin
        if u in visited:
            return True

        visiting.add(u)

        for v in adj[u]:
            if not self.has_cycle_dfs(v, adj, visited, visiting, top_sort):
                return False

        visiting.remove(u)
        visited.add(u)
        top_sort.append(u)

        return True
