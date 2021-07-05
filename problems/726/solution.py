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
        #             # 获取完整的数字，并解析出对应的数值
        #             j = i
        #             while j < n and str.isdigit(formula[j]):
        #                 j += 1
        #             cnt = int(formula[i:j])
        #             i = j
        #             # 如果栈顶元素是 )，说明当前数值可以应用给「连续一段」的原子中
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
        #             # 如果栈顶元素不是 )，说明当前数值只能应用给栈顶的原子
        #             else:
        #                 cur = d.pop()
        #                 map[cur] *= cnt
        #                 d.append(cur)
        #         else:
        #             # 获取完整的原子名
        #             j = i + 1
        #             while j < n and str.islower(formula[j]):
        #                 j += 1
        #             cur = formula[i:j] + "_" + str(idx)
        #             idx += 1
        #             map[cur] = 1
        #             i = j
        #             d.append(cur)
        #
        # #  将不同编号的相同原子进行合并
        # mm = defaultdict(int)
        # for key, cnt in map.items():
        #     atom = key.split("_")[0]
        #     mm[atom] += cnt
        #
        # # 对mm中的key进行排序作为答案
        # ans = []
        # for key in sorted(mm.keys()):
        #     if mm[key] > 1:
        #         ans.append(key+str(mm[key]))
        #     else:
        #         ans.append(key)
        # return "".join(ans)

        # 倒着的时候， 记录map，乘的基数，迭代中的乘数，个数，个数的10进制位数，元素
        cnts, multiply, muls, num, num_count, atom = defaultdict(int), 1, [], 0, 0, ""
        for c in formula[::-1]:
            if c == ')':
                # 如果当前有统计的数字，乘的基数要叠加
                if num:
                    multiply *= num
                    muls.append(num)
                    num = num_count = 0
                else:
                    muls.append(multiply)
            elif c == '(':
                # 去除掉上一个乘数
                multiply //= muls.pop()
            elif str.isdigit(c):
                num += int(c) * (10 ** num_count)
                num_count += 1
            elif str.islower(c):
                atom += c
            else:
                atom += c
                # 注意我们在更新元素个数时，始终要考虑乘的基数
                if num:
                    cnts[atom[::-1]] += num * multiply
                else:
                    cnts[atom[::-1]] += multiply
                atom = ""
                num = num_count = 0
        return "".join(key if cnts[key] == 1 else key + str(cnts[key]) for key in sorted(cnts.keys()))
