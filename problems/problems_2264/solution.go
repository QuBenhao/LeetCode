package problem2264

import (
	"encoding/json"
	"log"
	"strings"
)

func largestGoodInteger(num string) (ans string) {
	for left, right := 0, 0; right < len(num); right++ {
		if num[left] != num[right] {
			left = right
			continue
		}
		if right-left == 2 {
			ans = max(ans, num[left:right+1])
			left++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num string

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return largestGoodInteger(num)
}
