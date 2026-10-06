import solution
from collections import defaultdict, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countOfAtoms(str(test_input))

    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        # n = len(formula)
        # map = defaultdict(lambda: 1)
        # d = deque([])
        # i = idx = 0
        # while i < n:
        #     c = formula[i]
        #     if c == '(' or c == ')':
        #         d.append(c)
        #         i += 1
        #     else:
        #         if str.isdigit(c):
        #             # Read the complete number and parse its value
        #             j = i
        #             while j < n and str.isdigit(formula[j]):
        #                 j += 1
        #             cnt = int(formula[i:j])
        #             i = j
        #             # If the stack top is ), this value applies to a consecutive group of atoms
        #             if d and d[-1] == ')':
        #                 tmp = []
        #                 d.pop()
        #                 while d and d[-1] != '(':
        #                     cur = d.pop()
        #                     map[cur] *= cnt
        #                     tmp.append(cur)
        #                 d.pop()
        #
        #                 for k in range(len(tmp) - 1, -1, -1):
        #                     d.append(tmp[k])
        #             # Otherwise, this value applies only to the atom at the stack top
        #             else:
        #                 cur = d.pop()
        #                 map[cur] *= cnt
        #                 d.append(cur)
        #         else:
        #             # Read the complete atom name
        #             j = i + 1
        #             while j < n and str.islower(formula[j]):
        #                 j += 1
        #             cur = formula[i:j] + "_" + str(idx)
        #             idx += 1
        #             map[cur] = 1
        #             i = j
        #             d.append(cur)
        #
        # # Merge identical atoms with different indices
        # mm = defaultdict(int)
        # for key, cnt in map.items():
        #     atom = key.split("_")[0]
        #     mm[atom] += cnt
        #
        # # Sort the keys in mm to construct the answer
        # ans = []
        # for key in sorted(mm.keys()):
        #     if mm[key] > 1:
        #         ans.append(key+str(mm[key]))
        #     else:
        #         ans.append(key)
        # return "".join(ans)

        # Scan backward while tracking the count map, total multiplier, multiplier stack, count, decimal place, and element name
        cnts, multiply, muls, num, num_count, atom = defaultdict(int), 1, [], 0, 0, ""
        for c in formula[::-1]:
            if c == ')':
                # If a number has been parsed, include it in the total multiplier
                if num:
                    multiply *= num
                    muls.append(num)
                    num = num_count = 0
                else:
                    muls.append(1)
            elif c == '(':
                # Remove the previous multiplier
                multiply //= muls.pop()
            elif str.isdigit(c):
                num += int(c) * (10 ** num_count)
                num_count += 1
            elif str.islower(c):
                atom += c
            else:
                atom += c
                # Always account for the total multiplier when updating an element's count
                if num:
                    cnts[atom[::-1]] += num * multiply
                else:
                    cnts[atom[::-1]] += multiply
                atom = ""
                num = num_count = 0
        return "".join(key if cnts[key] == 1 else key + str(cnts[key]) for key in sorted(cnts.keys()))
