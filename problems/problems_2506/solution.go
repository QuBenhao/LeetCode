package problem2506

import (
	"encoding/json"
	"log"
	"strings"
)

func similarPairs(words []string) (ans int) {
	counter := map[int]int{}
	for _, word := range words {
		cur := 0
		for _, r := range word {
			cur |= 1 << (r - 'a')
		}
		ans += counter[cur]
		counter[cur]++
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return similarPairs(words)
}
