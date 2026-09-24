class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            dictionary[num] = i

        for i, num in enumerate(nums):
            dic_b = dictionary.get(target - num, None)
            if dic_b is not None and i != dic_b:
                return [i, dic_b]