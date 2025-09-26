package problem812

import (
	"encoding/json"
	"log"
	"strings"
)

func largestTriangleArea(points [][]int) float64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var points [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &points); err != nil {
		log.Fatal(err)
	}

	return largestTriangleArea(points)
}
