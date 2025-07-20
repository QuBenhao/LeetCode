package problem3625

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func countTrapezoids(points [][]int) (ans int) {
	cnt := make(map[float64]map[float64]int)
	cnt2 := make(map[int]map[float64]int)
	n := len(points)
	for i := range n - 1 {
		x, y := points[i][0], points[i][1]
		for j := i + 1; j < n; j++ {
			x2, y2 := points[j][0], points[j][1]
			var k, b float64
			if x == x2 {
				k = math.MaxFloat64
				b = float64(x)
			} else {
				k = float64(y2-y) / float64(x2-x)
				b = float64(y*(x2-x)-x*(y2-y)) / float64(x2-x)
			}
			if _, ok := cnt[k]; !ok {
				cnt[k] = make(map[float64]int)
			}
			cnt[k][b]++
			mask := (x+x2+2000)<<16 | (y + y2 + 2000)
			if _, ok := cnt2[mask]; !ok {
				cnt2[mask] = make(map[float64]int)
			}
			cnt2[mask][k]++
		}
	}
	for _, m := range cnt {
		s := 0
		for _, v := range m {
			ans += s * v
			s += v
		}
	}
	for _, m := range cnt2 {
		s := 0
		for _, v := range m {
			ans -= s * v
			s += v
		}
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
