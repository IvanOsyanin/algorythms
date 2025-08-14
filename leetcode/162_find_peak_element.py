from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        low = 0
        high = len(nums) - 1

        # Поиск пика (ищем локальный максимум)
        while low < high:  # < потому что мы сужаем область, где может быть пик
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid      # Пик в левой половине (включая mid)
            else:
                low = mid + 1   # Пик в правой половине
        return low  # low == high, это и есть позиция пика


if __name__ == '__main__':
    solution = Solution()
    assert solution.findPeakElement(nums=[1, 2, 3, 1]) == 2
    assert solution.findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4]) == 5
    assert solution.findPeakElement(nums=[1, 2]) == 1
    assert solution.findPeakElement(nums=[3, 2, 1]) == 0
    assert solution.findPeakElement(nums=[1, 3, 2]) == 1
