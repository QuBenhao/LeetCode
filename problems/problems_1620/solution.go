package problem1620

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func bestCoordinate(towers [][]int, radius int) []int {
	ans := 0
	ansX, ansY := 0, 0
	radius *= radius
	for x := range 51 {
		for y := range 51 {
			sum := 0
			for _, tower := range towers {
				dx := x - tower[0]
				dy := y - tower[1]
				distSquared := dx*dx + dy*dy
				if distSquared <= radius {
					sum += int(math.Floor(float64(tower[2]) / (1 + math.Sqrt(float64(distSquared)))))
				}
			}
			if sum > ans {
				ans = sum
				ansX, ansY = x, y
			}
		}
	}
	return []int{ansX, ansY}
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var towers [][]int
	var radius int

	if err := json.Unmarshal([]byte(inputValues[0]), &towers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &radius); err != nil {
		log.Fatal(err)
	}

	return bestCoordinate(towers, radius)
}
