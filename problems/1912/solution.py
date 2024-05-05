import solution
from collections import defaultdict
from sortedcontainers import SortedList
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        # Your MovieRentingSystem object will be instantiated and called as such:
        obj = MovieRentingSystem(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class MovieRentingSystem(object):

    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        self.movies = defaultdict(SortedList)
        self.shops = defaultdict(dict)
        self.renting = SortedList([])
        for shop, movie, price in entries:
            self.movies[movie].add((price, shop))
            self.shops[shop][movie] = price

    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        return [i[1] for i in list(self.movies[movie].islice(stop=5))]

    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price = self.shops[shop][movie]
        self.movies[movie].discard((price, shop))
        self.renting.add((price, shop, movie))

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        price = self.shops[shop][movie]
        self.movies[movie].add((price, shop))
        self.renting.discard((price, shop, movie))

    def report(self):
        """
        :rtype: List[List[int]]
        """
        return [[x,y] for _,x,y in self.renting.islice(stop=5)]
