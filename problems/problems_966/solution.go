package problem966

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func spellchecker(wordlist, queries []string) []string {
	n := len(wordlist)
	origin := make(map[string]bool, n) // Preallocate space
	lowerToOrigin := make(map[string]string, n)
	vowelToOrigin := make(map[string]string, n)
	// Replace all vowels with '?'
	vowelReplacer := strings.NewReplacer("a", "?", "e", "?", "i", "?", "o", "?", "u", "?")

	for _, s := range slices.Backward(wordlist) {
		origin[s] = true
		lower := strings.ToLower(s)
		lowerToOrigin[lower] = s                        // For example, kite -> KiTe
		vowelToOrigin[vowelReplacer.Replace(lower)] = s // For example, k?t? -> KiTe
	}

	for i, q := range queries {
		if origin[q] { // Exact match
			continue
		}
		lower := strings.ToLower(q)
		if s, ok := lowerToOrigin[lower]; ok { // Case-insensitive match
			queries[i] = s
		} else { // Case-insensitive match allowing vowel substitutions
			queries[i] = vowelToOrigin[vowelReplacer.Replace(lower)]
		}
	}

	return queries
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var wordlist []string
	var queries []string

	if err := json.Unmarshal([]byte(inputValues[0]), &wordlist); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return spellchecker(wordlist, queries)
}
