package problemLCR_041

import (
	"container/list"
	"encoding/json"
	"log"
	"strings"
)

type MovingAverage struct {
	size   int
	window list.List
	sum    float64
}

/** Initialize your data structure here. */
func Constructor(size int) MovingAverage {
	return MovingAverage{
		size:   size,
		window: list.List{},
		sum:    0.0,
	}
}

func (ma *MovingAverage) Next(val int) float64 {
	if ma.window.Len() == ma.size {
		front := ma.window.Front()
		ma.sum -= float64(front.Value.(int))
		ma.window.Remove(front)
	}
	ma.sum += float64(val)
	ma.window.PushBack(val)
	return ma.sum / float64(ma.window.Len())
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * obj := Constructor(size);
 * param_1 := obj.Next(val);
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
	obj := Constructor(int(opValues[0][0].(float64)))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "next", "Next":
			res = obj.Next(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
