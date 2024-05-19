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

        # # 转换orders为，所有订单里的全部桌和全部食物
        # obj = list(zip(*orders))
        # # 排序好的tables，每个table对应结果数组中的第几行
        # tables = SortedDict({v:i for i,v in enumerate(sorted(map(int,set(obj[1]))), 1)})
        # # 排序好的foods，每个food对应结果数组中的第几列
        # foods = SortedDict({v:i for i,v in enumerate(sorted(set(obj[2])), 1)})
        # # 结果数组的第一行
        # res = [["Table"] + [food for food in foods]] + [[str(key)] + ["0"] * len(foods) for key in tables]
        # # 统计每桌每个食物的数量
        # for _, table, food in orders:
        #     res[tables[int(table)]][foods[food]] = str(int(res[tables[int(table)]][foods[food]]) + 1)
        # return res

        tables, foods = set(), set()
        for _, table, food in orders:
            tables.add(table)
            foods.add(food)
        foods = sorted(foods)
        tables = sorted(tables, key=int)
        res = [["Table"] + foods] + [[tables[i]] + ["0"] * len(foods) for i in range(len(tables))]
        tables = {v:i for i,v in enumerate(tables, 1)}
        foods = {v:i for i,v in enumerate(foods, 1)}

        for _, table, food in orders:
            res[tables[table]][foods[food]] = str(int(res[tables[table]][foods[food]]) + 1)
        return res
