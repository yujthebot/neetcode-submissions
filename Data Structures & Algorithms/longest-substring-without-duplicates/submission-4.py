class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = []
        maxl =0
        length = 0
        n = len(s)
        for i in range(n):
            if s[i] in dup:
                idx = dup.index(s[i])
                del dup[:idx+1]
            dup.append(s[i])
            length  =len(dup)
            maxl = max(maxl,length)
        return maxl

                