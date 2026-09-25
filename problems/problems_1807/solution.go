package problem1807

import (
	"encoding/json"
	"log"
	"strings"
)

func evaluate(s string, knowledge [][]string) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var knowledge [][]string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &knowledge); err != nil {
		log.Fatal(err)
	}

	return evaluate(s, knowledge)
}
