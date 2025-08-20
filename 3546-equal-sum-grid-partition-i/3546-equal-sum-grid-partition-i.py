class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_sum = [sum(row) for row in grid]
        col_sum = [sum([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))]


        first_half_row = row_sum[0]
        second_half_row = sum(row_sum[1:])
        for i in row_sum[1:]:
            if first_half_row == second_half_row:
                return True
            first_half_row += i
            second_half_row -= i

        first_half_col = col_sum[0]
        second_half_col = sum(col_sum[1:])
        for i in col_sum[1:]:
            if first_half_col == second_half_col:
                return True
            first_half_col += i
            second_half_col -= i

        return False

        