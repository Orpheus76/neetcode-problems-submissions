from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # If the start or end is blocked, no path exists
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        
        # Queue stores (row, col)
        queue = deque([(0, 0)])
        # Set to keep track of visited cells
        visited = set([(0, 0)])

        length = 0

        while queue:
            # Number of nodes at the current distance
            for i in range(len(queue)):
                r, c = queue.popleft()

                # Did we reach the target?
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                # Check 4 neighbors: Right, Left, Down, Up
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc # New row, New column

                    # Validation check:
                    # 1. Stay inside grid boundaries
                    # 2. Cell must be land (grid[nr][nc] == 0)
                    # 3. Cell must not be visited
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        grid[nr][nc] == 0 and (nr, nc) not in visited):

                        queue.append((nr, nc))
                        visited.add((nr, nc))

            # Increment length after checking all nodes at the current distance
            length += 1
        
        return - 1  # Path not found





