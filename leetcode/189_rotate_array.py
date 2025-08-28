from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def rotate(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        rotate(0, n-1)  # Шаг 1: реверсируем весь массив
        rotate(0, k-1)  # Шаг 2: реверсируем первые k элементов
        rotate(k, n-1)  # Шаг 3: реверсируем остальные элементы

        return nums


if __name__ == '__main__':
    solution = Solution()
    solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
    assert solution.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3) == [
        5, 6, 7, 1, 2, 3, 4]
    assert solution.rotate(nums=[-1, -100, 3, 99], k=2) == [3, 99, -1, -100]
