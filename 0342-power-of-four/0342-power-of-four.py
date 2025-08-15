class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # Solution 1 (Building integer from sratch)
        # if n < 1:
        #     return False

        # curr = 1
        # while curr < n:
        #     curr *= 4
        # if curr == n:
        #     return True
        # else: 
        #     return False

        # Solution 2 (Check if the log (base 4) of a number is integer)
        if n < 1:
            return False
        res = math.log(n, 4)
        if res - int(res) < 1 * 10**-10:
            return True
        else:
            return False