package problemLCR_014

import (
	"encoding/json"
	"log"
	"strings"
)

func checkInclusion(s1 string, s2 string) bool {
	m, n := len(s1), len(s2)
	cnt1, cnt2 := [26]int{}, [26]int{}
	for _, ch := range s1 {
		cnt1[ch-'a']++
	}
	for i := 0; i < n; i++ {
		cnt2[s2[i]-'a']++
		if i >= m-1 {
			if cnt1 == cnt2 {
				return true
			}
			cnt2[s2[i-m+1]-'a']--
		}
	}
	return false
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s1 string
	var s2 string

	if err := json.Unmarshal([]byte(inputValues[0]), &s1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s2); err != nil {
		log.Fatal(err)
	}

	return checkInclusion(s1, s2)
}
