package problem1833

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func maxIceCream(costs []int, coins int) (ans int) {
	sort.Ints(costs)
	for _, cost := range costs {
		if coins < cost {
			return
		}
		ans++
		coins -= cost
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var costs []int
	var coins int

	if err := json.Unmarshal([]byte(inputValues[0]), &costs); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &coins); err != nil {
		log.Fatal(err)
	}

	return maxIceCream(costs, coins)
}
