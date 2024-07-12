package problem74

import (
	"encoding/json"
	"log"
	"strings"
)

func searchMatrix(matrix [][]int, target int) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var matrix [][]int
	var target int

	if err := json.Unmarshal([]byte(inputValues[0]), &matrix); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return searchMatrix(matrix, target)
}
