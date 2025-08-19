from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Возвращает индексы первого и последнего вхождения `target`
        в отсортированном массиве.
        Если `target` не найден, возвращает [-1, -1].
        """

        def find_bound(is_first: bool) -> int:
            """Находит либо первую, либо последнюю позицию `target`,
            в зависимости от `is_first`."""
            low, high = 0, len(nums) - 1
            bound = -1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    bound = mid
                    if is_first:
                        high = mid - 1  # Ищем дальше влево
                    else:
                        low = mid + 1   # Ищем дальше вправо
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return bound

        first = find_bound(is_first=True)
        last = find_bound(is_first=False)

        return [first, last]


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert solution.searchRange([], 0) == [-1, -1]
