package problem3531

import (
	"encoding/json"
	"log"
	"strings"
)

func countCoveredBuildings(n int, buildings [][]int) (ans int) {
	bound_x := make([][2]int, n+1)
	bound_y := make([][2]int, n+1)
	for i := range n {
		bound_x[i][0] = n + 1
		bound_y[i][0] = n + 1
	}
	for _, building := range buildings {
		x, y := building[0], building[1]
		bound_x[x][0] = min(bound_x[x][0], y)
		bound_x[x][1] = max(bound_x[x][1], y)
		bound_y[y][0] = min(bound_y[y][0], x)
		bound_y[y][1] = max(bound_y[y][1], x)
	}
	for _, building := range buildings {
		x, y := building[0], building[1]
		if bound_x[x][0] < y && bound_x[x][1] > y &&
			bound_y[y][0] < x && bound_y[y][1] > x {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var buildings [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &buildings); err != nil {
		log.Fatal(err)
	}

	return countCoveredBuildings(n, buildings)
}
