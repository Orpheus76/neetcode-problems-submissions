class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_maps = self.createMap(s)
        t_maps = self.createMap(t)

        return s_maps == t_maps  


    def createMap(self, enter: str) -> {str: int}:
        enterMap = {}

        for ch in enter:
            if ch not in enterMap:
                enterMap[ch] = 1
            else:
                enterMap[ch] += 1
        
        return enterMap