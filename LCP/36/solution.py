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
        # dp滚动更新，存储的是num的上一个数last_num组成的结尾为last_num+1和结尾为last_num+2的顺子数
        dp = {(0, 0): 0}
        # nums中有断层，或者，假如没有num+2，也就是num+1为最大值的时候,动态规划更新d是否正确？
        # 因为当num遍历到最大值（断层）时，v1必然是0，那么所有大于0的d1都不会出现在最后一轮的d的循环中;
        # 满足条件的只有d1=0的情况，而d1=0的循环中，d也必然是0,新的dp只有(0,0)是有值的,也就是之前d0的分配所组成的最大值;
        # 这也符合实际的逻辑，如果没有tiles里面num+1，那就无法构成num-1,num,num+1的顺子和num,num+1,num+2的顺子
        for num in nums:
            v0, v1 = tiles[num], tiles[num+1]
            new_dp = Counter()
            # 枚举用num-2,num-1,num 和 num-1,num,num+1能组成的顺子中,num和num+1的使用情况
            for (d0, d1), c in dp.items():
                # 枚举所有num和num+1已经使用的情况
                t0, t1 = v0 - d0, v1 - d1
                for d in range(min(t0, t1, 2) + 1):
                    # num+1变为下一个num,num+1使用情况为:原来使用的 d1 + 当前组成新的顺子使用的 d
                    # num+2要使用掉 d
                    k = (d1 + d, d)
                    # 动态规划, k的使用情况的最大结果为 原来凑成的顺子数 + 新凑出的顺子数 + 剩余num可以组成的刻子数
                    # 到这里所有num能使用的情况已经枚举完毕，剩余的num必然是按刻子分
                    # 当前num的使用：
                    # 组成d0-d1个num-2,num-1,num的顺子，
                    # 组成d1个num-1,num,num+1的顺子，
                    # 组成d个num,num+1,num+2个顺子
                    new_dp[k] = max(new_dp[k], c + d + (t0 - d) // 3)
            dp = new_dp
        return max(dp.values())
