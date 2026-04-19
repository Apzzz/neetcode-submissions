class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssort, tsort = "".join(sorted(s)), "".join(sorted(t))

        return ssort == tsort
