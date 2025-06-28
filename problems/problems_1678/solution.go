package problem1678

import (
	"encoding/json"
	"log"
	"strings"
)

func interpret(command string) string {
	var ans strings.Builder
	for i, n := 0, len(command); i < n; i++ {
		if command[i] == 'G' {
			ans.WriteByte('G')
		} else if command[i] == '(' {
			if i+1 < n && command[i+1] == ')' {
				ans.WriteByte('o')
				i++ // Skip the next character ')'
			} else if i+1 < n && command[i+1] == 'a' {
				ans.WriteString("al")
				i += 3 // Skip "al)"
			}
		}
	}
	return ans.String()
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var command string

	if err := json.Unmarshal([]byte(inputValues[0]), &command); err != nil {
		log.Fatal(err)
	}

	return interpret(command)
}
