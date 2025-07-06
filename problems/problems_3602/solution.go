package problem3602

import (
	"encoding/json"
	"log"
	"strings"
)

func concatHex36(n int) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return concatHex36(n)
}
