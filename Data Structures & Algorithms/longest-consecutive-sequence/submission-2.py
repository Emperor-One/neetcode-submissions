class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hashset = set()
        for i in range(len(nums)):
            hashset.add(nums[i])
        
        output = 1
        for num in hashset:
            if num - 1 not in hashset:
                next = num + 1
                current = 1
                while next in hashset:
                    next += 1
                    current += 1
                if current > output:
                    output = current
        
        return output