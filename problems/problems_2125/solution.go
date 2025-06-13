package problem2125

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfBeams(bank []string) (ans int) {
	prev := 0
	for _, row := range bank {
		count := 0
		for _, b := range row {
			if b == '1' {
				count++
			}
		}
		ans += count * prev
		if count > 0 {
			prev = count
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var bank []string

	if err := json.Unmarshal([]byte(inputValues[0]), &bank); err != nil {
		log.Fatal(err)
	}

	return numberOfBeams(bank)
}
