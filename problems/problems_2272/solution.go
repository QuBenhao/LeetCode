package problem2272

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func largestVariance(s string) (ans int) {
	var f0, f1 [26][26]int
	for i := range f1 {
		for j := range f1[i] {
			f1[i][j] = math.MinInt
		}
	}

	for _, ch := range s {
		ch -= 'a'
		// At ch, only compute states with a=ch or b=ch; other states are unrelated to ch and their f values stay unchanged
		for i := range 26 {
			if i == int(ch) {
				continue
			}
			// Assume the most frequent letter is a=ch; update all states with b=i
			f0[ch][i] = max(f0[ch][i], 0) + 1
			f1[ch][i]++
			// Assume the least frequent letter is b=ch; update all states with a=i
			f0[i][ch] = max(f0[i][ch], 0) - 1
			f1[i][ch] = f0[i][ch]
			ans = max(ans, f1[ch][i], f1[i][ch])
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

	return largestVariance(s)
}
