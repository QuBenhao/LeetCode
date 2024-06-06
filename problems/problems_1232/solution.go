package problem1232

import (
	"encoding/json"
	"log"
	"strings"
)

func checkStraightLine(coordinates [][]int) bool {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var coordinates [][]int

	if err := json.Unmarshal([]byte(values[0]), &coordinates); err != nil {
		log.Fatal(err)
	}

	return checkStraightLine(coordinates)
}
