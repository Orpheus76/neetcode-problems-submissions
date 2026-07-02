class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                # Calcul de la clé du carré 3 * 3
                square_key = (r // 3, c // 3)

                # Vérification : le chiffre est-il déjà présent ?
                if val in rows[r] or val in cols[c] or val in squares[square_key]:
                    return False

                # Ajout : On enregistre le chiffre
                rows[r].add(val)
                cols[c].add(val)
                squares[square_key].add(val)

        return True
