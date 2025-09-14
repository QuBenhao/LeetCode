package problem3679

import (
	"encoding/json"
	"log"
	"strings"
)

func minArrivalsToDiscard(arrivals []int, w int, m int) (ans int) {
	var dq []int
	counter := make(map[int]int)
	for i, v := range arrivals {
		for len(dq) > 0 && dq[0] < i-w+1 {
			counter[arrivals[dq[0]]]--
			dq = dq[1:]
		}
		if counter[v] == m {
			ans++
		} else {
			counter[v]++
			dq = append(dq, i)
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arrivals []int
	var w int
	var m int

	if err := json.Unmarshal([]byte(inputValues[0]), &arrivals); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &w); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &m); err != nil {
		log.Fatal(err)
	}

	return minArrivalsToDiscard(arrivals, w, m)
}
