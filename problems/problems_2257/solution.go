package problem2257

import (
	"encoding/json"
	"log"
	"strings"
)

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var m int
	var n int
	var guards [][]int
	var walls [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &guards); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &walls); err != nil {
		log.Fatal(err)
	}

	return countUnguarded(m, n, guards, walls)
}
