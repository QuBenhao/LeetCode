package problemLCR_016

import (
	"encoding/json"
	"log"
	"strings"
)

func lengthOfLongestSubstring(s string) (ans int) {
	var window []byte
	var explored = make(map[byte]bool)
	for i := 0; i < len(s); i++ {
		if explored[s[i]] {
			for j := 0; j < len(window); j++ {
				if window[j] == s[i] {
					window = window[j+1:]
					break
				}
				delete(explored, window[j])
			}
		}
		window = append(window, s[i])
		explored[s[i]] = true
		if len(window) > ans {
			ans = len(window)
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return lengthOfLongestSubstring(s)
}
