package problem2410

import (
	"encoding/json"
	"log"
	"strings"
)

func matchPlayersAndTrainers(players []int, trainers []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var players []int
	var trainers []int

	if err := json.Unmarshal([]byte(inputValues[0]), &players); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &trainers); err != nil {
		log.Fatal(err)
	}

	return matchPlayersAndTrainers(players, trainers)
}
