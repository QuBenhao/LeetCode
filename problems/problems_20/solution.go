package problem20

import (
	"encoding/json"
	"log"
	"strings"
)

func isValid(s string) bool {
	var stack []byte
	left, right := "([{", ")]}"
	for i := 0; i < len(s); i++ {
		if strings.Contains(left, string(s[i])) {
			stack = append(stack, s[i])
		} else if len(stack) == 0 || left[strings.Index(right, string(s[i]))] != stack[len(stack)-1] {
			return false
		} else {
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return isValid(s)
}
