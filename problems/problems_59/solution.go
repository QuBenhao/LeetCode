package problem59

import (
	"encoding/json"
	"log"
	"strings"
)

func generateMatrix(n int) [][]int {
	directions := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	ans := make([][]int, n)
	for i := 0; i < n; i++ {
		ans[i] = make([]int, n)
	}
	num := 1
	for i := 0; i < n/2; i++ {
		ans[i][i] = num
		num++
		x, y := i, i+1
		minBound, maxBound := i-1, n-i
		dIdx := 0
		for x != i || y != i {
			ans[x][y] = num
			num++
			nx, ny := x+directions[dIdx][0], y+directions[dIdx][1]
			if nx <= minBound || nx >= maxBound || ny <= minBound || ny >= maxBound {
				dIdx++
				if dIdx < len(directions) {
					x += directions[dIdx][0]
					y += directions[dIdx][1]
				}
			} else {
				x = nx
				y = ny
			}
		}
	}
	if n%2 == 1 {
		ans[n/2][n/2] = num
	}

	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return generateMatrix(n)
}
