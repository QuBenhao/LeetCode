package problem1103

import (
	"encoding/json"
	"log"
	"strings"
)

func distributeCandies(candies int, num_people int) []int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var candies int
	var num_people int

	if err := json.Unmarshal([]byte(values[0]), &candies); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &num_people); err != nil {
		log.Fatal(err)
	}

	return distributeCandies(candies, num_people)
}
