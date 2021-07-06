import solution
from sortedcontainers import SortedSet, SortedDict
from collections import defaultdict, Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.displayTable([x[:] for x in test_input])

    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        # foods = SortedSet()
        # tables = defaultdict(Counter)
        # for name, number, food in orders:
        #     foods.add(food)
        #     tables[number][food] += 1
        # return [["Table"] + [food for food in foods]] + [[table] + [str(tables[table][food]) for food in foods] for
        #                                                  table in sorted(tables.keys(), key=int)]

        # 转换orders为，所有订单里的全部桌和全部食物
        obj = list(zip(*orders))
        # 排序好的tables，每个table对应结果数组中的第几行
        tables = SortedDict({v:i for i,v in enumerate(sorted(map(int,set(obj[1]))), 1)})
        # 排序好的foods，每个food对应结果数组中的第几列
        foods = SortedDict({v:i for i,v in enumerate(sorted(set(obj[2])), 1)})
        res = [[0] * (len(foods) + 1) for _ in range(len(tables) + 1)]
        res[0][0] = "Table"
        # 结果数组的第一行
        for i, food in enumerate(foods.keys(),1):
            res[0][i] = food
        # 统计每桌每个食物的数量
        for _, table, food in orders:
            res[tables[int(table)]][foods[food]] += 1
        # 每行加入桌号，变成str即可
        for i in range(1, len(res)):
            res[i][0] = tables.keys()[i-1]
            res[i] = list(map(str, res[i]))
        return res
