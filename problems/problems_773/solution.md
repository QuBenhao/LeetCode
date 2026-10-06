# [Python] A Star (with concise BFS, 100%)

> Author: Benhao
> Date: 2021-06-25
> Upvotes: 11
> Tags: Python, Python3

---

### Approach
This is the classic 8 puzzle, with two common heuristic functions:
1. The number of misplaced elements;
2. The Manhattan distance from each element to its target position.

The first performs better, so it is used here.
<br>
For an N*M puzzle with odd M, an odd inversion count means there is no solution; see the [proof](https://blog.csdn.net/qq_45458915/article/details/103313671)

### Code

```python3
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Neighbors
        neighbors = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}

        # Manhattan distance
        def ManhattanDist(p1, p2):
            return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

        # State
        class State:
            def __init__(self, b=None, cost=0):
                self.board = b
                self.h = self.heuristic()
                self.g = cost
                # A*, f=h+g
                self.f = self.h + self.g
                self.hash = hash(tuple(self.board))

            def __lt__(self, other):
                return self.f < other.f

            def __eq__(self, other):
                return self.hash == other.hash or self.board == other.board

            def __hash__(self):
                return self.hash

            # Two heuristics
            def heuristic(self):
                # h1
                return sum(1 for i in range(6) if self.board[i] and self.board[i] != i + 1)
                # h2
                # return sum(
                #     ManhattanDist((i // 3, i % 3), ((num - 1) // 3, (num - 1) % 3))
                #     for i, num in enumerate(self.board) if num)

            # Generate the next states by swapping with 0
            def successor(self):
                idx = self.board.index(0)
                successors = []
                for ng in neighbors[idx]:
                    temp = self.board[:]
                    temp[idx] = temp[ng]
                    temp[ng] = 0
                    successors.append(State(temp, self.g + 1))
                return successors

        board = board[0] + board[1]
        # In an n*m puzzle with odd m, inversion parity must match the target state's parity; otherwise there is no solution
        if sum(1 for i in range(6) for j in range(i+1, 6) if board[j] and board[i] > board[j]) % 2 == 1:
            return -1
        initState = State(board)
        pq = [initState]
        explored = {initState}
        # The priority queue is ordered by f=h+g
        while pq:
            state = heapq.heappop(pq)
            if state.board == [1, 2, 3, 4, 5, 0]:
                return state.g
            for successor in state.successor():
                if successor not in explored:
                    explored.add(successor)
                    heapq.heappush(pq, successor)
        return -1
```
Standard BFS
```python3
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        neighbors = {0: (1, 3), 1: (0, 2, 4), 2: (1, 5), 3: (0, 4), 4: (1, 3, 5), 5: (2, 4)}

        start = tuple(board[0] + board[1])
        target = tuple([1,2,3,4,5,0])
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            node,depth = queue.popleft()
            if node == target:
                return depth
            pos = node.index(0)
            for i in neighbors[pos]:
                newboard = list(node)
                newboard[pos] = newboard[i]
                newboard[i] = 0
                nb = tuple(newboard)
                if nb not in seen:
                    seen.add(nb)
                    queue.append((nb,depth+1))
        return -1
```
