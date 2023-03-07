import collections
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            m = collections.defaultdict(int)
            for j in range(n):
                dist = abs(points[i][0] - points[j][0]) ** 2 + abs(points[i][1] - points[j][1]) ** 2
                m[dist] += 1
            for count in m.values():
                ans += count * (count-1)
        return ans
