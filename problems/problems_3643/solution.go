package problem3643

import (
	"encoding/json"
	"log"
	"strings"
)

func reverseSubmatrix(grid [][]int, x int, y int, k int) [][]int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var grid [][]int
	var x int
	var y int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &grid); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &x); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &y); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &k); err != nil {
		log.Fatal(err)
	}

	return reverseSubmatrix(grid, x, y, k)
}
