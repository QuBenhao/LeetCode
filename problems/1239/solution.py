import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxLength(list(test_input))

    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        # 预处理数据, 去掉带有重复字符的字符串
        arr = [t for s in arr if len(t := set(s)) == len(s)]
        # 启发式预估最大的结果
        predict = len(set().union(*arr))
        n = len(arr)
        self.curr = set()
        self.ans = 0

        def dfs(idx):
            # 更新当前背包中的长度到答案
            self.ans = max(self.ans, len(self.curr))
            # 找到能拼接出最大可能结果的结果了，不需要继续搜索 或者 当前的背包加上后面最长的结果都无法超过当前的答案了，不需要继续搜索
            if self.ans == predict or idx == n or len(self.curr) + len(set().union(*arr[idx:])) < self.ans:
                return
            # 从idx到n,根据回溯寻找当前01背包和后面组成的最大值
            for i in range(idx, n):
                # 当前背包与arr[idx]不冲突
                if not self.curr & arr[i]:
                    # 加入背包, A+B
                    self.curr |= arr[i]
                    # 判断新的背包的最大值
                    dfs(i + 1)
                    # 回溯继续寻找最大值, (A+B) - B
                    self.curr ^= arr[i]

        dfs(0)
        return self.ans
