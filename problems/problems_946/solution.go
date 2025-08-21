package problem946

import (
	"encoding/json"
	"log"
	"strings"
)

func validateStackSequences(pushed []int, popped []int) bool {
	n, j := len(popped), 0
	var st []int
	for _, x := range pushed {
		st = append(st, x)
		for len(st) > 0 && j < n && st[len(st)-1] == popped[j] {
			st = st[:len(st)-1]
			j++
		}
	}
	return len(st) == 0
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var pushed []int
	var popped []int

	if err := json.Unmarshal([]byte(inputValues[0]), &pushed); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &popped); err != nil {
		log.Fatal(err)
	}

	return validateStackSequences(pushed, popped)
}
