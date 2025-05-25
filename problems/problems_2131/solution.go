package problem2131

import (
	"encoding/json"
	"log"
	"strings"
)

func longestPalindrome(words []string) (ans int) {
	counter := map[string]int{}
	for _, word := range words {
		counter[word]++
	}
	hasExtra := false
	for word, c := range counter {
		if word[0] == word[1] {
			ans += c / 2 * 4
			hasExtra = hasExtra || c%2 == 1
		} else if word[0] < word[1] {
			rev := string([]byte{word[1], word[0]})
			ans += min(c, counter[rev]) * 4
		}
	}
	if hasExtra {
		ans += 2
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return longestPalindrome(words)
}
