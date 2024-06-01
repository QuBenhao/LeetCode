package problem575

import (
	"encoding/json"
	"log"
	"strings"
)

func distributeCandies(candyType []int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var candyType []int

	if err := json.Unmarshal([]byte(values[0]), &candyType); err != nil {
		log.Fatal(err)
	}

	return distributeCandies(candyType)
}
