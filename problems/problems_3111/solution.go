package problem3111

import (
	"encoding/json"
	"log"
	"strings"
)

func minRectanglesToCoverPoints(points [][]int, w int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var points [][]int
	var w int

	if err := json.Unmarshal([]byte(inputValues[0]), &points); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &w); err != nil {
		log.Fatal(err)
	}

	return minRectanglesToCoverPoints(points, w)
}
