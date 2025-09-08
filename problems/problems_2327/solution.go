package problem2327

import (
	"encoding/json"
	"log"
	"strings"
)

func peopleAwareOfSecret(n int, delay int, forget int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var delay int
	var forget int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &delay); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &forget); err != nil {
		log.Fatal(err)
	}

	return peopleAwareOfSecret(n, delay, forget)
}
