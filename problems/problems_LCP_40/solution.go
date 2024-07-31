package problemLCP_40

import (
	"encoding/json"
	"log"
	"strings"
)

func maxmiumScore(cards []int, cnt int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var cards []int
	var cnt int

	if err := json.Unmarshal([]byte(inputValues[0]), &cards); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &cnt); err != nil {
		log.Fatal(err)
	}

	return maxmiumScore(cards, cnt)
}
