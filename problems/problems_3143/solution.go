package problem3143

import (
	"encoding/json"
	"log"
	"strings"
)

func maxPointsInsideSquare(points [][]int, s string) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var points [][]int
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &points); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s); err != nil {
		log.Fatal(err)
	}

	return maxPointsInsideSquare(points, s)
}
