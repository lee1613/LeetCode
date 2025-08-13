class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        

        def binary_search(target, start, end):
            if start == end:
                if target > nums[start]:
                    return start + 1
                else: 
                    return start
            new_half = start + int((end - start + 1) / 2)
            
            if target == nums[new_half]:
                return new_half
            elif target > nums[new_half]:
                return binary_search(target, new_half, end)
            else:
                return binary_search(target, start, new_half - 1)
        
        return binary_search(target, 0, len(nums) - 1)