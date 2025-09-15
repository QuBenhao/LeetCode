# N皇后

```python3
def total_n_queens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """

    # queens[i] means the column position for queen at i-1 th row
    # lu_rd: left up corner to right down corner
    # ld_ru: left down corner to right up corner
    def dfs(queens, lu_rd, ld_ru):
        row = len(queens)
        if row == n:
            nonlocal ans
            ans += 1
            return
        for col in range(n):
            if col not in queens and col - row not in lu_rd and row + col not in ld_ru:
                queens.add(col)
                lu_rd.add(col - row)
                ld_ru.add(row + col)
                dfs(queens, lu_rd, ld_ru)
                queens.remove(col)
                lu_rd.remove(col - row)
                ld_ru.remove(row + col)

    ans = 0
    dfs(set(), set(), set())
    return ans
```

```go
package main

func totalNQueens(n int) (ans int) {
	cols := map[int]any{}
	rowCols := map[int]any{}
	colRows := map[int]any{}

	var backtrack func()
	backtrack = func() {
		r := len(cols)
		if r == n {
			ans++
			return
		}
		for c := 0; c < n; c++ {
			if _, ok := cols[c]; ok {
				continue
			}
			rc := r + c
			if _, ok := rowCols[rc]; ok {
				continue
			}
			cr := r - c
			if _, ok := colRows[cr]; ok {
				continue
			}
			cols[c] = nil
			rowCols[rc] = nil
			colRows[cr] = nil
			backtrack()
			delete(cols, c)
			delete(rowCols, rc)
			delete(colRows, cr)
		}
	}
	backtrack()
	return
}
```
