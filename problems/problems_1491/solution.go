package problem1491

import (
	"encoding/json"
	"log"
	"strings"
)

func average(salary []int) float64 {
	s, mx, mn := 0, salary[0], salary[0]
	for _, v := range salary {
		s, mx, mn = s+v, max(mx, v), min(mn, v)
	}
	return float64(s-mx-mn) / float64(len(salary)-2)
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var salary []int

	if err := json.Unmarshal([]byte(values[0]), &salary); err != nil {
		log.Fatal(err)
	}

	return average(salary)
}
