package problem1928

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minCost(maxTime int, edges [][]int, passingFees []int) int {
	n := len(passingFees)
	f := make([][]int, maxTime+1)
	for i := range f {
		f[i] = make([]int, n)
		for j := range f[i] {
			f[i][j] = math.MaxInt32
		}
	}
	f[0][0] = passingFees[0]
	for t := 1; t <= maxTime; t++ {
		for _, edge := range edges {
			i, j, cost := edge[0], edge[1], edge[2]
			if cost <= t {
				if f[t-cost][j] != math.MaxInt32 {
					f[t][i] = min(f[t][i], f[t-cost][j]+passingFees[i])
				}
				if f[t-cost][i] != math.MaxInt32 {
					f[t][j] = min(f[t][j], f[t-cost][i]+passingFees[j])
				}
			}
		}
	}

	ans := math.MaxInt32
	for t := 1; t <= maxTime; t++ {
		ans = min(ans, f[t][n-1])
	}
	if ans == math.MaxInt32 {
		return -1
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var maxTime int
	var edges [][]int
	var passingFees []int

	if err := json.Unmarshal([]byte(inputValues[0]), &maxTime); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &passingFees); err != nil {
		log.Fatal(err)
	}

	return minCost(maxTime, edges, passingFees)
}
