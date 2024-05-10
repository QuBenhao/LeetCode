package problem2391

import (
	"encoding/json"
	"log"
	"strings"
)

func Solve(input string) int {
	values := strings.Split(input, "\n")
	var garbage []string
	var travel []int

	if err := json.Unmarshal([]byte(values[0]), &garbage); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &travel); err != nil {
		log.Fatal(err)
	}

	return garbageCollection(garbage, travel)
}

func garbageCollection(garbage []string, travel []int) int {

}