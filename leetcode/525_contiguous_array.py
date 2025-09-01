from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_indices = {0: -1}
        max_lenght = 0
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += 1 if num == 1 else -1

            if current_sum in sum_indices:
                prev_index = sum_indices[current_sum]
                lenght = i - prev_index
                if lenght > max_lenght:
                    max_lenght = lenght

            else:
                sum_indices[current_sum] = i

        return max_lenght


if __name__ == "__main__":
    solution = Solution()
    assert solution.findMaxLength(nums=[0, 1]) == 2
    assert solution.findMaxLength(nums=[0, 1, 0]) == 2
    assert solution.findMaxLength(nums=[0, 1, 1, 1, 1, 1, 0, 0, 0]) == 6
