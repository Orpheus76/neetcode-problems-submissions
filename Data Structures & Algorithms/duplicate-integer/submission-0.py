class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq_elem = []

        for i in range(len(nums)):

            if nums[i] in uniq_elem:
                return True
            uniq_elem.append(nums[i])
        
        return False