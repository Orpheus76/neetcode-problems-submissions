# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs: return pairs
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)
    
    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if s < e:
            # 1. Calculer le milieu
            m = (s + e) // 2

            # 2. Trier la gauche
            self.mergeSortHelper(pairs, s, m)

            # 3. Trier la droite
            self.mergeSortHelper(pairs, m + 1, e)

            # 4. Fusionner (merge)
            self.merge(pairs, s, m, e)

        return pairs


    def merge(self, pairs: List[Pair], s: int, m: int, e: int):

        L = pairs[s : m + 1]    # tableau de gauche
        R = pairs[m + 1 : e + 1]    # tableau de droite

        i = 0   # Pointeur de L
        j = 0   # Pointeur de R
        k = s   # Pointeur pour le tableau pairs (commence à s)
        
        # Tant qu'il reste des éléments dans les deux listes
        while i < len(L) and j < len(R):
            
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1

        return pairs

