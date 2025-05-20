package problem28

import (
	"encoding/json"
	"log"
	"strings"
)

func strStr(haystack string, needle string) int {
	return strings.Index(haystack, needle)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var haystack string
	var needle string

	if err := json.Unmarshal([]byte(values[0]), &haystack); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &needle); err != nil {
		log.Fatal(err)
	}

	return strStr(haystack, needle)
}
