class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            if path not in result:
                result.append(path[:])
            for i in range(start,len(nums)): #limit the start of the for loop to test all values following the start
                path.append(nums[i])
                backtrack(i+1,path) #test out the next value to be filled into previous
                path.pop() #remove the element after all next ones are tested and then go backwards
        backtrack(0,[])
        return result

          


