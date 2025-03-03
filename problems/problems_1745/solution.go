package problem1745

import (
	"encoding/json"
	"log"
	"strings"
)

func checkPartitioning(s string) bool {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return checkPartitioning(s)
}
