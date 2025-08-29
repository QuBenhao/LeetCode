package problem735

import (
	"encoding/json"
	"log"
	"strings"
)

func asteroidCollision(asteroids []int) []int {
	ans := make([]int, len(asteroids))
	idx := 0
	for _, asteroid := range asteroids {
		if asteroid > 0 {
			ans[idx] = asteroid
			idx++
		} else {
			for idx > 0 && ans[idx-1] > 0 && ans[idx-1] < -asteroid {
				idx--
			}
			if idx == 0 || ans[idx-1] < 0 {
				ans[idx] = asteroid
				idx++
			} else if ans[idx-1] == -asteroid {
				idx--
			}
		}
	}
	ans = ans[:idx]
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var asteroids []int

	if err := json.Unmarshal([]byte(inputValues[0]), &asteroids); err != nil {
		log.Fatal(err)
	}

	return asteroidCollision(asteroids)
}
