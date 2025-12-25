class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0] * n
        # Any edge cases where the nums.length  = 2 is resolved

        res[-1] = nums[-1]
        for i in range(n - 2, 0, -1):
            res[i] = nums[i] * res[i + 1]
        
        res[0] = res[1]

        product = 1

        for i in range(1, n - 1):
            product *= nums[i - 1]
            res[i] = product * res[i + 1]
        
        res[-1] = product * nums[-2]

        return res
        



        
        # # The first result is the index - -2 of suffix, then the second results is the product of index - 0 of prefix * index - -3 of suffix, 


        # for i in range(n - 2):
        #     # Multiply with the third last suffix product when it's the first one since the second element is being ignored
        #     res.append(suffix[n - 3  - i] * prefix[i])

        #     # The last element will be prefix of n-3th element multiply with the 0th elmeent of suffix
        # res.append(prefix[-2])

        # return res

        