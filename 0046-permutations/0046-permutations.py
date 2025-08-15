class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(combi): 
            if len(combi) == len(nums):
                res.append([i for i in combi]) 
            
            else:
                for i in [j for j in nums if j not in combi]:
                    combi.append(i)
                    
                    backtrack(combi)
                    combi.pop(-1)
            
        backtrack([])
        return res
