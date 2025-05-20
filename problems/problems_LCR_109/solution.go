package problemLCR_109

import (
	"encoding/json"
	"log"
	"strings"
)

func openLock(deadends []string, target string) int {
	dead := make(map[string]bool)
	for _, d := range deadends {
		dead[d] = true
	}
	if dead["0000"] {
		return -1
	}
	if target == "0000" {
		return 0
	}
	visited := make(map[string]bool)
	visited["0000"] = true
	queue := []string{"0000"}
	step := 0
	for len(queue) > 0 {
		step++
		size := len(queue)
		for i := 0; i < size; i++ {
			cur := queue[0]
			queue = queue[1:]
			for j := 0; j < 4; j++ {
				for k := -1; k <= 1; k += 2 {
					next := cur[:j] + string(rune((int(cur[j]-'0')+k+10)%10+'0')) + cur[j+1:]
					if next == target {
						return step
					}
					if !dead[next] && !visited[next] {
						visited[next] = true
						queue = append(queue, next)
					}
				}
			}
		}
	}
	return -1
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var deadends []string
	var target string

	if err := json.Unmarshal([]byte(inputValues[0]), &deadends); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return openLock(deadends, target)
}
