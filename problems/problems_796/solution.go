package problem796

import (
	"encoding/json"
	"log"
	"strings"
)

func rotateString(s string, goal string) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var goal string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &goal); err != nil {
		log.Fatal(err)
	}

	return rotateString(s, goal)
}
