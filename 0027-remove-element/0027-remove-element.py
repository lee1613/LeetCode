class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # if len(nums) == 0:
        #     return 0
        # tail = len(nums) - 1
        # res = len(nums)
        # # Finding the value in nums such that it isn't the targeted val to be removed (If there isn't any val to be removed, which means tail will be - 1, then nothing to remove)
        # while nums[tail] == val and tail >= 0:
        #     tail -= 1
        #     res -= 1
        
        # head = 0
        # while head < tail:
        #     print(head, tail)
        #     if nums[head] == val: 
        #         res -= 1 
        #         nums[head] = nums[tail]
        #         tail -= 1
        #         while nums[tail] == val and tail > 0:
        #             tail -= 1
        #             res -= 1

            
        #     head += 1
        
        # return res

        ## The index will keep track of the first position that always has to be filled
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index



        