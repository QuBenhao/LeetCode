package problem1957

import (
	"encoding/json"
	"log"
	"strings"
)

func makeFancyString(s string) string {
	var ans strings.Builder
	for i := 0; i < len(s); i++ {
		if i > 1 && s[i] == s[i-1] && s[i] == s[i-2] {
			continue
		}
		ans.WriteByte(s[i])
	}
	return ans.String()
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return makeFancyString(s)
}
