class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        left = 0
        n = len(s)
        length = 0
        maxl = 0
        for right in range(n):
            if s[right] in window:
                window[s[right]]+=1
            else:
                window[s[right]]=1

            if (sum(window.values())-max(window.values()))>k:
                window[s[left]]-=1
                left+=1
                
            length = sum(window.values())
            maxl = max(length, maxl)
        return maxl
        