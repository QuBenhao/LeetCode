package problem3259

import (
	"encoding/json"
	"log"
	"strings"
)

func maxEnergyBoost(energyDrinkA []int, energyDrinkB []int) int64 {
    
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
