package problem1845

import (
	"container/heap"
	"encoding/json"
	"log"
	"sort"
	"strings"
)

type SeatManager struct {
	sort.IntSlice
}

func Constructor(n int) SeatManager {
	m := SeatManager{make([]int, n)}
	for i := range m.IntSlice {
		m.IntSlice[i] = i + 1
	}
	return m
}

func (m *SeatManager) Reserve() int {
	return heap.Pop(m).(int)
}

func (m *SeatManager) Unreserve(seatNumber int) {
	heap.Push(m, seatNumber)
}

func (m *SeatManager) Push(v any) { m.IntSlice = append(m.IntSlice, v.(int)) }
func (m *SeatManager) Pop() any {
	a := m.IntSlice
	v := a[len(a)-1]
	m.IntSlice = a[:len(a)-1]
	return v
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Reserve();
 * obj.Unreserve(seatNumber);
 */

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]interface{}
	var ans []interface{}
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
		var res interface{}
		switch operators[i] {
		case "reserve", "Reserve":
			res = obj.Reserve()
		case "unreserve", "Unreserve":
			res = nil
			obj.Unreserve(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
