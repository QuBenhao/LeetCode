package problem679

import (
	"encoding/json"
	"log"
	"strings"
)

const (
	TARGET  = 24.0
	EPSILON = 1e-6
)

func judgePoint24(cards []int) bool {
	var backtrack func([]float64) bool
	backtrack = func(nums []float64) bool {
		if len(nums) == 1 {
			return abs(nums[0]-TARGET) < EPSILON
		}
		for i, x := range nums {
			for j := i + 1; j < len(nums); j++ {
				var nextNums []float64
				for k, other := range nums {
					if k != i && k != j {
						nextNums = append(nextNums, other)
					}
				}
				y := nums[j]
				for op := range 6 {
					switch op {
					case 0:
						nextNums = append(nextNums, x+y)
					case 1:
						nextNums = append(nextNums, x-y)
					case 2:
						nextNums = append(nextNums, y-x)
					case 3:
						nextNums = append(nextNums, x*y)
					case 4:
						if abs(y) < EPSILON {
							continue
						}
						nextNums = append(nextNums, x/y)

					case 5:
						if abs(x) < EPSILON {
							continue
						}
						nextNums = append(nextNums, y/x)

					}
					if backtrack(nextNums) {
						return true
					}
					nextNums = nextNums[:len(nextNums)-1] // backtrack, remove last element
				}

			}
		}
		return false
	}

	floatCards := make([]float64, len(cards))
	for i, v := range cards {
		floatCards[i] = float64(v)
	}
	return backtrack(floatCards)
}

func abs(x float64) float64 {
	if x < 0 {
		return -x
	}
	return x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var cards []int

	if err := json.Unmarshal([]byte(inputValues[0]), &cards); err != nil {
		log.Fatal(err)
	}

	return judgePoint24(cards)
}
