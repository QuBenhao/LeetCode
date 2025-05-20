package problemLCR_015

import (
	"encoding/json"
	"log"
	"strings"
)

func findAnagrams(s string, p string) (ans []int) {
	var cnt [26]int
	for _, ch := range p {
		cnt[ch-'a']++
	}
	diff := 0
	for _, c := range cnt {
		if c != 0 {
			diff++
		}
	}
	for i, ch := range s {
		cnt[ch-'a']--
		if cnt[ch-'a'] == 0 {
			diff--
		} else if cnt[ch-'a'] == -1 {
			diff++
		}
		if i >= len(p)-1 {
			if diff == 0 {
				ans = append(ans, i-len(p)+1)
			}
			cnt[s[i-len(p)+1]-'a']++
			if cnt[s[i-len(p)+1]-'a'] == 0 {
				diff--
			} else if cnt[s[i-len(p)+1]-'a'] == 1 {
				diff++
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var p string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &p); err != nil {
		log.Fatal(err)
	}

	return findAnagrams(s, p)
}
