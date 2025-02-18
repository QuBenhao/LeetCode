package problem624

import (
	"encoding/json"
	"log"
	"strings"
)

func maxDistance(arrays [][]int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arrays [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &arrays); err != nil {
		log.Fatal(err)
	}

	return maxDistance(arrays)
}
