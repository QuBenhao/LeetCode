import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        code, k = test_input
        return self.decrypt(list(code), k)

    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """
        # n = len(code)
        # ans = [0] * n
        # if not k:
        #     return ans
        # for i in range(n):
        #     for j in range(abs(k)):
        #         ans[i] += code[(i + j + 1) % n] if k > 0 else code[(i - j - 1) % n]
        # return ans

        n = len(code)
        ans = [0] * n
        if not k:
            return ans
        ng = k < 0
        if k < 0:
            k = -k
        s = sum(code[:k])
        count = 0
        if ng:
            left = 0
            right = k
        else:
            left = n - 1
            right = k - 1
        if ng:
            ans[k] = s
            while count < n - 1:
                s -= code[left]
                s += code[right]
                left = (left + 1) % n
                right = (right + 1) % n
                ans[right] = s
                count += 1
        else:
            ans[-1] = s
            while count < n - 1:
                s += code[left]
                s -= code[right]
                left = (left - 1) % n
                right = (right - 1) % n
                ans[left] = s
                count += 1
        return ans
