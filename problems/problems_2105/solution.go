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
		// Alice 给植物 i 浇水
		if a < plants[i] {
			// 没有足够的水，重新灌满水罐
			ans++
			a = capacityA
		}
		a -= plants[i]
		i++
		// Bob 给植物 j 浇水
		if b < plants[j] {
			// 没有足够的水，重新灌满水罐
			ans++
			b = capacityB
		}
		b -= plants[j]
		j--
	}
	// Alice 和 Bob 到达同一株植物，那么当前水罐中水更多的人会给这株植物浇水
	if i == j && max(a, b) < plants[i] {
		// 没有足够的水，重新灌满水罐
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
