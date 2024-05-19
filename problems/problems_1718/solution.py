import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.constructDistancedSequence(test_input)

    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def fill(curr_list, left_index, left_nums):
            if not left_index:
                return curr_list

            ans = []
            for num in left_nums:
                if num == 1:
                    temp = list(curr_list)
                    temp_ = list(left_index)
                    _temp = list(left_nums)
                    i = temp_.pop(0)
                    _temp.remove(num)
                    temp[i] = num
                    ans = fill(temp, temp_, _temp)
                else:
                    if left_index[0] + num in left_index:
                        temp = list(curr_list)
                        temp_ = list(left_index)
                        _temp = list(left_nums)
                        i = temp_.pop(0)
                        temp_.remove(i + num)
                        _temp.remove(num)
                        temp[i] = num
                        temp[i + num] = num
                        ans = fill(temp, temp_, _temp)
                if ans:
                    return ans
            return ans

        curr = [0] * (2 * n - 1)
        left_i = [i for i in range(2 * n - 1)]
        left_n = [i for i in range(n, 0, -1)]
        return fill(curr, left_i, left_n)
