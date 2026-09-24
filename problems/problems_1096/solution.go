package problem1096

import (
	"encoding/json"
	"log"
	"strings"
)

func braceExpansionII(expression string) []string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var expression string

	if err := json.Unmarshal([]byte(inputValues[0]), &expression); err != nil {
		log.Fatal(err)
	}

	return braceExpansionII(expression)
}
