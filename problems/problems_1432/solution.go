package problem1432

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func maxDiff(num int) int {
	s := strconv.Itoa(num)
	n := len(s)
	idx := 0
	for idx < n && s[idx] == '9' {
		idx++
	}
	var mx, mn int
	if idx == n {
		mx = num
	} else {
		mx, _ = strconv.Atoi(strings.ReplaceAll(s, string(s[idx]), "9"))
	}
	if s[0] == '1' {
		idx = 1
		for idx < n && (s[idx] == '0' || s[idx] == s[0]) {
			idx++
		}
		if idx == n {
			mn = num
		} else {
			mn, _ = strconv.Atoi(strings.ReplaceAll(s, string(s[idx]), "0"))
		}
	} else {
		mn, _ = strconv.Atoi(strings.ReplaceAll(s, string(s[0]), "1"))
	}
	return mx - mn
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return maxDiff(num)
}
