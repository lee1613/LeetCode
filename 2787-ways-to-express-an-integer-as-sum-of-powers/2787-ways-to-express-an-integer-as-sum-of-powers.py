class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        def recurse(n, j, dp):
            if n == 0:
                if j >= 0:
                    return 0
                return 1
                
                
            if j == 0:
                return 0   
            if j == 1:
                if n > j:
                    return 0
                else: 
                    
                    return 1                           
            if dp[n][j] != -1:
                return dp[n][j]
            
            dp[n][j -1] = recurse(n, j - 1, dp)
            j1 = j - 1
            # Assuming the j is the largest j1 such that it is smaller than n
            reduced_n = n - j**x

            if reduced_n == 0:
                
                dp[reduced_n][j1] = 1
            else:
                while reduced_n < j1**x:
                    j1 -= 1

                

                dp[reduced_n][j1] = recurse(reduced_n, j1, dp)

            dp[n][j] = dp[n][j - 1] + dp[reduced_n][j1]

            return dp[n][j]
            
            

            dp[n][j - 1] = recurse(n)

        dp  = [[-1] * (n + 1) for i in range(n + 1)]
        actl_j = n ** (1/x)
        j = ceil(n ** (1/x))
        if j - actl_j > 1*10 ** -5:
            j -= 1
        return recurse(n, j, dp) % (10**9 + 7)