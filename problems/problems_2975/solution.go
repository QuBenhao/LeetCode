package problem2975

import (
	"encoding/json"
	"log"
	"strings"
)

func maximizeSquareArea(m int, n int, hFences []int, vFences []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var m int
	var n int
	var hFences []int
	var vFences []int

	if err := json.Unmarshal([]byte(inputValues[0]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &hFences); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &vFences); err != nil {
		log.Fatal(err)
	}

	return maximizeSquareArea(m, n, hFences, vFences)
}
