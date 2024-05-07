package problem2079

import (
	"encoding/json"
	"log"
	"strings"
)

func Solve(input string) int {
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

func wateringPlants(plants []int, capacity int) int {

}