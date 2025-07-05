package problem1784

import (
	"encoding/json"
	"log"
	"strings"
)

func checkOnesSegment(s string) bool {
	count := 0
	appear := false
	for _, r := range s {
		if r == '1' {
			appear = true
		} else {
			if appear {
				count++
				if count > 1 {
					return false
				}
				appear = false
			}
		}
	}
	return count == 0 || !appear
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return checkOnesSegment(s)
}
