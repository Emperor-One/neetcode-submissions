class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        output = [0] * len(nums)
        suffix = 0
        # Construct suffix sum on output to save space
        for i in range(len(nums) - 1, -1, -1):
            suffix += nums[i]
            output[i] = suffix
            
        prefix_sum = 0
        # Compare prefix and suffix sum. Check for equality
        for i in range(len(output)):
            suffix_sum = 0 if i + 1 == len(output) else output[i + 1]
            print(i, prefix_sum, suffix_sum, nums[i])
            if prefix_sum == suffix_sum:
                return i

            prefix_sum += nums[i]

        return -1 

        