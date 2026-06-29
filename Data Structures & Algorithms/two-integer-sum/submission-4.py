class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # nombre : index

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n

            if diff in seen:
                return [seen[diff], i]

            seen[n] = i
