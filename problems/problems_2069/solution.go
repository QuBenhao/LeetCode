package problem2069

import (
	"encoding/json"
	"log"
	"strings"
)

var DIRS = []string{"East", "North", "West", "South"}

type Robot struct {
	m, n, total, loc int
	moved            bool
}

func Constructor(width int, height int) Robot {
	return Robot{
		m:     width,
		n:     height,
		total: 2 * (width + height - 2),
		loc:   0,
		moved: false,
	}
}

func (r *Robot) Step(num int) {
	num %= r.total
	r.loc = (r.loc + num) % r.total
	r.moved = true
}

func (r *Robot) GetPos() []int {
	return r.move()[:2]
}

func (r *Robot) GetDir() string {
	return DIRS[r.move()[2]]
}

func (r *Robot) move() []int {
	if !r.moved {
		return []int{0, 0, 0}
	}
	if r.loc < r.m {
		if r.loc == 0 {
			return []int{r.loc, 0, 3}
		}
		return []int{r.loc, 0, 0}
	}
	if r.loc < r.m+r.n-1 {
		return []int{r.m - 1, r.loc - r.m + 1, 1}
	}
	if r.loc < 2*r.m+r.n-2 {
		return []int{r.m - 1 - (r.loc - r.m - r.n + 2), r.n - 1, 2}
	}
	return []int{0, r.total - r.loc, 3}
}

/**
 * Your Robot object will be instantiated and called as such:
 * obj := Constructor(width, height);
 * obj.Step(num);
 * param_2 := obj.GetPos();
 * param_3 := obj.GetDir();
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
	obj := Constructor(int(opValues[0][0].(float64)), int(opValues[0][1].(float64)))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "step", "Step":
			res = nil
			obj.Step(int(opValues[i][0].(float64)))
		case "getPos", "GetPos":
			res = obj.GetPos()
		case "getDir", "GetDir":
			res = obj.GetDir()
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
