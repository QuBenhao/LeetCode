import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxGroupNumber(list(test_input))

    def maxGroupNumber(self, tiles):
        """
        :type tiles: List[int]
        :rtype: int
        """
        # counts = Counter(tiles)
        # # dp[x][y] 表示
        # # 在预留x张(tile-2)和y张(tile-1)的前提下，
        # # (tile)之前的牌能组成的牌组数
        # dp = [[-1] * 5 for _ in range(5)]
        # dp[0][0] = 0
        # prev_tile = 0 # 前一张牌的点数
        # # 每三个相同的顺子可以替换成三组的刻子，所以考虑组成的顺子数为0,1,2
        # for tile in sorted(counts.keys()):
        #     cnt = counts[tile]
        #     # 如果上一张牌和这张牌没法练起来，
        #     # 意味着无论之前留几张牌，都无法和tile组成数字，
        #     # 只能保留dp[0][0]，即一张不留的最大结果
        #     # 相当于在这里递归了maxGroupNumber
        #     if prev_tile != tile - 1:
        #         ldp = dp[0][0]
        #         dp = [[-1] * 5 for _ in range(5)]
        #         dp[0][0] = ldp
        #     # 新的dp数组
        #     new_dp = [[-1] * 5 for _ in range(5)]
        #     for cnt_2 in range(0, 5): # (tile-2)的牌数
        #         for cnt_1 in range(0, 5): # (tile-1)的牌数
        #             # 如果牌数不够
        #             if dp[cnt_2][cnt_1] < 0:
        #                 continue
        #             # 顺子的数量为三者最多的最小值且小于等于2
        #             for sz in range(0, min(cnt_2, cnt_1, cnt) + 1):
        #                 new_2 = cnt_1 - sz # 当前的_1是下一个的_2
        #                 for new_1 in range(0, min(4, cnt - sz) + 1):
        #                     new_dp[new_2][new_1] = max(new_dp[new_2][new_1],
        #                                                dp[cnt_2][cnt_1] + sz +(cnt - sz -new_1)//3)
        #     dp = new_dp
        #     prev_tile = tile
        #
        # return max(max(i) for i in dp)

        tiles = Counter(tiles)
        nums = sorted(tiles)
        dp = {(0, 0): 0}
        for num in nums:
            v0, v1 = tiles[num], tiles[num+1]
            new_dp = Counter()
            for (d0, d1), c in dp.items():
                t0, t1 = v0 - d0, v1 - d1
                for d in range(min(t0, t1, 2) + 1):
                    k = (d1 + d, d)
                    new_dp[k] = max(new_dp[k], c + d + (t0 - d) // 3)
            dp = new_dp
        return max(dp.values())
