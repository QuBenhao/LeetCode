package problem1542

import (
	"encoding/json"
	"log"
	"strings"
)

func longestAwesome(s string) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var s string

	if err := json.Unmarshal([]byte(values[0]), &s); err != nil {
		log.Fatal(err)
	}

	return longestAwesome(s)
}
