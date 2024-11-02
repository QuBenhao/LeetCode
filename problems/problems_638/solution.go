package problem638

import (
	"encoding/json"
	"log"
	"strings"
)

func shoppingOffers(price []int, special [][]int, needs []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var price []int
	var special [][]int
	var needs []int

	if err := json.Unmarshal([]byte(inputValues[0]), &price); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &special); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &needs); err != nil {
		log.Fatal(err)
	}

	return shoppingOffers(price, special, needs)
}
