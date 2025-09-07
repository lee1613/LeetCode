class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 == 1:
            res.append(0)
            for i in range(1, int((n - 1) / 2 + 1)):
                res.append(i) 
                res.append(-i)
        else:
            for i in range(int((n - 2) / 2 + 1)):
                res.append(i + 1)
                res.append(-i - 1)
        
        return res
        