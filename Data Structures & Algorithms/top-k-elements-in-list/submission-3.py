class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        
        for n in nums:
            if n in count:
                count[n] = 1 + count.get(n, 0)
            else:
                count[n] = 1
        
        sorted_elements = sorted(
            count.keys(),
            key=lambda x: count[x],
            reverse=True
        )

        res = []
        for elem in range(k):
            res.append(sorted_elements[elem])

        return res 