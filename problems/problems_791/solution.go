package problem791

import (
	"encoding/json"
	"log"
	"strings"
)

func customSortString(order string, s string) string {
	counter := make([]int, 26)
	for _, char := range s {
		counter[char-'a']++
	}
	result := strings.Builder{}
	for _, char := range order {
		if count := counter[char-'a']; count > 0 {
			result.WriteString(strings.Repeat(string(char), count))
			counter[char-'a'] = 0 // Reset to avoid double counting
		}
	}
	for i, count := range counter {
		if count > 0 {
			result.WriteString(strings.Repeat(string('a'+i), count))
		}
	}
	return result.String()
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var order string
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &order); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s); err != nil {
		log.Fatal(err)
	}

	return customSortString(order, s)
}
