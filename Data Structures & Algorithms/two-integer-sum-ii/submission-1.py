class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s=None
        index1 = 0
        index2 = len(numbers)-1
        while s != target:
            s = numbers[index1]+numbers[index2]
            if s>target:
                index2-=1
            elif s<target:
                index1+=1
        return [index1+1,index2+1]