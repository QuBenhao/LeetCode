package problem2105

import (
	"encoding/json"
	"log"
	"strings"
)

func Solve(input string) int {
	values := strings.Split(input, "\n")
	var plants []int
	var capacityA int
	var capacityB int

	if err := json.Unmarshal([]byte(values[0]), &plants); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &capacityA); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[2]), &capacityB); err != nil {
		log.Fatal(err)
	}

	return minimumRefill(plants, capacityA, capacityB)
}

func minimumRefill(plants []int, capacityA int, capacityB int) int {

}