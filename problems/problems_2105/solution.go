package problem2105

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumRefill(plants []int, capacityA, capacityB int) (ans int) {
	a, b := capacityA, capacityB
	i, j := 0, len(plants)-1
	for i < j {
		// Alice waters plant i
		if a < plants[i] {
			// Not enough water; refill the watering can
			ans++
			a = capacityA
		}
		a -= plants[i]
		i++
		// Bob waters plant j
		if b < plants[j] {
			// Not enough water; refill the watering can
			ans++
			b = capacityB
		}
		b -= plants[j]
		j--
	}
	// If Alice and Bob reach the same plant, the person with more water remaining waters it
	if i == j && max(a, b) < plants[i] {
		// Not enough water; refill the watering can
		ans++
	}
	return
}

func Solve(input string) any {
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
