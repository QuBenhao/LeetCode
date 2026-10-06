# [Python] BFS

> Author: Benhao
> Date: 2024-03-02
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [909. 蛇梯棋](https://leetcode.cn/problems/snakes-and-ladders/description/)

[TOC]

# Intuition

> Run standard BFS from the start to find the fewest jumps to the destination

# Approach

> Snakes and ladders cannot be chained. If a jump lands on another snake or ladder, do not mark that square visited; only landing there via a die roll counts

# Complexity

Time complexity:
> $O(n^2)$

Space complexity:
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
                # If all squares are empty, only take the farthest jump
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
                        # Ladders cannot be chained, so a destination square with a snake or ladder can still be reached another way; do not mark it
                        #explored.add(board[x][y] - 1)
                        queue.append(board[x][y] - 1)
                    elif not already:
                        already = True
                        queue.append(nxt)
        return -1
```
  
