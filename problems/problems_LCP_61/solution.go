package problemLCP_61

import (
	"encoding/json"
	"log"
	"strings"
)

func temperatureTrend(temperatureA []int, temperatureB []int) (ans int) {
	for i, cur := 1, 0; i < len(temperatureA); i++ {
		if d1, d2 := temperatureA[i]-temperatureA[i-1], temperatureB[i]-temperatureB[i-1]; (d1*d2 > 0) || (d1 == 0 && d2 == 0) {
			cur++
			ans = max(ans, cur)
		} else {
			cur = 0
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var temperatureA []int
	var temperatureB []int

	if err := json.Unmarshal([]byte(values[0]), &temperatureA); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &temperatureB); err != nil {
		log.Fatal(err)
	}

	return temperatureTrend(temperatureA, temperatureB)
}
