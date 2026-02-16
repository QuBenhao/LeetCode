package problem401

import (
	"encoding/json"
	"log"
	"strings"
)

func readBinaryWatch(turnedOn int) []string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var turnedOn int

	if err := json.Unmarshal([]byte(inputValues[0]), &turnedOn); err != nil {
		log.Fatal(err)
	}

	return readBinaryWatch(turnedOn)
}
