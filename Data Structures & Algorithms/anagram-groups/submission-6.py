class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        words = {}
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char)-ord("a")] += 1
            c = tuple(count)
            if c in words:
                words[c].append(s)
            else:
                words[c] = [s]
        return list(words.values())
                