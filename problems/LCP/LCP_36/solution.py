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
        # # dp[x][y] represents
        # # the number of groups formed by tiles before (tile),
        # # while reserving x copies of (tile-2) and y copies of (tile-1)
        # dp = [[-1] * 5 for _ in range(5)]
        # dp[0][0] = 0
        # prev_tile = 0 # Value of the previous tile
        # # Three identical runs can be replaced by three triplets, so only 0, 1, or 2 runs need consideration
        # for tile in sorted(counts.keys()):
        #     cnt = counts[tile]
        #     # If the previous tile and this tile cannot connect,
        #     # no number of previously reserved tiles can form a run with tile,
        #     # so keep only dp[0][0], the best result with no tiles reserved
        #     # This is equivalent to recursively calling maxGroupNumber here
        #     if prev_tile != tile - 1:
        #         ldp = dp[0][0]
        #         dp = [[-1] * 5 for _ in range(5)]
        #         dp[0][0] = ldp
        #     # New dp array
        #     new_dp = [[-1] * 5 for _ in range(5)]
        #     for cnt_2 in range(0, 5): # Number of (tile-2) tiles
        #         for cnt_1 in range(0, 5): # Number of (tile-1) tiles
        #             # If there are not enough tiles
        #             if dp[cnt_2][cnt_1] < 0:
        #                 continue
        #             # The number of runs is bounded by the minimum of the three tile counts and by 2
        #             for sz in range(0, min(cnt_2, cnt_1, cnt) + 1):
        #                 new_2 = cnt_1 - sz # The current _1 becomes the next _2
        #                 for new_1 in range(0, min(4, cnt - sz) + 1):
        #                     new_dp[new_2][new_1] = max(new_dp[new_2][new_1],
        #                                                dp[cnt_2][cnt_1] + sz +(cnt - sz -new_1)//3)
        #     dp = new_dp
        #     prev_tile = tile
        #
        # return max(max(i) for i in dp)

        tiles = Counter(tiles)
        nums = sorted(tiles)
        # Roll dp forward across iterations; it stores the counts of runs ending at last_num+1 and last_num+2 formed at last_num, the value before num
        dp = {(0, 0): 0}
        # Is the DP update for d correct when nums has a gap, or when num+2 is absent and num+1 is the largest value?
        # When num reaches the maximum value (or a gap), v1 must be 0, so no positive d1 participates in the final loop over d;
        # only d1=0 is valid, which also forces d=0. The new dp has a value only at (0,0): the best result from the previous allocation of d0;
        # this matches the logic: without num+1 in tiles, neither num-1,num,num+1 nor num,num+1,num+2 can form a run
        for num in nums:
            v0, v1 = tiles[num], tiles[num+1]
            new_dp = Counter()
            # Enumerate how num and num+1 are used in runs num-2,num-1,num and num-1,num,num+1
            for (d0, d1), c in dp.items():
                # Enumerate all existing usage counts of num and num+1
                t0, t1 = v0 - d0, v1 - d1
                for d in range(min(t0, t1, 2) + 1):
                    # num+1 becomes the next num; its usage is the previous d1 plus d used in newly formed runs
                    # Use d copies of num+2
                    k = (d1 + d, d)
                    # DP: the best result for usage state k is the existing group count plus new runs plus triplets formed from the remaining num tiles
                    # All ways to use num in runs have now been enumerated; the remaining num tiles must form triplets
                    # Usage of the current num:
                    # Form d0-d1 runs of num-2,num-1,num,
                    # form d1 runs of num-1,num,num+1,
                    # and form d runs of num,num+1,num+2
                    new_dp[k] = max(new_dp[k], c + d + (t0 - d) // 3)
            dp = new_dp
        return max(dp.values())
