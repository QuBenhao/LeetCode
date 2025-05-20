package problem2079

import (
	"encoding/json"
	"log"
	"strings"
)

func wateringPlants(plants []int, capacity int) int {
	ans := len(plants)
	water := capacity
	for i, need := range plants {
		if water < need {
			ans += i * 2
			water = capacity
		}
		water -= need
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var plants []int
	var capacity int

	if err := json.Unmarshal([]byte(values[0]), &plants); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &capacity); err != nil {
		log.Fatal(err)
	}

	return wateringPlants(plants, capacity)
}
