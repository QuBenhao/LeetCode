package problem2712

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumCost(s string) int64 {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minimumCost(s)
}
