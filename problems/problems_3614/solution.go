package problem3614

import (
	"encoding/json"
	"log"
	"strings"
)

func processStr(s string, k int64) byte {
	var length int64
	n := len(s)
	invalids := make(map[int]bool)
	for i, c := range s {
		if c == '#' {
			length *= 2
		} else if c == '*' {
			if length > 0 {
				length--
			} else {
				invalids[i] = true
			}
		} else if c != '%' {
			length++
		}
	}
	if k >= length {
		return '.'
	}
	for i := n - 1; i >= 0; i-- {
		if invalids[i] {
			continue
		}
		switch s[i] {
		case '#':
			length /= 2
			k %= length
		case '*':
			length++
		case '%':
			k = length - 1 - k
		default:
			if k == length-1 {
				return s[i]
			}
			length--
		}
	}
	return s[k]
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var k int64

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return processStr(s, k)
}
