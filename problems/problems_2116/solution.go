package problem2116

import (
	"encoding/json"
	"log"
	"strings"
)

func canBeValid(s string, locked string) bool {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var locked string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &locked); err != nil {
		log.Fatal(err)
	}

	return canBeValid(s, locked)
}
