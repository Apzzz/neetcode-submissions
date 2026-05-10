class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapNo = {}

        for no in nums:
            if no in mapNo.keys():
                mapNo[no] += 1
            else:
                mapNo[no] = 1
        
        sortedNos = sorted(mapNo, key=mapNo.get, reverse = True)
        return sortedNos[:k]