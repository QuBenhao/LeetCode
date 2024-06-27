package problem2742

import (
	"encoding/json"
	"log"
	"strings"
)

func paintWalls(cost []int, time []int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var cost []int
	var time []int

	if err := json.Unmarshal([]byte(values[0]), &cost); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &time); err != nil {
		log.Fatal(err)
	}

	return paintWalls(cost, time)
}
