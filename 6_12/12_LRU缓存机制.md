# 题目地址(146. LRU 缓存机制)

https://leetcode-cn.com/problems/lru-cache/

## 标签

- 哈希表
- 链表

## 难度

- 困难

## 入选理由

1. 书写难度较大，当压轴题

## 哈希表+双向链表

### 思路

首先简单介绍下什么是 LRU 缓存，熟悉的可以跳过。

假设我们有一个玩具摊位，用于向顾客展示小玩具。玩具很多，摊位大小有限，不能一次性展示所有玩具，于是大部分玩具放在了仓库里。

![img](https://p.ipic.vip/iv5f2i.jpg)

如果有顾客来咨询某个玩具，我们就去仓库把该玩具拿出来，摆在摊位上。

![img](https://p.ipic.vip/ok23uf.jpg)

因为摊位最上面的位置最显眼，所以我们总是把最新拿出来的玩具放在那。

![img](https://p.ipic.vip/etqt8y.jpg)

不过由于摊位大小有限，很快就摆满了，这时如果又有顾客想看新玩具。

![img](https://p.ipic.vip/ibx9jj.jpg)

我们只能把摊位最下面的玩具拿回仓库(因为最下面的位置相对没那么受欢迎)，然后其他玩具往下移，腾出最上面的位置来放新玩具。

![img](https://p.ipic.vip/41y180.jpg)

如果顾客想看的玩具就摆在摊位上，我们就可以把这个玩具直接移到摊位最上面的位置，其他的玩具就要往下挪挪位置了。还记得我们的规则吧，最近有人询问的玩具要摆在最上面显眼的位置。

![img](https://p.ipic.vip/079qov.jpg)

这就是对 LRU 缓存的一个简单解释。回到计算机问题上面来，玩具摊位代表的就是缓存空间，我们首先需要考虑的问题是使用哪种数据结构来表示玩具摊位，以达到题目要求的时间复杂度。

**数组？**

如果选择数组，因为玩具在摊位上的位置会挪来挪去，这个操作的时间复杂度是O(N)O(N)，不符合题意，pass。

**链表？**

- 如果选择链表，在给定节点后新增节点，或者移除给定节点的时间复杂度是 O(1)O(1)。但是，链表查找节点的时间复杂度是 O(N)O(N)，同样不符合题意，不过还有办法补救。
- 在玩具摊位的例子中，我们是手动移动玩具，人类只需要看一眼就知道要找的玩具在哪个位置上，但计算机没那么聪明，因此还需要给它一个脑子(哈希表)来记录什么玩具在什么位置上，也就是要用一个哈希表来记录每个 key 对应的链表节点引用。这样查找链表节点的时间复杂度就降到了 O(1)O(1)，不过代价是空间复杂度增加到了 O(N)O(N)。
- 另外，由于移除链表节点后还需要把该节点前后的两个节点连起来，因此我们需要的是双向链表而不是单向链表。

伪代码：

```
// put

if key 存在:
    更新节点值
    把节点移到链表头部

else:
    if 缓存满了:
        移除最后一个节点
        删除它在哈希表中的映射

    新建一个节点
    把节点加到链表头部
    在哈希表中增加映射


// get

if key 存在:
    返回节点值
    把节点移到链表头部
else:
    返回 -1
```

### 代码

代码支持：JS， Java，CPP, Python

Python Code:

手写版本：

```python
# 创建双向链表
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # 构建首尾节点, 使之相连
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.lookup = dict()
        self.max_len = capacity

    def get(self, key: int) -> int:
        if key in self.lookup:
            node = self.lookup[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            self.remove(self.lookup[key])
        if len(self.lookup) == self.max_len:
            # 把表头位置节点删除(说明最近的数据值)
            self.remove(self.head.next)
        self.add(Node(key, value))
    # 删除链表节点
    def remove(self, node):
        del self.lookup[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
    # 加在链表尾
    def add(self, node):
        self.lookup[node.key] = node
        pre_tail = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        pre_tail.next = node
        node.prev = pre_tail
```

直接调用库版本：

```python
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.lrucache = OrderedDict()

    def get(self, key: int) -> int:
        # 说明在缓存中,重新移动字典的尾部
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        return self.lrucache.get(key, -1)
        
        

    def put(self, key: int, value: int) -> None:
        # 如果存在,删掉,重新赋值
        if key in self.lrucache:
            del self.lrucache[key]
        # 在字典尾部添加
        self.lrucache[key] = value
        if len(self.lrucache) > self.maxsize:
            # 弹出字典的头部(因为存储空间不够了)
            self.lrucache.popitem(last = False)
```

**复杂度分析**

- 时间复杂度：各种操作平均都是 O(1)O(1)。
- 空间复杂度：链表占用空间 O(N)O(N)，哈希表占用空间也是 O(N)O(N)，因此总的空间复杂度为 O(N)O(N)，其中 N 为容量大小，也就是题目中的 capacity。

上一页下一页
