package problem2332

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func latestTimeCatchTheBus(buses []int, passengers []int, capacity int) (ans int) {
	sort.Ints(buses)
	sort.Ints(passengers)
	j, c := 0, 0
	for _, bus := range buses {
		c = capacity
		for j < len(passengers) && c > 0 && passengers[j] <= bus {
			c--
			j++
		}
	}
	j--
	if c != 0 {
		ans = buses[len(buses)-1]
	} else {
		ans = passengers[j]
	}
	for j >= 0 && ans == passengers[j] {
		ans--
		j--
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var buses []int
	var passengers []int
	var capacity int

	if err := json.Unmarshal([]byte(inputValues[0]), &buses); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &passengers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &capacity); err != nil {
		log.Fatal(err)
	}

	return latestTimeCatchTheBus(buses, passengers, capacity)
}
