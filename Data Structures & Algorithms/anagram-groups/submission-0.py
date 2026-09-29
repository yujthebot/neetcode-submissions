class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        flist = []
        temp = []
        count = 1
        for s in strs:
            s_sorted = sorted(s)
            if tuple(s_sorted) in group:
                group[tuple(s_sorted)].append(s)

            else: 
                group[tuple(s_sorted)]=[s]

        return list(group.values())