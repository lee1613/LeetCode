class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # res = 0
        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         if matrix[row][col] == 1:
        #             matrix[row][col] == 0
        #             res += 1
        #             row_size = 1
        #             col_size = 1
        #             while row + size < len(matrix) and col + size < len(matrix[0]):
        #                 row_expand = True
        #                 col_expand = True
        #                 for i in range(size + 1):
        #                     if matrix[row + size][col + i] != 1:
        #                         col_expand = False
                        
        #                 for i in range(size):
        #                     if matrix[row + i][col + size] != 1:
        #                         expand = False
                        
        #                 if expand:
        #                     for i in range(size + 1):
        #                         if matrix[row + size][col + i] == 1:
        #                             matrix[row + size][col + i] = 0                       
                            
        #                     for i in range(size):
        #                         if matrix[row + i][col + size] == 1:
        #                             matrix[row + i][col + size] = 0

        #                     res += size * 2 + 1 + size ** 2
        #                     size += 1
        #                 else:
        #                     break

        # return res

        res = 0
        size = 1
        while size <= min(len(matrix), len(matrix[0])):
            count = 0
            for row in range(len(matrix) - size + 1):
                for col in range(len(matrix[0]) - size + 1):
                    expand = True
                    for i in range(size):
                        for j in range(size):
                            if matrix[row + i][col + j] == 0:
                                expand = False
                    if expand:
                        count += 1
            
            res += count
            size += 1
            if count < 4:
                break
            
            

        return res
                            

