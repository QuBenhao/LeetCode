package problemLCR_065

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func minimumLengthEncoding(words []string) (ans int) {
	reverseStrings := make([]string, len(words))
	for i, word := range words {
		bytes := []byte(word)
		reverseBytes := make([]byte, len(bytes))
		for j := 0; j < len(bytes); j++ {
			reverseBytes[j] = bytes[len(bytes)-1-j]
		}
		reverseStrings[i] = string(reverseBytes)
	}
	sort.Strings(reverseStrings)
	for i := 0; i < len(reverseStrings)-1; i++ {
		if !strings.HasPrefix(reverseStrings[i+1], reverseStrings[i]) {
			ans += len(reverseStrings[i]) + 1
		}
	}
	ans += len(reverseStrings[len(reverseStrings)-1]) + 1
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return minimumLengthEncoding(words)
}
