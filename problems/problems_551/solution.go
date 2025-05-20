package problem551

import (
	"encoding/json"
	"log"
	"strings"
)

func checkRecord(s string) bool {
	return !strings.Contains(s, "LLL") && strings.Count(s, "A") < 2
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return checkRecord(s)
}
