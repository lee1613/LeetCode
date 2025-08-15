class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n < 1:
            return False

        curr = 1
        while curr < n:
            curr *= 4
        if curr == n:
            return True
        else: 
            return False