package problem3754

import (
	"encoding/json"
	"log"
	"strings"
)

func sumAndMultiply(n int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return sumAndMultiply(n)
}
