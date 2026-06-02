class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        return self.dfsHelper(grid, 0, 0, visit)

    def dfsHelper(self, grid: List[List[int]], r: int, c: int, visit):
        ROWS = len(grid)
        COLS = len(grid[0])

        # 1. Conditions d'échec (Hors limites, Obstacle, Déjà visité)
        if (r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 1 or (r,c) in visit):
            return 0

        # 2. Condition de réussite (Arrivée au coin bas-droit)
        if r == ROWS - 1 and c == COLS - 1:
            return 1

        # 3. Marquage de la cellule actuelle
        visit.add((r, c))

        # 4. Exploration des 4 directions
        count = 0
        count += self.dfsHelper(grid, r-1, c, visit) # Haut
        count += self.dfsHelper(grid, r, c+1, visit) # Droite
        count += self.dfsHelper(grid, r+1, c, visit) # Bas
        count += self.dfsHelper(grid, r, c-1, visit) # Gauche

        # 5. Backtracking : on retire la cellule pour permettre d'autres chemins
        visit.remove((r, c))

        return count