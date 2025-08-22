class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top = len(grid) - 1
        bottom = 0
        left = len(grid[0]) - 1
        right = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if row < top:
                        top = row
                    if row > bottom:
                        bottom = row
                    
                    if col < left:
                        left = col
                    if col > right:
                        right = col
        
        # print(top, bottom, left, right)

        if top > bottom and left > right:
            return 0
            
        return (bottom - top + 1) * (right - left + 1)
                    

        