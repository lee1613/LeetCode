class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # There's no heristics to define whether to continue or accumulate the subsequence lenght, so brute force with optimization will be suitable for this problem, I could make use of dp

        # Keep cutting the index by half and return the max from the second half and min from the first half the maximum subsequence it contains
        subseq_count = 1
        min_max = float("-inf")
        smallest = nums[0]

        # NO, we have to look at the ups, not the min_max
        
        # Through this process, we are trying to find the lower bound for the intermediate value, so that whenever we are not done with 3 values, we can make it easier to find the third subsequence, which is the optimal solution. Whenever the value goes up, as long as we haven't hit the third value, if the current value is smaller than the min_max, we replace the min_max with a smaller value and the smallest will be whichever is the smaller before. If it goes down, if the value is smaller than the min_max but bigger than the smallest, we replace it

        for i in range(1, len(nums)):
            # If it's an up
            if nums[i] > nums[i - 1]:
                if nums[i] > min_max:
                    subseq_count += 1
                    smallest = min(nums[i - 1], smallest)
                    min_max = nums[i]
                    if subseq_count == 3:
                        return True
                    
                # If it's not larger than the min_max, see if we could replace it
                else:
                    min_max = nums[i]
                    smallest = min(nums[i - 1], smallest)

            else:
                if nums[i] > smallest:
                    min_max = min(nums[i], min_max)
            
            # Even if it's going down, when the value is larger than the smallest, I could still replace it

        return False

                



        