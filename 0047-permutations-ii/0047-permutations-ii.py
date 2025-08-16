class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Solution 1 (7ms, 18mb)
        # res = []
        # nums.sort()
        # n = len(nums)
        # def backtrack(combi, rem_nums):
        #     if len(combi) == n:
        #         res.append([i for i in combi])
                
        #     else:
        #         prev = 11
        #         for i in range(len(rem_nums)):
        #             num = rem_nums[i]
        #             if num != prev:
        #                 prev = num
        #                 combi.append(num)
        #                 popped = rem_nums.pop(i)
        #                 backtrack(combi, rem_nums)
        #                 rem_nums.insert(i, popped)
        #                 combi.pop(-1)
            
        # backtrack([], nums)
        # return res

        # Solution 2 (3ms, 17.92mb)
        
        res = []
        nums.sort()
        def backtrack(start):
            if start == len(nums):
                res.append([i for i in nums])
            else:
                used = set()
                for i in range(start, len(nums)):
                    if nums[i] in used:
                        continue
    
                    else:
                        used.add(nums[i])
                        nums[start], nums[i] = nums[i], nums[start]
                        backtrack(start + 1)
                        nums[i], nums[start] = nums[start], nums[i]
        backtrack(0)
        return res
                
        
                    