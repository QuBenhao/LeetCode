package problem58

import (
	"encoding/json"
	"log"
	"strings"
)

func lengthOfLastWord(s string) int {
	idx := len(s) - 1
	for ; idx >= 0 && s[idx] == ' '; idx-- {
	}
	i := idx - 1
	for ; i >= 0 && s[i] != ' '; i-- {
	}
	return idx - i
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return lengthOfLastWord(s)
}
