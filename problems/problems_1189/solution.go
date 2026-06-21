package problem1189

import (
	"encoding/json"
	"log"
	"strings"
)

func maxNumberOfBalloons(text string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var text string

	if err := json.Unmarshal([]byte(inputValues[0]), &text); err != nil {
		log.Fatal(err)
	}

	return maxNumberOfBalloons(text)
}
