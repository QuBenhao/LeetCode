package problem661

import (
	"encoding/json"
	"log"
	"strings"
)

func imageSmoother(img [][]int) [][]int {
	m, n := len(img), len(img[0])
	prefixSum := make([][]int, m+1)
	for i := 0; i <= m; i++ {
		prefixSum[i] = make([]int, n+1)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			prefixSum[i+1][j+1] = prefixSum[i+1][j] + prefixSum[i][j+1] - prefixSum[i][j] + img[i][j]
		}
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			a, b, c, d := max(0, i-1), max(0, j-1), min(m-1, i+1), min(n-1, j+1)
			img[i][j] = (prefixSum[c+1][d+1] + prefixSum[a][b] - prefixSum[c+1][b] - prefixSum[a][d+1]) / ((c - a + 1) * (d - b + 1))
		}
	}
	return img
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var img [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &img); err != nil {
		log.Fatal(err)
	}

	return imageSmoother(img)
}
