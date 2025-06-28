package problem2030

import (
	"encoding/json"
	"log"
	"strings"
)

func smallestSubsequence(s string, k int, letter byte, repetition int) string {
	ans := make([]rune, k)
	letterLeft := strings.Count(s, string(letter))
	runeLetter := rune(letter)
	letterCount := 0
	idx := 0
	n := len(s)
	for i, c := range s {
		for idx > 0 && ans[idx-1] > c && n-i+idx-1 >= k &&
			(c == runeLetter || letterCount+letterLeft-btoi(ans[idx-1] == runeLetter) >= repetition) {
			if ans[idx-1] == runeLetter {
				letterCount--
			}
			idx--
		}
		if idx < k {
			if c == runeLetter {
				letterCount++
				ans[idx] = c
				idx++
			} else if k-idx > repetition-letterCount {
				ans[idx] = c
				idx++
			}
		}
		if c == runeLetter {
			letterLeft--
		}
	}
	return string(ans)
}

func btoi(b bool) int {
	if b {
		return 1
	}
	return 0
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int
	var letter byte
	var repetition int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	var letterStr string
	if err := json.Unmarshal([]byte(inputValues[2]), &letterStr); err != nil {
		log.Fatal(err)
	}
	if len(letterStr) > 1 {
		letter = letterStr[1]
	} else {
		letter = letterStr[0]
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &repetition); err != nil {
		log.Fatal(err)
	}

	return smallestSubsequence(s, k, letter, repetition)
}
