package problem1689

import (
	"encoding/json"
	"log"
	"strings"
)

func minPartitions(n string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n string

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return minPartitions(n)
}
