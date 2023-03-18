## 题目地址(1834. 单线程 CPU)

https://leetcode-cn.com/problems/single-threaded-cpu/

## 前置知识

- 模拟
- 堆

## 标签

- 模拟
- 堆

## 难度

- 中等

## 入选理由

- 难度适中，同时联动了后面的专题《堆》

## 公司

- 暂无

## 思路

对于这道题，直接模拟即可。模拟就是直接按照题目描述写代码就行。

简单模拟题直接模拟就行， 中等模拟题则通常需要结合其他知识点。对于这道题来说， 就需要大家结合 **堆** 来完成。

题目说我们需要按照任务的先后顺序处理任务，并且：

- 如果当前没有正在处理任务时，直接处理。
- 如果当前正在处理任务， 则将其放入任务队列。处理完成之后从任务队列拿任务，而拿任务的依据就是**任务** 的时间长短，具体来说就是优先拿任务时长短的。

根据上面的描述，我们可以发现应该先对 task 按照开始时间进行排序。由于排序会破坏原有的顺序，而题目的返回是排序前的索引，因此排序后仍然需要维护排序前的索引。

另外任务队列中每次都取时间最短，这提示我们使用堆来存任务队列，并用任务时长做为 key，这是因为堆特别适合处理**动态极值**问题。如果不太熟悉堆也没关系，我们后面会讲解，如果现在做不出来，大家也可以到时候回过头来再做这道题。

那么如何用代码模拟上述过程呢？

我们用 time 表示当前的时间，time 从 0 开始，用 pos 记录我们处理到的 tasks。（由于我们进行了排序，因此 pos 从 0 开始处理，当处理完所有的 tasks，模拟结束）

具体来说：

1. 如果任务队列没有任务，那么直接将 time 快进到下一个任务的开始时间 ，这样可以减少时间复杂度。
2. 将 time 之前开始的任务全部加入到任务队列中，表示这些任务都可以被处理了。
3. 从任务队列中取出一个时间最短的进行处理。（这是题目要求的）
4. 重复 1 - 3 直到 n 个任务都被处理完毕。

## 关键点

- 堆

## 代码

- 语言支持：Python3，JS，Java，CPP

Python3 Code:

```python
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(task[0], i, task[1]) for i, task in enumerate(tasks)]
        tasks.sort()
        backlog = []
        time = 0
        ans = []
        pos = 0
        for _ in tasks:
            if not backlog:
                time = max(time, tasks[pos][0])
            while pos < len(tasks) and tasks[pos][0] <= time:
                heapq.heappush(backlog, (tasks[pos][2], tasks[pos][1]))
                pos += 1
            d, j = heapq.heappop(backlog)
            time += d
            ans.append(j)
        return ans
```

**复杂度分析**

令 n 为数组长度。

- 时间复杂度：O(nlogn)
- 空间复杂度：O(n)
