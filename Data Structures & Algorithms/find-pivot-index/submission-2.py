class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suffix_sum = [0] * len(nums)
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            suffix_sum[i] = total
            total += nums[i]
        print(suffix_sum)
        total = 0
        for i in range(len(nums)):
            print(total, suffix_sum[i])
            if total == suffix_sum[i]:
                return i
            total += nums[i]
        
        return -1

        