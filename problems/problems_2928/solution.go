package problem2928

import (
	"encoding/json"
	"log"
	"strings"
)

func distributeCandies(n int, limit int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var n int
	var limit int

	if err := json.Unmarshal([]byte(values[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &limit); err != nil {
		log.Fatal(err)
	}

	return distributeCandies(n, limit)
}
