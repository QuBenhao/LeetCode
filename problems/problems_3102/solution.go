package problem3102

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumDistance(points [][]int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var points [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &points); err != nil {
		log.Fatal(err)
	}

	return minimumDistance(points)
}
