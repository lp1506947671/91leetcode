from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, data in enumerate(nums):
            item = target - data
            if item in nums and nums.index(item) != index:
                return [index, nums.index(item)]
        return []


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    a = Solution()
    print(a.twoSum(nums, target))
