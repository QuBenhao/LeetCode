# 并查集

并查集（Union-Find）是一种数据结构，用于处理一些不交集的合并及查询问题。它支持两种操作：

1. **Find**：查找元素所在的集合。
2. **Union**：合并两个集合。

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        self.cc = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # 路径压缩
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # 已经在同一集合

        # 按秩合并
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_x] = root_y
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_y] += 1
            self.size[root_y] += self.size[root_x]
        self.cc -= 1
        return True

    def is_connected(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)

```

```go
package main

type UnionFind struct {
	parent []int
	rank   []int
	size   []int
	cc     int
}

func NewUnionFind(n int) *UnionFind {
	uf := &UnionFind{
		parent: make([]int, n),
		rank:   make([]int, n),
		size:   make([]int, n),
		cc:     n,
	}
	for i := range uf.parent {
		uf.parent[i] = i
		uf.rank[i] = 1
		uf.size[i] = 1
	}
	return uf
}

func (uf *UnionFind) Find(x int) int {
	for uf.parent[x] != x {
		uf.parent[x] = uf.parent[uf.parent[x]] // 路径压缩
		x = uf.parent[x]
	}
	return x
}

func (uf *UnionFind) Union(x, y int) bool {
	rootX := uf.Find(x)
	rootY := uf.Find(y)

	if rootX == rootY {
		return false // 已经在同一集合
	}

	// 按秩合并
	if uf.rank[rootX] > uf.rank[rootY] {
		uf.parent[rootY] = rootX
		uf.size[rootX] += uf.size[rootY]
	} else {
		uf.parent[rootX] = rootY
		if uf.rank[rootX] == uf.rank[rootY] {
			uf.rank[rootY]++
		}
		uf.size[rootY] += uf.size[rootX]
	}
	uf.cc-- // 合并后集合数减少
	return true
}

func (uf *UnionFind) IsConnected(x, y int) bool {
	return uf.Find(x) == uf.Find(y)
}

func (uf *UnionFind) GetSize(x int) int {
	return uf.size[uf.Find(x)]
}
```
```c++
class UnionFind {
  vector<int> fa;
  vector<int> size;

public:
  int cc;
  explicit UnionFind(int n) : fa(n), size(n, 1), cc(n) {
    for (int i = 0; i < n; i++) {
      fa[i] = i;
    }
  }

  int find(int x) {
    if (fa[x] != x) {
      fa[x] = find(fa[x]);
    }
    return fa[x];
  }

  bool merge(int x, int y) {
    int px = find(x), py = find(y);
    if (px == py) {
      return false;
    }
    fa[px] = py;
    size[py] += size[px];
    cc--;
    return true;
  }

  int get_size(int x) { return size[find(x)]; }
};
```
```java
class UnionFind {
    private int[] parent;
    private int[] size;
    private int count;

    public UnionFind(int n) {
        parent = new int[n];
        size = new int[n];
        count = n;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Path compression
        }
        return parent[x];
    }

    public boolean union(int x, int y) {
        int px = find(x);
        int py = find(y);
        if (px == py) {
            return false; // Already in the same set
        }
        if (size[px] < size[py]) {
            parent[px] = py;
            size[py] += size[px];
        } else {
            parent[py] = px;
            size[px] += size[py];
        }
        count--;
        return true; // Union successful
    }

    public int getCount() {
        return count;
    }

    public int getSize(int x) {
        return size[find(x)];
    }
}
```