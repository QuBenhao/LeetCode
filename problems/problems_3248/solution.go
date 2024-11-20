package problem3248

import (
	"encoding/json"
	"log"
	"strings"
)

func finalPositionOfSnake(n int, commands []string) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var commands []string

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &commands); err != nil {
		log.Fatal(err)
	}

	return finalPositionOfSnake(n, commands)
}
