class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            j = dictionary.get(target - nums[i], None)
            if j is not None:
                return [j, i]
            dictionary[nums[i]] = i 