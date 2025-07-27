class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        out = 0

        smaller = None
        prev = nums[1]
        for i in range(1, len(nums)):
            if nums[i] == nums[0]:
                continue
            else:
                smaller = nums[i] > nums[0]
                break
        if smaller is None :
            return out

        
        for j in range(i + 1, len(nums)):
            if nums[j] < prev:
                if smaller:
                    out += 1
                    smaller = False
                
            elif nums[j] > prev:
                if not smaller:
                    out += 1
                    smaller = True

            prev = nums[j]
        
        return out