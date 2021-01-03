import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countArrangement(test_input)

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [i for i in range(1,n+1)]
        available = [[] for i in range(n)]
        self.count = 0

        for i in range(n):
            for n in nums:
                if n >= (i+1) and n % (i+1) == 0:
                    available[i].append(n)
                elif (i+1) % n == 0:
                    available[i].append(n)
        available.sort(key=lambda x:len(x))

        def dfs(available,left_nums):
            if not available or not left_nums:
                self.count += 1
                return
            for num in available[0]:
                if num in left_nums:
                    t = [x[:] for x in available]
                    t.pop(0)
                    for arr in t:
                        if num in arr:
                            arr.remove(num)
                    t.sort(key=lambda x:len(x))
                    temp = list(left_nums)
                    temp.remove(num)

                    dfs(t,temp)

        dfs([x[:] for x in available],nums)
        return self.count

        # import collections
        # nums = [i for i in range(1,n+1)]
        # # arr = [0] * n
        # available = collections.defaultdict(list)
        # self.count = 0
        #
        # for i in range(n):
        #     for n in nums:
        #         if n >= (i+1) and n % (i+1) == 0:
        #             available[i].append(n)
        #         elif (i+1) % n == 0:
        #             available[i].append(n)
        #
        # def dfs(index,left_nums):
        #     if index == n and not left_nums:
        #         self.count += 1
        #         return
        #     for num in available[index]:
        #         if num in left_nums:
        #             temp = list(left_nums)
        #             temp.remove(num)
        #             dfs(index+1,temp)
        # dfs(0,nums)
        # return self.count
