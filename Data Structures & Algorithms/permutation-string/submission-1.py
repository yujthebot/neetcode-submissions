class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ref = {}
        l=0
        for right, char in enumerate(s1):
            ref[char] = ref.get(char,0) +1
        count = {}
        for r,ch in enumerate(s2):
            count[ch] = count.get(ch,0) +1
            same = True
              
            while sum(count.values()) > sum(ref.values()):
                count[s2[l]]-=1
                l+=1
            for char in ref:
                if count.get(char,0) != ref[char]:
                    same = False
                    break         
            if same:
                return True
        return False