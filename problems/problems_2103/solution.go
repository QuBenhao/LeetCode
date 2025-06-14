package problem2103

import (
	"encoding/json"
	"log"
	"strings"
)

func countPoints(rings string) (ans int) {
    count := make([]int, 10)
    for i := 0; i < len(rings); i += 2 {
        count[rings[i+1] - '0'] |= 1 << strings.IndexByte("RGB", rings[i])
    }
    for _, v := range count {
        if v == (1<<3)-1 {
            ans++
        }
    }
    return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var rings string

	if err := json.Unmarshal([]byte(inputValues[0]), &rings); err != nil {
		log.Fatal(err)
	}

	return countPoints(rings)
}
