class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        sorted_elements = sorted(
            count.keys(),
            key=lambda x: count[x],
            reverse=True
        )

        return sorted_elements[:k]