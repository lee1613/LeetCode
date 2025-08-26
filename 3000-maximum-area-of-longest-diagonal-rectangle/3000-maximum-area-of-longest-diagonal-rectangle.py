class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = 0 
        diaganol = 0 
        for length, width in dimensions:
            curr_diaganol = length ** 2 + width ** 2
            if curr_diaganol > diaganol:
                diaganol = curr_diaganol
                area = length * width

            elif curr_diaganol == diaganol:
                if length * width > area:
                    area = length * width
            

        return area 
        