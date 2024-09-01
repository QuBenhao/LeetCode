package problemLCR_037

import (
	"encoding/json"
	"log"
	"strings"
)

func asteroidCollision(asteroids []int) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var asteroids []int

	if err := json.Unmarshal([]byte(inputValues[0]), &asteroids); err != nil {
		log.Fatal(err)
	}

	return asteroidCollision(asteroids)
}
