import solution
from collections import defaultdict, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.circularArrayLoop(list(test_input))

    mark = 1001
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            # 已经被检查过了
            if nums[i] >= self.mark:
                continue
            # i为起点, 标记值，以及上一个的值
            cur, tag, last = i, self.mark + i, -1
            # 循环要全正还是全负
            flag = nums[cur] > 0
            while True:
                # 下一个点
                nxt = (cur + nums[cur]) % n
                # 当前的值
                last = nums[cur]
                # 修改数组里为标记过
                nums[cur] = tag
                # 移动到下一个点
                cur = nxt
                # 回到出发点了，可以停止
                if cur == i:
                    break
                # 回到标记过的点了，可以停止
                if nums[cur] >= self.mark:
                    break
                # 以下两种情况为正负相反出现了，不符合题目要求，可以停止
                if flag and nums[cur] < 0:
                    break
                if not flag and nums[cur] > 0:
                    break
            # 如果最后出现的点不是指向他自己的，并且当前的值为当前标记值，我们才认定构成一个要的循环
            if last % n != 0 and nums[cur] == tag:
                return True
        return False

        # n = len(nums)
        # connect = defaultdict(list)
        # marks = deque([])
        # for i, num in enumerate(nums):
        #     nxt = (i + num) % n
        #     connect[nxt].append(i)
        #     if nxt == i or nums[nxt] * num < 0:
        #         marks.append(i)
        #         nums[i] = 0
        # while marks:
        #     i = marks.popleft()
        #     for nxt in connect[i]:
        #         if nums[nxt]:
        #             nums[nxt] = 0
        #             marks.append(nxt)
        # return any(num for num in nums)
