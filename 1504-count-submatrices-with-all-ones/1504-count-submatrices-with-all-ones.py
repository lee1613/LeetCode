class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        res = 0
        sub = [[0] * (len(mat[0]) + 1) for i in range(len(mat) +1)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    sub[i + 1][j + 1] = min(sub[i][j], sub[i + 1][j], sub[i][j + 1]) + 1
        
        res += sum(list(map(sum, sub)))
        
        
        for i in range(1, len(sub)):
            prev = 0
            count = 0
            for j in range(1, len(sub[0])): 
                if sub[i][j] > 1:
                    if sub[i][j] == prev:
                        count += 1
                        res += count - 1
                    
                    else:
                        count = 1
                        prev = sub[i][j]

                else:
                    prev = sub[i][j]
                    count = 0
                    

        
        

        for j in range(1, len(sub[0])):
            prev = 0
            count = 0
            for i in range(1, len(sub)): 
                if sub[i][j] > 1:
                    if sub[i][j] == prev:
                        count += 1
                        res += count - 1
                        
                    else:
                        prev = sub[i][j]
                        count = 1
                else:
                    count = 0
                    prev = sub[i][j]

                

        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count += 1
                    res += max(count - 1, 0)
                else:
                    count = 0

        for j in range(len(mat[0])):
            count = 0
            for i in range(len(mat)):
                if mat[i][j] == 1:
                    count += 1
                    res += max(count - 1, 0)
                else:
                    count = 0

        return res
        
