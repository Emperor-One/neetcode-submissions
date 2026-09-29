class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            j = dic.get(target-num, None)
            if j is not None:
                return [j, i]
            dic[num] = i