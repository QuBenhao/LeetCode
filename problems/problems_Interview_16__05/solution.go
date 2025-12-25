package problemInterview_16__05

import (
	"encoding/json"
	"log"
	"strings"
)

func trailingZeroes(n int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return trailingZeroes(n)
}
