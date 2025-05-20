package problem2716

import (
	"encoding/json"
	"log"
	"strings"
)

func minimizedStringLength(s string) (ans int) {
	explored := map[rune]bool{}
	for _, c := range s {
		if _, val := explored[c]; val {
			continue
		}
		explored[c] = true
		ans++
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minimizedStringLength(s)
}
