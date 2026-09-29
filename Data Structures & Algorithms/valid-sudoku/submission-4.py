class Solution:
    def validCheck(self, d):
        ans = True
        for key, values in d.items():
            if key == '.':
                pass
            elif d[key] == 1:
                pass
            else:
                ans = False
        return ans
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #grid detection
        coli = 0
        for row in range (0,9,3):
            for col in range (0, 9, 3):
                g1 = {}
                for i in range(col, col+3):
                    for j in range(row, row+3):
                        if board[i][j] in g1:
                            g1[board[i][j]] += 1
                        else: 
                            g1[board[i][j]] = 1
                if self.validCheck(g1) == False:
                    return False
        for col in range(9):
            c = {}
            for row in range(9):                
                p = board[row][col]
                if p in c:
                    c[p] +=1
                else:
                    c[p] = 1
                print(c)
                if self.validCheck(c) == False:
                    return False
        for row in range(9):
            r = {}
            for col in range(9):                
                p = board[row][col]
                if p in r:
                    r[p] +=1
                else:
                    r[p] = 1
                print(r)
                if self.validCheck(r) == False:
                    return False
        
            
        return True

