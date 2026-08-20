class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Dictionnaire pour stocker : valeur -> index
        my_map = {} 

        # On parcourt les indices de 0 à la fin de la liste
        for i in range(len(nums)):
            # On récupère la valeur manuellement avec l'index
            n = nums[i]
            diff = target - n

            # On vérifie si la différence est déjà dans notre dictionnaire
            if diff in my_map:
                # Si oui, on retourne l'index stocké et l'index actuel
                return [my_map[diff], i]
            
            # Sinon, on ajoute la valeur actuelle et son index au dictionnaire
            my_map[n] = i