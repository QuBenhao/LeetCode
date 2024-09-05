package problem3174

import (
	"encoding/json"
	"log"
	"strings"
)

func clearDigits(s string) string {
	var st []rune
	for _, r := range s {
		if r >= '0' && r <= '9' {
			if len(st) > 0 {
				st = st[:len(st)-1]
			}
		} else {
			st = append(st, r)
		}
	}
	return string(st)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return clearDigits(s)
}
