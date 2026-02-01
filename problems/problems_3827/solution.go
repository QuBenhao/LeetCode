package problem3827

import (
	"encoding/json"
	"log"
	"strings"
)

func countMonobit(n int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return countMonobit(n)
}
