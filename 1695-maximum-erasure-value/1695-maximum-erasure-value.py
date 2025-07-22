class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        unique = set(nums)
        included = {num: False for num in unique}

        if len(unique) == len(nums):
            return sum(unique)

        i = 0
        j = 0
        max_out = 0
        curr_val = 0

        while j < len(nums):
            num = nums[j]
            if included[num] is False:
                included[num] = True
                curr_val += num
                if curr_val > max_out:
                    max_out = curr_val
            else:
                while nums[i] != num:
                    curr_val -= nums[i]
                    included[nums[i]] = False
                    i += 1
                
                i += 1

            j += 1 

        return max_out

