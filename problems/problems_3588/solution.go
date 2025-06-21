package problem3588

import (
	"encoding/json"
	"log"
	"strings"
)

func maxArea(coords [][]int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var coords [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &coords); err != nil {
		log.Fatal(err)
	}

	return maxArea(coords)
}
