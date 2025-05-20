package problem3096

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumLevels(possible []int) int {
	s := 0
	for _, v := range possible {
		if v == 0 {
			s--
		} else {
			s += v
		}
	}
	pre := 0
	for i, v := range possible[:len(possible)-1] {
		if v == 0 {
			pre--
		} else {
			pre += v
		}
		if pre*2 > s {
			return i + 1
		}
	}
	return -1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var possible []int

	if err := json.Unmarshal([]byte(inputValues[0]), &possible); err != nil {
		log.Fatal(err)
	}

	return minimumLevels(possible)
}
