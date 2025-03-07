package problem2234

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumBeauty(flowers []int, newFlowers int64, target int, full int, partial int) int64 {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var flowers []int
	var newFlowers int64
	var target int
	var full int
	var partial int

	if err := json.Unmarshal([]byte(inputValues[0]), &flowers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &newFlowers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &target); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &full); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &partial); err != nil {
		log.Fatal(err)
	}

	return maximumBeauty(flowers, newFlowers, target, full, partial)
}
