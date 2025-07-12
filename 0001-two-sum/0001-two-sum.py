class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique_nums = set(nums)
        index_map = {n:[] for n in unique_nums}
        for i, n in enumerate(nums):
            index_map[n].append(i)

        for num in unique_nums:
            if num * 2 == target:
                if len(index_map[num]) > 1:
                    return index_map[num]
            else:
                if index_map.get(target - num, -1) != -1:
                    return [index_map[num][0], index_map[target - num][0]]