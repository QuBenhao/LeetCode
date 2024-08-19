package problem76

import (
	"encoding/json"
	"log"
	"strings"
)

func minWindow(s string, t string) string {
	var cntS, cntT [60]int
	getIdx := func(c byte) int {
		if c >= 'A' && c <= 'Z' {
			return int(c - 'A')
		}
		return int(c - 'a' + 26)
	}
	diff := 0
	for i := 0; i < len(t); i++ {
		idx := getIdx(t[i])
		if cntT[idx] == 0 {
			diff++
		}
		cntT[idx]++
	}
	ans := ""
	for l, r := 0, 0; r < len(s); r++ {
		idx := getIdx(s[r])
		cntS[idx]++
		if cntS[idx] == cntT[idx] {
			diff--
		}
		for l < r {
			i := getIdx(s[l])
			if cntS[i] > cntT[i] {
				cntS[i]--
				l++
			} else {
				break
			}
		}
		if diff == 0 && (ans == "" || len(ans) > r-l+1) {
			ans = s[l : r+1]
		}
	}
	return ans
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
