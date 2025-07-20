package problem3623

import (
	"encoding/json"
	"log"
	"strings"
)

const mod = 1_000_000_007

func countTrapezoids(points [][]int) (ans int) {
	counts := make(map[int]int)
	for _, point := range points {
		counts[point[1]]++
	}
	s := 0
	for _, v := range counts {
		k := int64(1) * int64(v) * int64(v-1) / 2 % mod
		ans = (int(k*int64(s)%mod) + ans) % mod
		s = (int(k%mod) + s) % mod
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var points [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &points); err != nil {
		log.Fatal(err)
	}

	return countTrapezoids(points)
}
