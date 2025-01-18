package problem2266

import (
	"encoding/json"
	"log"
	"strings"
)

func countTexts(pressedKeys string) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var pressedKeys string

	if err := json.Unmarshal([]byte(inputValues[0]), &pressedKeys); err != nil {
		log.Fatal(err)
	}

	return countTexts(pressedKeys)
}
