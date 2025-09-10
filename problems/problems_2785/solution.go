package problem2785

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

const VOWELS = "AEIOUaeiou"

func sortVowels(s string) string {
	var vowels []byte
	for _, ch := range s {
		if strings.IndexRune(VOWELS, ch) >= 0 {
			vowels = append(vowels, byte(ch))
		}
	}

	slices.Sort(vowels)

	ans := []byte(s)
	j := 0
	for i, ch := range ans {
		if strings.IndexRune(VOWELS, rune(ch)) >= 0 {
			ans[i] = vowels[j]
			j++
		}
	}
	return string(ans)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return sortVowels(s)
}
