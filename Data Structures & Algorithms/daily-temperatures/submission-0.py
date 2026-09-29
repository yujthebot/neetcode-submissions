class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = [0]*len(temperatures)
        temp_rev = []
        
        for i in range(len(temperatures)):
            index = n-i-1
            (x,y)=temperatures.pop(index),index
            while temp_rev and temp_rev[-1][0] <= x:
                temp_rev.pop()
            if temp_rev:
                out[index] = temp_rev[-1][1] - index
            else:
                out[index] = 0
            temp_rev.append((x,y))
        return out
        
        