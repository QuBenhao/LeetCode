package problem3461

import (
	"encoding/json"
	"log"
	"strings"
)

func hasSameDigits(s string) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return hasSameDigits(s)
}
