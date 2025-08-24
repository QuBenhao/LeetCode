package problem498

import (
	"encoding/json"
	"log"
	"strings"
)

func findDiagonalOrder(mat [][]int) (ans []int) {
	for m, n, k := len(mat), len(mat[0]), 0; k < m+n-1; k++ {
		if k&1 == 1 {
			for x := max(0, k-n+1); x < min(k+1, m); x++ {
				ans = append(ans, mat[x][k-x])
			}
		} else {
			for x := min(k, m-1); x >= max(0, k-n+1); x-- {
				ans = append(ans, mat[x][k-x])
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var mat [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &mat); err != nil {
		log.Fatal(err)
	}

	return findDiagonalOrder(mat)
}
