package problem699

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func fallingSquares(positions [][]int) []int {
	points := map[int]interface{}{}
	for _, pos := range positions {
		points[pos[0]] = nil
		points[pos[0]+pos[1]-1] = nil
	}
	idxMap := make(map[int]int, len(points))
	ranges := make([]int, 0, len(points))
	sortPoints := make([]int, 0, len(points))
	for p := range points {
		sortPoints = append(sortPoints, p)
		ranges = append(ranges, 0)
	}
	sort.Ints(sortPoints)
	for i, p := range sortPoints {
		idxMap[p] = i
	}
	ans := make([]int, 0, len(positions))
	cur := 0
	for _, pos := range positions {
		left, right := idxMap[pos[0]], idxMap[pos[0]+pos[1]-1]
		newHeight := 0
		for i := left; i <= right; i++ {
			newHeight = max(newHeight, ranges[i])
		}
		newHeight += pos[1]
		for i := left; i <= right; i++ {
			ranges[i] = newHeight
		}
		cur = max(cur, newHeight)
		ans = append(ans, cur)
	}
	return ans
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var positions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &positions); err != nil {
		log.Fatal(err)
	}

	return fallingSquares(positions)
}
