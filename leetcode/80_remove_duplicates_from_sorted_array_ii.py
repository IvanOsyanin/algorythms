from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i, j = 2, 2
        while j <= len(nums) - 1:
            # Если текущий элемент не равен элементу на 2 позиции назад от i
            # Это гарантирует, что мы не добавляем третий дубликат подряд
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


if __name__ == '__main__':
    solution = Solution()
    assert solution.removeDuplicates([1, 1, 1, 2, 2, 3]) == 5
    assert solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7
