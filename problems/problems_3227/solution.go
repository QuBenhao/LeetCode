package problem3227

import (
	"encoding/json"
	"log"
	"strings"
)

func doesAliceWin(s string) bool {
	return strings.ContainsAny(s, "aeiou")
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return doesAliceWin(s)
}
