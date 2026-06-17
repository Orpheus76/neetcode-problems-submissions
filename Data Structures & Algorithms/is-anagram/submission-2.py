class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_contain = {}
        t_contain = {}

        for ch in s:
            s_contain[ch] = 1 + s_contain.get(ch, 0)

        for ch in t:
            t_contain[ch] = 1 + t_contain.get(ch, 0)

        for key in s_contain:
            if key not in t_contain or t_contain[key] != s_contain[key]:
                return False

        return True
