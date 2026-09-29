class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)      

        inverted = defaultdict(list)
        for key in freq:
            inverted[freq[key]].append(key)

        ordered_frequencies = sorted(inverted.keys(), reverse=True)

        count = 0
        output = []
        for frequency in ordered_frequencies:
            for num in inverted[frequency]:
                output.append(num)
                count += 1
            if count == k:
                break
        
        return output
        