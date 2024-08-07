package problem950

import (
	"encoding/json"
	"log"
	"strings"
)

func deckRevealedIncreasing(deck []int) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var deck []int

	if err := json.Unmarshal([]byte(inputValues[0]), &deck); err != nil {
		log.Fatal(err)
	}

	return deckRevealedIncreasing(deck)
}
