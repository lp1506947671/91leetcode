import collections
import heapq
from typing import List


class Solution1:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_list = []
        hash_map = {}
        for i in nums:
            hash_map[i] = hash_map.setdefault(i, 0) + 1

        freq_list = [None] * (len(nums) + 1)  # 边界值为0的情况不会使用,固要加1
        for key, value in hash_map.items():
            if not freq_list[value]:
                freq_list[value] = []
            freq_list[value].append(key)

        for j in freq_list[-1::-1]:
            if not j:
                continue
            for z in j:
                if len(result_list) < k:
                    result_list.append(z)

        return result_list


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = {}  # {'nums的值':'nums的值出现的次数'}
        for i in nums:
            occurrences[i] = occurrences.setdefault(i, 0) + 1
        occurrences = collections.Counter(nums)
        heap = [(-frequency, value) for value, frequency in occurrences.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for i in range(k)]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    a = Solution()
    print(a.topKFrequent(nums, k))
    ...
