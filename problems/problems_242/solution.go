package problem242

import (
	"encoding/json"
	"log"
	"strings"
)

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	counter := map[byte]int{}
	for i := 0; i < len(s); i++ {
		counter[s[i]]++
		counter[t[i]]--
	}
	for _, v := range counter {
		if v != 0 {
			return false
		}
	}
	return true
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var s string
	var t string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &t); err != nil {
		log.Fatal(err)
	}

	return isAnagram(s, t)
}
