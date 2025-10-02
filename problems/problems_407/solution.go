package problem407

import (
	"encoding/json"
	"log"
	"strings"
)

func trapRainWater(heightMap [][]int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var heightMap [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &heightMap); err != nil {
		log.Fatal(err)
	}

	return trapRainWater(heightMap)
}
