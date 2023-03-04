## 题目地址(两数之和)

https://leetcode-cn.com/problems/two-sum

## 入选理由

1. 两数之和的经典程度不用我多说了，大家都应该知道。
2. 这道题不仅是入门题目，而且和后面我们要讲的双指针有联系。

## 标签

- 哈希表
- 双指针

## 难度

- 简单

### 前置知识

- 哈希表

### 思路 - 暴力

思路很简单，遍历数据，对每一个出现的 num 判断其另一半 `target - num` 是否也出现在数组中即可

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []

```



#### 复杂度分析

- 空间复杂度: O(1)O(1)
- 时间复杂度：O(n^2)O(n2), nn为数组长度
- 

### 思路

上面是用于搜索整个数组的方式来判断 `target - num` 是否也存在 `nums`, 我们也可以用哈希表记录所有已经遍历过的数字，判断 `target - num` 是否出现时，直接查表即可。

#### 代码

**哈希表是非常常用的时间换空间的方式**

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



### 复杂度分析

- 空间复杂度: O(n)O(n)
- 时间复杂度: O(n)O(n)
