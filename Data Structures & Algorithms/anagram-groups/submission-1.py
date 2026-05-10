class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapAnagrams = {}

        for s in strs:
            sortedString = ''.join(sorted(s))
            if sortedString in mapAnagrams.keys():
                mapAnagrams[sortedString].append(s)
            else:
                mapAnagrams[sortedString] = [s]
        
        return list(mapAnagrams.values())