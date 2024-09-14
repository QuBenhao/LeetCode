package problem2390

import (
	"encoding/json"
	"log"
	"strings"
)

func removeStars(s string) string {
	var ans []rune
	for _, c := range s {
		if c != '*' {
			ans = append(ans, c)
		} else {
			if len(ans) > 0 {
				ans = ans[:len(ans)-1]
			}
		}
	}
	return string(ans)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return removeStars(s)
}
