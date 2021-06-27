import solution
from collections import defaultdict
from sortedcontainers import SortedList


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, vals = test_input
        n, entries = vals[0]
        # Your MovieRentingSystem object will be instantiated and called as such:
        obj = MovieRentingSystem(n, entries)
        ans = [None]
        for i in range(1, len(ops)):
            if ops[i] == "search":
                ans.append(obj.search(vals[i][0]))
            elif ops[i] == "rent":
                obj.rent(vals[i][0], vals[i][1])
                ans.append(None)
            elif ops[i] == "drop":
                obj.drop(vals[i][0], vals[i][1])
                ans.append(None)
            else:
                ans.append(obj.report())
        return ans


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
