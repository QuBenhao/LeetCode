package problem1340

import (
	"encoding/json"
	"log"
	"strings"
)

func maxJumps(arr []int, d int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int
	var d int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &d); err != nil {
		log.Fatal(err)
	}

	return maxJumps(arr, d)
}
