# [Python] SortedList

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 7
> Tags: Python, Python3

---

### 解题思路
核心思路就是使用有序序列维护题目要求的各种东西

### 代码

```python3
from sortedcontainers import SortedList


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.n = n
        self.movies = defaultdict(SortedList)
        self.shops = defaultdict(dict)
        self.renting = SortedList([])
        for shop, movie, price in entries:
            self.movies[movie].add((price, shop))
            self.shops[shop][movie] = price      

    def search(self, movie: int) -> List[int]:
        return [i[1] for i in list(self.movies[movie].islice(stop=5))]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shops[shop][movie]
        self.movies[movie].discard((price,shop))
        self.renting.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price= self.shops[shop][movie]
        self.movies[movie].add((price,shop))
        self.renting.discard((price, shop, movie))

    def report(self) -> List[List[int]]:
        return [[x,y] for _,x,y in self.renting.islice(stop=5)]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
```