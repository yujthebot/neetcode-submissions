class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowrow = 0
        highrow = len(matrix)-1
        rowans = 0
        while lowrow <=highrow:
            midrow = (lowrow+highrow)//2
            if matrix[midrow][0] == target:
                return True
            elif matrix[midrow][0] >target:
                if matrix[midrow-1][0] <target:
                    rowans = midrow-1
                    break
                else:
                    highrow = midrow-1
            else:
                if midrow == highrow:
                    rowans = midrow
                    break
                elif matrix[midrow+1][0]> target:
                    rowans = midrow
                    break
                else:
                    lowrow = midrow+1
        low = 0
        high = len(matrix[rowans])-1
        while low <= high:
            mid = (low+high)//2
            if matrix[rowans][mid]== target:
                return True
            elif matrix[rowans][mid]> target:
                high = mid-1
            else:
                low = mid+1
        return False