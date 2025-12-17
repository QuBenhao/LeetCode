package problemInterview_16__01

import (
	"encoding/json"
	"log"
	"strings"
)

func swapNumbers(numbers []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var numbers []int

	if err := json.Unmarshal([]byte(inputValues[0]), &numbers); err != nil {
		log.Fatal(err)
	}

	return swapNumbers(numbers)
}
