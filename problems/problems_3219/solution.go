package problem3219

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumCost(m int, n int, horizontalCut []int, verticalCut []int) int64 {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var m int
	var n int
	var horizontalCut []int
	var verticalCut []int

	if err := json.Unmarshal([]byte(inputValues[0]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &horizontalCut); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &verticalCut); err != nil {
		log.Fatal(err)
	}

	return minimumCost(m, n, horizontalCut, verticalCut)
}
