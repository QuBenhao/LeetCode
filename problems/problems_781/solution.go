package problem781

import (
	"encoding/json"
	"log"
	"strings"
)

func numRabbits(answers []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var answers []int

	if err := json.Unmarshal([]byte(inputValues[0]), &answers); err != nil {
		log.Fatal(err)
	}

	return numRabbits(answers)
}
