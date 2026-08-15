package problem2029

import (
	"encoding/json"
	"log"
	"strings"
)

func stoneGameIX(stones []int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var stones []int

	if err := json.Unmarshal([]byte(inputValues[0]), &stones); err != nil {
		log.Fatal(err)
	}

	return stoneGameIX(stones)
}
