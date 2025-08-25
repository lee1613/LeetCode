class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        reverse = False
        for i in range(m + n - 1):
            if reverse:
                if i < n:
                    start = i
                    row = 0
                    while row < m and start >= 0:
                        res.append(mat[row][start])
                        row += 1
                        start -= 1

                else: 
                    start = i - n + 1
                    col = n - 1 # Start from last col
                    while col >= 0 and start < m:
                        res.append(mat[start][col])
                        start += 1
                        col -= 1  

                reverse = False

            
            else: 
                # If it's not reverse (i.e. It travel from the bottom to top / left to right)
                if i >= m:
                    # If i is alr bigger than the number of row in mat, then we should traverse by col of the bottom row
                    start = i - m + 1
                    row = m - 1
                    while start < n and row >= 0:
                        res.append(mat[row][start])
                        row -= 1
                        start += 1 
                
                else:
                    col = 0
                    start = i 
                    # The starting point here is the ith row
                    while start >= 0 and col < n:
                        res.append(mat[start][col])
                        col += 1
                        start -= 1

                reverse = True


        return res