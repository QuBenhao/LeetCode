package problemLCR_005

import (
	"encoding/json"
	"log"
	"strings"
)

func maxProduct(words []string) (ans int) {
	wordDict := make(map[int]int, len(words))
	for _, word := range words {
		mask := 0
		for _, c := range word {
			mask |= 1 << (c - 'a')
		}
		wordDict[mask] = max(wordDict[mask], len(word))
	}
	for k1, v1 := range wordDict {
		for k2, v2 := range wordDict {
			if k1&k2 == 0 {
				ans = max(ans, v1*v2)
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return maxProduct(words)
}
