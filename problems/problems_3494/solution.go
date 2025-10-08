package problem3494

import (
	"encoding/json"
	"log"
	"strings"
)

func minTime(skill []int, mana []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var skill []int
	var mana []int

	if err := json.Unmarshal([]byte(inputValues[0]), &skill); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &mana); err != nil {
		log.Fatal(err)
	}

	return minTime(skill, mana)
}
