import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canReorderDoubled(test_input.copy())

    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        def resolve(flag, val):
            count = 0
            while flag.get(val * 2, 0) > 0:
                # print(val)
                if val == 0:
                    c = flag[val] / 2
                    flag[val] -= 2 * c
                    return 2 * c
                c = min(flag[val], flag[val * 2])
                flag[val] -= c
                flag[val * 2] -= c
                val *= 2
                count += 2 * c
            return count

        flag = {}
        total = len(A)
        for val in A:
            if val in flag:
                flag[val] = flag[val] + 1
            else:
                flag[val] = 1

        for val in flag.keys():
            if val == 0 or val % 2 or val / 2 not in flag:
                total -= resolve(flag, val)
        if total > 0:
            return False

        return True

    # def canReorderDoubled(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: bool
    #     """
    #     A.sort()
    #
    #     left = right = 0
    #     while right < len(A):
    #         if A[left] == 0:
    #             if left != right and A[right] == 0:
    #                 A.pop(right)
    #                 A.pop(left)
    #                 right -= 1
    #             else:
    #                 right += 1
    #         elif A[left] < 0:
    #             if A[left]%2 != 0:
    #                 break
    #             elif A[right] == A[left]//2:
    #                 A.pop(right)
    #                 A.pop(left)
    #                 right -= 1
    #             else:
    #                 right += 1
    #         else:
    #             if A[right] == A[left] * 2:
    #                 A.pop(right)
    #                 A.pop(left)
    #                 right -= 1
    #             else:
    #                 right += 1
    #     if not A:
    #         return True
    #     return False
