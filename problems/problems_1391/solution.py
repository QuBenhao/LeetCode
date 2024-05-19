import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hasValidPath([x[:] for x in test_input])

    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """

        def is_connect(curr_street, next_street, dirction):
            # 0 down: up -> down
            # 1 left: right -> left
            # 2 up: down -> up
            # 3 right: left -> right
            if dirction == 0:
                if curr_street == 2 or curr_street == 3 or curr_street == 4:
                    if next_street == 2:
                        return 0
                    if next_street == 5:
                        return 1
                    if next_street == 6:
                        return 3
            elif dirction == 1:
                if curr_street == 1 or curr_street == 3 or curr_street == 5:
                    if next_street == 1:
                        return 1
                    if next_street == 4:
                        return 0
                    if next_street == 6:
                        return 2
            elif dirction == 2:
                if curr_street == 2 or curr_street == 5 or curr_street == 6:
                    if next_street == 2:
                        return 2
                    if next_street == 3:
                        return 1
                    if next_street == 4:
                        return 3
            else:
                if curr_street == 1 or curr_street == 4 or curr_street == 6:
                    if next_street == 1:
                        return 3
                    if next_street == 3:
                        return 0
                    if next_street == 5:
                        return 2
            return -1

        def search(curr_dirction):
            curr_x = curr_y = 0
            explored = set()
            explored.add((curr_x,curr_y))
            while curr_x != m - 1 or curr_y != n - 1:
                if curr_dirction == -1:
                    return False
                elif curr_dirction == 0:
                    next_x = curr_x + 1
                    next_y = curr_y
                elif curr_dirction == 1:
                    next_x = curr_x
                    next_y = curr_y - 1
                elif curr_dirction == 2:
                    next_x = curr_x - 1
                    next_y = curr_y
                else:
                    next_x = curr_x
                    next_y = curr_y + 1
                if 0 <= next_x < m and 0 <= next_y < n and (next_x,next_y) not in explored:
                    curr_dirction = is_connect(grid[curr_x][curr_y], grid[next_x][next_y], curr_dirction)
                    curr_x = next_x
                    curr_y = next_y
                    explored.add((curr_x,curr_y))
                else:
                    return False
            if curr_dirction == -1:
                return False
            return True

        m = len(grid)
        n = len(grid[0])
        curr_dirction = grid[0][0]
        if curr_dirction == 1 or curr_dirction == 6:
            curr_dirction = 3
        elif curr_dirction == 2 or curr_dirction == 3:
            curr_dirction = 0
        elif curr_dirction == 5:
            if m == n == 1:
                return True
            return False
        else:
            return search(0) or search(3)
        return search(curr_dirction)
