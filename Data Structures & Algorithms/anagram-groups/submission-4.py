class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        words = {}
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char)-ord("a")] += 1
            if tuple(count) in words:
                words[tuple(count)].append(s)
            else:
                words[tuple(count)] = [s]
        return list(words.values())
                