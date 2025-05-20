package problemLCR_037

import (
	"encoding/json"
	"log"
	"strings"
)

func asteroidCollision(asteroids []int) (ans []int) {
	stack := []int{}
out:
	for _, ast := range asteroids {
		for len(stack) > 0 && ast < 0 && stack[len(stack)-1] > 0 {
			if stack[len(stack)-1] < -ast {
				stack = stack[:len(stack)-1]
				continue
			} else if stack[len(stack)-1] == -ast {
				stack = stack[:len(stack)-1]
			}
			continue out
		}
		stack = append(stack, ast)
	}
	return stack
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var asteroids []int

	if err := json.Unmarshal([]byte(inputValues[0]), &asteroids); err != nil {
		log.Fatal(err)
	}

	return asteroidCollision(asteroids)
}
