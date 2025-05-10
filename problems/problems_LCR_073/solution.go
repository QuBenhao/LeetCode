package problemLCR_073

import (
	"encoding/json"
	"log"
	"strings"
)

func minEatingSpeed(piles []int, h int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var piles []int
	var h int

	if err := json.Unmarshal([]byte(inputValues[0]), &piles); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &h); err != nil {
		log.Fatal(err)
	}

	return minEatingSpeed(piles, h)
}
