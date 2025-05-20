package problem1232

import (
	"encoding/json"
	"log"
	"strings"
)

func checkStraightLine(coordinates [][]int) bool {
	xd, yd, c := coordinates[1][0]-coordinates[0][0], coordinates[1][1]-coordinates[0][1],
		coordinates[0][0]*coordinates[1][1]-coordinates[1][0]*coordinates[0][1]
	for _, coordinate := range coordinates {
		x, y := coordinate[0], coordinate[1]
		if x*yd-y*xd != c {
			return false
		}
	}
	return true
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var coordinates [][]int

	if err := json.Unmarshal([]byte(values[0]), &coordinates); err != nil {
		log.Fatal(err)
	}

	return checkStraightLine(coordinates)
}
