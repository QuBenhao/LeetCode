package problem3541

import (
	"encoding/json"
	"log"
	"strings"
)

const VOWELS = "aeiou"

func maxFreqSum(s string) int {
	vowelsCount := make([]int, 5)
	nonVowelsCount := make([]int, 26)
	for _, r := range s {
		if idx := strings.IndexRune(VOWELS, r); idx >= 0 {
			vowelsCount[idx]++
		} else {
			nonVowelsCount[r-'a']++
		}
	}
	return maxElement(vowelsCount) + maxElement(nonVowelsCount)
}

func maxElement(arr []int) (ans int) {
	for _, v := range arr {
		ans = max(ans, v)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return maxFreqSum(s)
}
