package problemLCR_042

import (
	"encoding/json"
	"log"
	"strings"
)

type RecentCounter struct {
	recent []int
}

func Constructor() RecentCounter {
	return RecentCounter{}
}

func (this *RecentCounter) Ping(t int) int {
	if len(this.recent) > 0 {
		left, right := 0, len(this.recent)
		for left < right {
			mid := (left + right) / 2
			if this.recent[mid] < t-3000 {
				left = mid + 1
			} else {
				right = mid
			}
		}
		this.recent = this.recent[left:]
	}
	this.recent = append(this.recent, t)
	return len(this.recent)
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ping(t);
 */

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]any
	var ans []any
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor()
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "ping", "Ping":
			res = obj.Ping(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
