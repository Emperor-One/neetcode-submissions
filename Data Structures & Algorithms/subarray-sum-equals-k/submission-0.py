class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        frequency = defaultdict(int, {0:1})
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in frequency:
                count += frequency[prefix_sum - k]
            frequency[prefix_sum] += 1
        
        return count
        