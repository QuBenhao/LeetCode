package problem1572

import (
	"encoding/json"
	"log"
	"strings"
)

func diagonalSum(mat [][]int) (ans int) {
	n := len(mat)
	for i := 0; i < n; i++ {
		ans += mat[i][i] + mat[i][n-1-i]
	}
	if n%2 == 1 {
		ans -= mat[n/2][n/2]
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var mat [][]int

	if err := json.Unmarshal([]byte(values[0]), &mat); err != nil {
		log.Fatal(err)
	}

	return diagonalSum(mat)
}
