# [Python] BFS

> Author: Benhao
> Date: 2024-03-02
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [909. 蛇梯棋](https://leetcode.cn/problems/snakes-and-ladders/description/)

[TOC]

# 思路

> 从起点标准的BFS看最早到终点的跳跃次数

# 解题方法

> 注意不能连续跳跃蛇梯，所以跳跃后的位置如果有蛇梯，不能标记为走过，必须是骰子走过才算

# 复杂度

时间复杂度:
> $O(n^2)$

空间复杂度:
> $O(n^2)$



# Code
```Python3 []
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        total = n * n - 1
        def trans(x):
            d = x // n
            return n - 1 - d, n - 1 - x % n if d % 2 else x % n

        ans = 0
        explored = set()
        queue = deque([0])
        while queue:
            length = len(queue)
            ans += 1
            for _ in range(length):
                cur = queue.popleft()
                # 如果都是空地，就跳最远的那一次即可
                already = False
                for nxt in range(min(total, cur + 6), cur, -1):
                    if nxt == total:
                        return ans
                    if nxt in explored:
                        continue
                    explored.add(nxt)
                    x, y = trans(nxt)
                    if board[x][y] != -1:
                        if board[x][y] - 1 == total:
                            return ans
                        # 不能连续跳梯子，所以下一个点如果是蛇梯，还可以以其他方式走，所以不标记
                        #explored.add(board[x][y] - 1)
                        queue.append(board[x][y] - 1)
                    elif not already:
                        already = True
                        queue.append(nxt)
        return -1
```
  
