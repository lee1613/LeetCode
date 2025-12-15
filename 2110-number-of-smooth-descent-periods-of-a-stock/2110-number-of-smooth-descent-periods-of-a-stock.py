class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        seq = 1
        res = 0
        prev = 0
        for price in prices:
            if price + 1 == prev:
                seq += 1
            else:
                seq = 1
            res += seq

            prev = price
        
        return res
        