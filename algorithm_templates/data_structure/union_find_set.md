# Union-Find

Union-Find is a data structure for merging and querying disjoint sets. It supports two operations:

1. **Find**: Find the set containing an element.
2. **Union**: Merge two sets.

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
        self.cc = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in the same set

        # Union by rank
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
		uf.parent[x] = uf.parent[uf.parent[x]] // Path compression
		x = uf.parent[x]
	}
	return x
}

func (uf *UnionFind) Union(x, y int) bool {
	rootX := uf.Find(x)
	rootY := uf.Find(y)

	if rootX == rootY {
		return false // Already in the same set
	}

	// Union by rank
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
	uf.cc-- // Merging reduces the number of sets
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

## Templates

### Basic
```c++
struct DSU {
    vector<size_t> pa;

    explicit DSU(size_t n) : pa(n) { iota(pa.begin(), pa.end(), 0); }

    size_t find(size_t x);
    void unite(size_t x, size_t y);
};

size_t DSU::find(size_t x) { return pa[x] == x ? x : pa[x] = find(pa[x]); }
void DSU::unite(size_t x, size_t y) { pa[find(x)] = find(y); }
```

### Union by Size
```c++
struct DSU {
    vector<size_t> pa, size;

    explicit DSU(size_t n) : pa(n), size(n, 1) { iota(pa.begin(), pa.end(), 0); }

    size_t find(size_t x);
    void unite(size_t x, size_t y);
};

size_t DSU::find(size_t x) { return pa[x] == x ? x : pa[x] = find(pa[x]); }
void DSU::unite(size_t x, size_t y) {
    x = find(x); y = find(y);
    if (x == y) return;
    if (size[x] < size[y]) swap(x, y);
    pa[y] = x;
    size[x] += size[y];
} 
```

### With Deletion
```c++
struct DSU {
  size_t id;
  std::vector<size_t> pa, size;

  // m is the total number of operations; allocate enough space for reconnections
  explicit DSU(size_t size_, size_t m)
      : id(size_ * 2), pa(size_ * 2 + m), size(size_ * 2 + m, 1) {
    // The first half of size is unused; it only simplifies index calculations
    std::iota(pa.begin(), pa.begin() + size_,
              size_);  // Point i to the virtual node i + size_
    std::iota(pa.begin() + size_, pa.end(), size_);  // Each virtual node points to itself
  }

  size_t find(size_t x) { return pa[x] == x ? x : pa[x] = find(pa[x]); }

  void unite(size_t x, size_t y) {
    x = find(x), y = find(y);
    if (x == y) return;
    if (size[x] < size[y]) std::swap(x, y);
    pa[y] = x;
    size[x] += size[y];
  }

  void erase(size_t x) {
    size_t y = find(x);
    --size[y];
    pa[x] = id++;
  }
};
```
