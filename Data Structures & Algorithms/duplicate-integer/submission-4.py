class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        my_map = set()

        for n in nums:
            if n in my_map:
                return True
            my_map.add(n)
        
        return False
