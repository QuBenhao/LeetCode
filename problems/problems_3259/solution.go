package problem3259

import (
	"encoding/json"
	"log"
	"strings"
)

func maxEnergyBoost(a, b []int) int64 {
	n := len(a)
	f := make([][2]int64, n+2)
	for i, x := range a {
		f[i+2][0] = max(f[i+1][0], f[i][1]) + int64(x)
		f[i+2][1] = max(f[i+1][1], f[i][0]) + int64(b[i])
	}
	return max(f[n+1][0], f[n+1][1])
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var energyDrinkA []int
	var energyDrinkB []int

	if err := json.Unmarshal([]byte(inputValues[0]), &energyDrinkA); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &energyDrinkB); err != nil {
		log.Fatal(err)
	}

	return maxEnergyBoost(energyDrinkA, energyDrinkB)
}
