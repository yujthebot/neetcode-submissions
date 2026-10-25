class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        for i in range(len(strs[0])):
            common_char = strs[0][:i+1]
            for j in range(1,len(strs)):
                test = strs[j][:i+1]
                if test != common_char:
                    return strs[0][:i]

        return strs[0][:i+1]
