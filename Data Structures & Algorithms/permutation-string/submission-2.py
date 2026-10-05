class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1d = {}
        for i in range(len(s1)):
            s1d[s1[i]]  = s1d.get(s1[i],0)+1
        valid = False
        for right in range(len(s2)):
            window = right-left+1
            if s2[right] in s1d:
                s1d[s2[right]]-=1
            if window > len(s1):
                left+=1
                if s2[left-1] in s1d:
                    s1d[s2[left-1]]+=1
            
            if all(v == 0 for v in s1d.values()):
                valid = True
        return valid
            

        

        