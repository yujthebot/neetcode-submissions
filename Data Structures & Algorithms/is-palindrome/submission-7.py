class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(" ", "").lower()
        s=list(s)
        t=s.copy()
        for i in s:
            if i.isalnum() == False:
                print(i)
                t.remove(i)

        for i in range((len(t)//2)):
            
            if t[i] != t[-1-i]:
                return False
        return True