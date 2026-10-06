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

        # # Extract all tables and all foods from orders
        # obj = list(zip(*orders))
        # # Sorted tables: map each table to its row in the result array
        # tables = SortedDict({v:i for i,v in enumerate(sorted(map(int,set(obj[1]))), 1)})
        # # Sorted foods: map each food to its column in the result array
        # foods = SortedDict({v:i for i,v in enumerate(sorted(set(obj[2])), 1)})
        # # First row of the result array
        # res = [["Table"] + [food for food in foods]] + [[str(key)] + ["0"] * len(foods) for key in tables]
        # # Count each food ordered by each table
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
