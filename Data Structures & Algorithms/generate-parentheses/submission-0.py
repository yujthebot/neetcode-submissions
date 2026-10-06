class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        left = 0
        right = 0
        def gen(path, left,right):
            if left+right == 2*n:
                result.append(path)
                return  #break when double the value is reached
            if left < n:
                path = path + "("
                left +=1 
                gen(path,left,right)
                path = path[:-1]
                left-=1
            if right<left:
                path = path + ")"
                right+=1
                gen(path, left, right)
                path = path[:-1]
                right-=1
            print(path)
            
        gen("",left,right)
        return result