package problem3128

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfRightTriangles(grid [][]int) int64 {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}

	return numberOfRightTriangles(grid)
}
