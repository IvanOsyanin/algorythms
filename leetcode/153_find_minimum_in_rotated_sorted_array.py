from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        # Бинарный поиск
        while low < high:
            mid = (low + high) // 2
            # Если средний элемент больше последнего — минимум справа
            if nums[mid] > nums[high]:
                low = mid + 1
            # Иначе минимум слева (или это mid)
            else:
                high = mid
        # После завершения цикла `low` указывает на минимальный элемент
        return nums[low]


if __name__ == "__main__":
    solver =  Solution()
    assert solver.findMin([3,4,5,1,2]) == 1
    assert solver.findMin([4,5,6,7,0,1,2]) == 0
    assert solver.findMin([11,13,15,17]) == 11
