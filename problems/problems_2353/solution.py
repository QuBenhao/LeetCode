from collections import defaultdict

from sortedcontainers import SortedList

import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = FoodRatings(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(SortedList)  # sortedcontainers
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [rating, cuisine]
            # 取负号，保证 rating 相同时，字典序更小的 food 排在前面
            self.cuisine_map[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.food_map[food]
        sl = self.cuisine_map[cuisine]
        sl.discard((-rating, food))  # 移除旧数据
        sl.add((-newRating, food))  # 添加新数据
        self.food_map[food][0] = newRating  # 更新 food 的 rating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_map[cuisine][0][1]

