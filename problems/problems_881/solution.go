package problem881

import (
	"encoding/json"
	"log"
	"strings"
)

func numRescueBoats(people []int, limit int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var people []int
	var limit int

	if err := json.Unmarshal([]byte(values[0]), &people); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &limit); err != nil {
		log.Fatal(err)
	}

	return numRescueBoats(people, limit)
}
