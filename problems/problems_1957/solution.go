package problem1957

import (
	"encoding/json"
	"log"
	"strings"
)

func makeFancyString(s string) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return makeFancyString(s)
}
