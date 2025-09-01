from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(1, len(self.prefix)):
            self.prefix[i] = self.prefix[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]


if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    assert obj.sumRange(0, 2) == 1
    assert obj.sumRange(2, 5) == -1
