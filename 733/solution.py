import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        image, sr, sc, newColor = test_input
        return self.floodFill(list(image), sr, sc, newColor)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])
        color = image[sr][sc]
        explored = set()

        def dfs(r, c):
            if image[r][c] != color:
                return

            image[r][c] = newColor
            explored.add((r,c))
            if r < rows - 1 and (r+1,c) not in explored:
                dfs(r + 1, c)
            if r > 0 and (r-1,c) not in explored:
                dfs(r - 1, c)
            if c < cols - 1 and (r,c+1) not in explored:
                dfs(r, c + 1)
            if c > 0 and (r,c-1) not in explored:
                dfs(r, c - 1)

        if color != newColor:
            dfs(sr, sc)
        return image
