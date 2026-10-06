class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        window = []
        max_box = 0 
        curr_min = float("inf")
        for start_idx,char in enumerate(heights):
            idx = start_idx
            while len(window) != 0 and char <  window[-1][1]:
                element = window.pop()
                max_box = max(max_box, element[1]*(start_idx-element[0])) #calculate the maximum box size
                idx = element[0] #store the new potential left wing
            tup = (idx, char)
            window.append(tup)
        while len(window) != 0:
            element = window.pop()
            max_box = max(max_box,element[1]*(start_idx-element[0]+1))
        return max_box