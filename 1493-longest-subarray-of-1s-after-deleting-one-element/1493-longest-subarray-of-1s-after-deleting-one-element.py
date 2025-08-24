class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev_count = 0
        curr_count = 0
        zero_count = 0
        all_1 = True
        longest = 0

        for num in nums:
            if num == 0:
                all_1 = False
                zero_count += 1
                if zero_count > 1:
                    prev_count = 0
                else:
                    prev_count = curr_count
                curr_count = 0
            else:
                zero_count = 0
                curr_count += 1
                if prev_count + curr_count > longest:
                    longest = prev_count + curr_count
                
        if len(nums) == 0:
            return 0
        if all_1:
            return longest - 1
        
        return longest

