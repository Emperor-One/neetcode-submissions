class Solution:
    def search(self, nums: List[int], target: int) -> int:        
# left + (right - left // 2)
# [0, 5, 10,| 20, 30,| 40]
# left right mid nums[mid] target       comparison
# 0    5     2      10        20      20 > 10 -> left = mid + 1
# 3    5     4      30        20        20 < 30 -> right = mid - 1
# 3    3     3      20        20        20 == 20 -> return mid (3)
        left = 0
        right = len(nums) - 1

        while (left <= right):
            mid = left + ((right - left) // 2)

            if (nums[mid] == target):
                return mid
            elif (target < nums[mid]):
                right = mid - 1
            elif (target > nums[mid]):
                left = mid + 1

        return -1