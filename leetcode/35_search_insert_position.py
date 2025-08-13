from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchInsert([1, 3, 5, 6], 0) == 0
    assert solution.searchInsert([1, 3, 5, 6], 5) == 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4
