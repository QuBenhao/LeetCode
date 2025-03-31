package problem2140

import (
	"encoding/json"
	"log"
	"strings"
)

func mostPoints(questions [][]int) int64 {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var questions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &questions); err != nil {
		log.Fatal(err)
	}

	return mostPoints(questions)
}
