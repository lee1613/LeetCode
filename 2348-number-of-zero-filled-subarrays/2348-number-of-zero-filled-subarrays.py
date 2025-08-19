class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        # Counting at each loop (29ms, 28.39mb)
        # res = 0
        # count = 0
        # for num in nums: 
        #     if num == 0:
        #         count += 1
        #         res += count
        #     else:
        #         count = 0

        # return res

        # Counting after the streak stop ()

        res = 0
        count = 0
        for num in nums: 
            if num == 0:
                count += 1
                
            else:
                if count > 0:
                    res += int(count * (count + 1) / 2)
                    count = 0

        res += int(count * (count + 1) / 2)

        return res