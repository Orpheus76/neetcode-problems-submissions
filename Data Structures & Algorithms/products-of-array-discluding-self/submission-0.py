class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i, j = 0, 0

        for i in range(len(nums)):
            n = 1

            for j in range(len(nums)):
                if j == i:
                    continue
                n *= nums[j]

            res.append(n)

        return res
