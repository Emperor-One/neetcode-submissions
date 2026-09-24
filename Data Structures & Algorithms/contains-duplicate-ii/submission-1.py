class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) == 1:
            return False
        
        dictionary = {}
        for i, num in enumerate(nums):
            j = dictionary.get(num, None)
            
            if j is not None:
                if abs(i - j) <= k:
                    return True
                del dictionary[num]
                j = None

            if j is None:
                dictionary[num] = i

        return False