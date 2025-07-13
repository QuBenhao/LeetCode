package problem3612

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func processStr(s string) string {
	var ans []byte
	for _, c := range s {
		if c == '#' {
			ans = append(ans, ans...)
		} else if c == '%' {
			slices.Reverse(ans)
		} else if c == '*' {
			if len(ans) > 0 {
				ans = ans[:len(ans)-1]
			}
		} else {
			ans = append(ans, byte(c))
		}
	}
	return string(ans)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return processStr(s)
}
