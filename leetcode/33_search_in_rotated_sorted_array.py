from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            # Если левая часть отсортирована
            if nums[low] <= nums[mid]:
                # Если элемент входит в левую часть
                if nums[low] <= target < nums[mid]:
                    # ищем в левой части
                    high = mid - 1
                # если он точно не входит, стоит проверить правую
                else:
                    low = mid + 1
            # Если правая часть отсортирована
            else:
                # Если элемент входит в правую часть
                if nums[mid] < target <= nums[high]:
                    # Там и ищем
                    low = mid + 1
                else:
                    high = mid - 1

        # если ничего не нашли
        return -1


if __name__ == '__main__':
    solution = Solution()
    assert solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert solution.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
    assert solution.search(nums=[1], target=0) == -1
    assert solution.search(nums=[3, 1], target=1) == 1
    assert solution.search(nums=[5, 1, 3], target=3) == 2
    assert solution.search(nums=[1, 3], target=3) == 1
