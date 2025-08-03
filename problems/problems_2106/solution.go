package problem2106

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func maxTotalFruits(fruits [][]int, startPos int, k int) (ans int) {
	left, _ := slices.BinarySearchFunc(fruits, startPos-k, func(a []int, b int) int {
		return a[0] - b
	})
	maxDistance := startPos + k
	s := 0
	for right := left; right < len(fruits) && fruits[right][0] <= maxDistance; right++ {
		fruit := fruits[right]
		pos := fruit[0]
		s += fruit[1]
		if pos > maxDistance {
			break
		}
		for pos*2-fruits[left][0]-startPos > k && pos+startPos-fruits[left][0]*2 > k {
			s -= fruits[left][1]
			left++
		}
		ans = max(ans, s)
	}

	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var fruits [][]int
	var startPos int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &fruits); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &startPos); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return maxTotalFruits(fruits, startPos, k)
}
