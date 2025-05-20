package problem1870

import (
	"encoding/json"
	"log"
	"strings"
)

func minSpeedOnTime(dist []int, hour float64) int {
	n := len(dist)
	if float64(n-1) >= hour {
		return -1
	}
	l, r := 1, 1_000_000_000
	for l < r {
		mid := l + (r-l)/2
		sum := 0
		for i := 0; i < n-1; i++ {
			sum += (dist[i] + mid - 1) / mid
		}
		if float64(sum)+float64(dist[n-1])/float64(mid) <= hour {
			r = mid
		} else {
			l = mid + 1
		}
	}
	return l
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var dist []int
	var hour float64

	if err := json.Unmarshal([]byte(inputValues[0]), &dist); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &hour); err != nil {
		log.Fatal(err)
	}

	return minSpeedOnTime(dist, hour)
}
