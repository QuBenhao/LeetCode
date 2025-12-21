package problem3783

import (
	"encoding/json"
	"log"
	"strings"
)

func mirrorDistance(n int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return mirrorDistance(n)
}
