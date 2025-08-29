from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers) - 1
        l, r = 0, n
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
    assert solution.twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
    assert solution.twoSum(numbers=[2, 3, 4], target=6) == [1, 3]
    assert solution.twoSum(numbers=[-1, 0], target=-1) == [1, 2]
