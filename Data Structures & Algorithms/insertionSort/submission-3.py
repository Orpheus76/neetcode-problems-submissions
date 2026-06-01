# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value


class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        res = []

        for r in range(len(pairs)):
            l = r

            while l > 0 and pairs[l - 1].key > pairs[l].key:
                tmp = pairs[l]
                pairs[l] = pairs[l - 1]
                pairs[l - 1] = tmp

                l -= 1

            res.append(pairs[:])  # [:] == [0:len(pairs)]

        return res
