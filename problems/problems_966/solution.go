package problem966

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func spellchecker(wordlist, queries []string) []string {
	n := len(wordlist)
	origin := make(map[string]bool, n) // 预分配空间
	lowerToOrigin := make(map[string]string, n)
	vowelToOrigin := make(map[string]string, n)
	// 把元音都替换成 '?'
	vowelReplacer := strings.NewReplacer("a", "?", "e", "?", "i", "?", "o", "?", "u", "?")

	for _, s := range slices.Backward(wordlist) {
		origin[s] = true
		lower := strings.ToLower(s)
		lowerToOrigin[lower] = s                        // 例如 kite -> KiTe
		vowelToOrigin[vowelReplacer.Replace(lower)] = s // 例如 k?t? -> KiTe
	}

	for i, q := range queries {
		if origin[q] { // 完全匹配
			continue
		}
		lower := strings.ToLower(q)
		if s, ok := lowerToOrigin[lower]; ok { // 不区分大小写的匹配
			queries[i] = s
		} else { // 不区分大小写+元音模糊匹配
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
