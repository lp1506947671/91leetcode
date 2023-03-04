

## 思路

1. 索整个数组的方式来判断 `target - num` 是否也存在 `nums` 
2. 使用哈希表  将寻找 `target - x` 的时间复杂度降低到从 O(N) 降低到 O(1), 对于每一个 `x`，我们首先查询哈希表中是否存在 `target - x`，然后将 `x` 插入到哈希表中，即可保证不会让 `x` 和自己匹配 



## 代码

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

```



## 复杂度

时间复杂度:O(n)

空间复杂度:O(n)