package problem3335

import (
	"encoding/json"
	"log"
	"strings"
)

const MOD = 1000000007

func lengthAfterTransformations(s string, t int) (ans int) {
	count := make([]int, 26)
	for _, r := range s {
		count[r-'a']++
	}
	remain := t % 26
	for range remain {
		extra := count[25]
		for i := 25; i > 0; i-- {
			count[i] = count[i-1]
		}
		count[0] = extra
		count[1] = (count[1] + extra) % MOD
	}
	for range (t - remain) / 26 {
		extra := count[25]
		for i := 25; i > 0; i-- {
			count[i] = (count[i] + count[i-1]) % MOD
		}
		count[0] = (count[0] + extra) % MOD
		count[1] = (count[1] + extra) % MOD
	}
	for _, c := range count {
		ans = (ans + c) % MOD
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var t int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &t); err != nil {
		log.Fatal(err)
	}

	return lengthAfterTransformations(s, t)
}
