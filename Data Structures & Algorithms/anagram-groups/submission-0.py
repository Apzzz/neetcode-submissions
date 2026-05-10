class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapAnagrams = defaultdict(list)

        for s in strs:
            sortedString = "".join(sorted(s))
            mapAnagrams[sortedString].append(s)

        return list(mapAnagrams.values())
