package problem2938

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumSteps(s string) (ans int64) {
	for i, b := 0, int64(0); i < len(s); i++ {
		if s[i] == '0' {
			ans += b
		} else {
			b++
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return minimumSteps(s)
}
