from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        for num in nums:
            if num == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count

    def findNumbers(self, nums: List[int]) -> int:
        count_even = 0
        for num in nums:
            current_count = 1
            while num  // 10 > 0:
                current_count += 1
                num = num  // 10
            if current_count % 2 == 0:
                count_even += 1
        return count_even

    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        rez_pointer = len(nums) - 1

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]

            if left_square > right_square:
                result[rez_pointer] = left_square
                left += 1
            else:
                result[rez_pointer] = right_square
                right -= 1

            rez_pointer -= 1

        return result

    def duplicateZeros(self, arr: List[int]):
        count_zeros = 0
        for n in arr:
            if n == 0:
                count_zeros += 1

        len_arr = len(arr)
        read_index = len_arr - 1
        write_index = len_arr - 1 + count_zeros

        while read_index >= 0:
            if write_index <= len_arr - 1:
                arr[write_index] = arr[read_index]

            if arr[read_index] == 0 and write_index - 1 >= 0:
                write_index -= 1
                if write_index < len_arr:
                    arr[write_index] = 0

            read_index -= 1
            write_index -= 1

        return arr


    def merge(self,
              nums1: List[int], m: int,
              nums2: List[int], n: int):
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        return nums1

if __name__ == '__main__':
    solution = Solution()
    assert solution.findMaxConsecutiveOnes(nums=[1,1,0,1,1,1])  == 3
    assert solution.findNumbers(nums=[12,345,2,6,7896]) == 2
    assert solution.sortedSquares(nums=[-4,-1,0,3,10]) == [0,1,9,16,100]
    assert solution.sortedSquares(nums=[-7,-3,2,3,11]) == [4,9,9,49,121]
    assert solution.duplicateZeros([1,0,2,3,0,4,5,0]) == [1,0,0,2,3,0,0,4]
    assert solution.merge(nums1 = [1,2,3,0,0,0], m = 3,
                          nums2 = [2,5,6], n = 3) == [1,2,2,3,5,6]
    assert solution.merge(nums1 = [1], m = 1, nums2 = [], n = 0) == [1]
    assert solution.merge(nums1 = [0], m = 0, nums2 = [1], n = 1) == [1]

    assert solution.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1) == [1,2]
