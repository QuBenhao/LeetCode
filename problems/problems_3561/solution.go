package problem3561

import (
	"encoding/json"
	"log"
	"strings"
)

func resultingString(s string) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return resultingString(s)
}
