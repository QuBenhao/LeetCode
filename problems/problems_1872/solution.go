package problem1872

import (
	"encoding/json"
	"log"
	"strings"
)

func stoneGameVIII(stones []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var stones []int

	if err := json.Unmarshal([]byte(inputValues[0]), &stones); err != nil {
		log.Fatal(err)
	}

	return stoneGameVIII(stones)
}
