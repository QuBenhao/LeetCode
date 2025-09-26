package problem812

import (
	"encoding/json"
	"log"
	"strings"
)

func largestTriangleArea(points [][]int) (ans float64) {
	for i, n := 0, len(points); i < n-2; i++ {
		for j := i + 1; j < n-1; j++ {
			for k := j + 1; k < n; k++ {
				x1, y1 := points[i][0], points[i][1]
				x2, y2 := points[j][0], points[j][1]
				x3, y3 := points[k][0], points[k][1]
				d := x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2
				if d < 0 {
					d *= -1
				}
				if cur := float64(d) / 2.0; cur > ans {
					ans = cur
				}
			}
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

	return largestTriangleArea(points)
}
