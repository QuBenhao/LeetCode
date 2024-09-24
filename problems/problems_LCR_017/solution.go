package problemLCR_017

import (
	"encoding/json"
	"log"
	"strings"
)

func minWindow(s string, t string) string {
	ansL, ansR := -1, -1
	left, right := 0, 0
	counter := make(map[byte]int)
	diff := 0
	for i := 0; i < len(t); i++ {
		counter[t[i]]++
		if counter[t[i]] == 1 {
			diff++
		}
	}
	for n := len(s); right < n; right++ {
		counter[s[right]]--
		if counter[s[right]] == 0 {
			diff--
		}
		for diff == 0 {
			if ansL == -1 || right-left < ansR-ansL {
				ansL, ansR = left, right
			}
			counter[s[left]]++
			if counter[s[left]] == 1 {
				diff++
			}
			left++
		}
	}
	if ansL == -1 {
		return ""
	}
	return s[ansL : ansR+1]
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var t string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &t); err != nil {
		log.Fatal(err)
	}

	return minWindow(s, t)
}
