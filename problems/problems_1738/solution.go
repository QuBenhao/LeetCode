package problem1738

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func kthLargestValue(matrix [][]int, k int) int {
	m, n := len(matrix), len(matrix[0])
	a := make([]int, 0, m*n) // 预分配空间
	colSum := make([]int, n)
	for _, row := range matrix {
		s := 0
		for j, x := range row {
			colSum[j] ^= x
			s ^= colSum[j]
			a = append(a, s)
		}
	}
	slices.Sort(a)
	return a[len(a)-k]
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var matrix [][]int
	var k int

	if err := json.Unmarshal([]byte(values[0]), &matrix); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &k); err != nil {
		log.Fatal(err)
	}

	return kthLargestValue(matrix, k)
}
