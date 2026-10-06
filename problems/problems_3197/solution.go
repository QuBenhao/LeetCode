package problem3197

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minimumArea(a [][]int) [][]int {
	m, n := len(a), len(a[0])
	// f[i+1][j+1] is the minimum rectangle area covering all ones in the subrectangle with top-left corner (0,0) and bottom-right corner (i,j)
	f := make([][]int, m+1)
	for i := range f {
		f[i] = make([]int, n+1)
	}
	type data struct{ top, left, right int }
	border := make([]data, n)
	for j := range border {
		border[j].top = -1 // None
	}

	for i, row := range a {
		left, right := -1, 0
		for j, x := range row {
			if x > 0 {
				if left < 0 {
					left = j
				}
				right = j
			}
			preB := border[j]
			if left < 0 { // This row contains only zeros so far
				f[i+1][j+1] = f[i][j+1] // Same as the result above
			} else if preB.top < 0 { // This row contains a 1; everything above is 0
				f[i+1][j+1] = right - left + 1
				border[j] = data{i, left, right}
			} else { // Both this row and the area above contain a 1
				l, r := min(preB.left, left), max(preB.right, right)
				f[i+1][j+1] = (r - l + 1) * (i - preB.top + 1)
				border[j] = data{preB.top, l, r}
			}
		}
	}
	return f
}

func minimumSum(grid [][]int) int {
	ans := math.MaxInt

	solve := func(a [][]int) {
		m, n := len(a), len(a[0])

		// Precompute the columns of the leftmost and rightmost ones in each row to calculate the minimum rectangle area for the middle region
		type pair struct{ l, r int }
		lr := make([]pair, m)
		for i, row := range a {
			l, r := -1, 0
			for j, x := range row {
				if x > 0 {
					if l < 0 {
						l = j
					}
					r = j
				}
			}
			lr[i] = pair{l, r}
		}

		// lt[i+1][j+1] = minimum rectangle area covering all ones in the subrectangle with top-left corner (0,0) and bottom-right corner (i,j)
		lt := minimumArea(a)
		a = rotate(a)
		// lb[i][j+1] = minimum rectangle area covering all ones in the subrectangle with bottom-left corner (m-1,0) and top-right corner (i,j)
		lb := rotate(rotate(rotate(minimumArea(a))))
		a = rotate(a)
		// rb[i][j] = minimum rectangle area covering all ones in the subrectangle with bottom-right corner (m-1,n-1) and top-left corner (i,j)
		rb := rotate(rotate(minimumArea(a)))
		a = rotate(a)
		// rt[i+1][j] = minimum rectangle area covering all ones in the subrectangle with top-right corner (0,n-1) and bottom-left corner (i,j)
		rt := rotate(minimumArea(a))

		if m >= 3 {
			for i := 1; i < m; i++ {
				left, right, top, bottom := n, 0, m, 0
				for j := i + 1; j < m; j++ {
					if p := lr[j-1]; p.l >= 0 {
						left = min(left, p.l)
						right = max(right, p.r)
						top = min(top, j-1)
						bottom = j - 1
					}
					// Top-left case in the diagram
					area := lt[i][n]                                // minimumArea(a[:i], 0, n)
					area += (right - left + 1) * (bottom - top + 1) // minimumArea(a[i:j], 0, n)
					area += lb[j][n]                                // minimumArea(a[j:], 0, n)
					ans = min(ans, area)
				}
			}
		}

		if m >= 2 && n >= 2 {
			for i := 1; i < m; i++ {
				for j := 1; j < n; j++ {
					// Top-middle case in the diagram
					area := lt[i][n] // minimumArea(a[:i], 0, n)
					area += lb[i][j] // minimumArea(a[i:], 0, j)
					area += rb[i][j] // minimumArea(a[i:], j, n)
					ans = min(ans, area)
					// Top-right case in the diagram
					area = lt[i][j]  // minimumArea(a[:i], 0, j)
					area += rt[i][j] // minimumArea(a[:i], j, n)
					area += lb[i][n] // minimumArea(a[i:], 0, n)
					ans = min(ans, area)
				}
			}
		}
	}

	solve(grid)
	solve(rotate(grid))
	return ans
}

func rotate(a [][]int) [][]int {
	m, n := len(a), len(a[0])
	b := make([][]int, n)
	for i := range b {
		b[i] = make([]int, m)
	}
	for i, row := range a {
		for j, x := range row {
			b[j][m-1-i] = x
		}
	}
	return b
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return minimumSum(grid)
}
