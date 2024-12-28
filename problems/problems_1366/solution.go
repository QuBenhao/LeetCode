package problem1366

import (
	"encoding/json"
	"log"
	"strings"
)

func rankTeams(votes []string) string {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var votes []string

	if err := json.Unmarshal([]byte(inputValues[0]), &votes); err != nil {
		log.Fatal(err)
	}

	return rankTeams(votes)
}
