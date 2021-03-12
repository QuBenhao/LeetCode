import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        command, obstacles, x, y = test_input
        return self.robot(str(command), [o[:] for o in obstacles], x, y)

    def robot(self, command, obstacles, x, y):
        """
        :type command: str
        :type obstacles: List[List[int]]
        :type x: int
        :type y: int
        :rtype: bool
        """
        def find(x_, y_):
            times = min(x_//cx,y_//cy)
            return (x_ - times * cx,y_ - times * cy) in path

        cx, cy = 0, 0
        path = set()
        path.add((cx,cy))
        for c in command:
            if c == 'U':
                cy += 1
            else:
                cx += 1
            path.add((cx,cy))

        if not find(x, y):
            return False

        for o in obstacles:
            if o[0] <= x and o[1] <= y:
                if find(o[0],o[1]):
                    return False

        return True
