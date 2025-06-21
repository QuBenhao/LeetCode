package problem2138

import (
	"encoding/json"
	"log"
	"strings"
)

func divideString(s string, k int, fill byte) []string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int
	var fill byte

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	var fillStr string
	if err := json.Unmarshal([]byte(inputValues[2]), &fillStr); err != nil {
		log.Fatal(err)
	}
	if len(fillStr) > 1 {
		fill = fillStr[1]
	} else {
		fill = fillStr[0]
	}

	return divideString(s, k, fill)
}
