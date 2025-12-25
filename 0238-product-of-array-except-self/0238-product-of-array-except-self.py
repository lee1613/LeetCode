class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]

        n = len(nums)

        # Any edge cases where the nums.length  = 2 is resolved

        for i in range(1, n):
            prefix.append(nums[i] * prefix[-1])
        
        for i in range(n - 2, -1, -1):
            suffix.append(nums[i] * suffix[-1])


        
        # The first result is the index - -2 of suffix, then the second results is the product of index - 0 of prefix * index - -3 of suffix, 

        res = [suffix[-2]]

        for i in range(n - 2):
            # Multiply with the third last suffix product when it's the first one since the second element is being ignored
            res.append(suffix[n - 3  - i] * prefix[i])

            # The last element will be prefix of n-3th element multiply with the 0th elmeent of suffix
        res.append(prefix[-2])

        return res

        