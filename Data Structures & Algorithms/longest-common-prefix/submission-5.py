class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first_word = strs[0]

        for i in range(len(first_word)):
            ch = first_word[i]

            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != ch:
                    return first_word[:i]
        
        return first_word