class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = i

        for i in range(len(nums)):
            j = dic.get(target-nums[i], None)
            if j is not None and i != j:
                return [i, j]
