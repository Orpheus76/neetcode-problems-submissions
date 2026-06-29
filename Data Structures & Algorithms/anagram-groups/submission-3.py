from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            # 1. On trie le mot. 'cat' devient ['a', 'c', 't']
            # 2. On le rejoint en string pour en faire une clé : "act"
            sorted_s = "".join(sorted(s))

            # 3. On ajoute le mot original à la liste correspondante à cette clé
            res[sorted_s].append(s)

        # On retourne toutes les listes regroupées
        return list(res.values())
