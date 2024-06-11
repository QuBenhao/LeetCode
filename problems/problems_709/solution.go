package problem709

import (
	"encoding/json"
	"log"
	"strings"
)

func toLowerCase(s string) string {
	return strings.ToLower(s)
}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return toLowerCase(s)
}
