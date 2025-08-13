from typing import List


class Solution:
    def searchMatrix(
        self,
        matrix: List[List[int]],
        target: int
    ) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        low = 0
        high = rows*columns - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[mid // columns][mid % columns] == target:
                return True
            elif matrix[mid // columns][mid % columns] > target:
                high = mid - 1
            elif matrix[mid // columns][mid % columns] < target:
                low = mid + 1
        return False


if __name__ == '__main__':
    solution = Solution()
    assert solution.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
        target=3) is True
    assert solution.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
        target=13) is False
