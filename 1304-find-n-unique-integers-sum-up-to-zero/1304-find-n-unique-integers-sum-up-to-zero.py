class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0] * n
        if n % 2 == 1:
            for i in range(1, int((n - 1) / 2 + 1)):
                res[i] = i
                res[-i] = -i
        else:
            for i in range(int((n - 2) / 2 + 1)):
                res[i] = i + 1
                res[-i - 1] = -i - 1
        
        return res
        