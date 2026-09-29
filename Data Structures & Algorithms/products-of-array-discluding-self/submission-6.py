class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        flist = []
        product = None
        count = 0
        for i in nums:
            if product == None:
                product = i if i !=0 else product
            else:
                product = product*i if i !=0 else product
        for j in nums:
            if j == 0:
                count +=1
        for j in nums:
            if count > 1:
                fproduct = 0
            elif count ==1:
                fproduct = product if j == 0 else 0
            else:
                fproduct = product/j 
            flist.append(int(fproduct))
        return flist