package problem622

import (
	"encoding/json"
	"log"
	"strings"
)

type MyCircularQueue struct {
	arr []int
	k   int
	sz  int
	idx int
}

func Constructor(k int) MyCircularQueue {
	return MyCircularQueue{
		arr: make([]int, k),
		k:   k,
		sz:  0,
		idx: 0,
	}
}

func (mcq *MyCircularQueue) EnQueue(value int) bool {
	if mcq.sz == mcq.k {
		return false
	}
	mcq.arr[mcq.idx] = value
	mcq.idx = (mcq.idx + 1) % mcq.k
	mcq.sz++
	return true
}

func (mcq *MyCircularQueue) DeQueue() bool {
	if mcq.sz == 0 {
		return false
	}
	mcq.sz--
	return true
}

func (mcq *MyCircularQueue) Front() int {
	if mcq.sz == 0 {
		return -1
	}
	return mcq.arr[(mcq.idx-mcq.sz+mcq.k)%mcq.k]
}

func (mcq *MyCircularQueue) Rear() int {
	if mcq.sz == 0 {
		return -1
	}
	return mcq.arr[(mcq.idx-1+mcq.k)%mcq.k]
}

func (mcq *MyCircularQueue) IsEmpty() bool {
	return mcq.sz == 0
}

func (mcq *MyCircularQueue) IsFull() bool {
	return mcq.sz == mcq.k
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.EnQueue(value);
 * param_2 := obj.DeQueue();
 * param_3 := obj.Front();
 * param_4 := obj.Rear();
 * param_5 := obj.IsEmpty();
 * param_6 := obj.IsFull();
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
		case "enQueue", "EnQueue":
			res = obj.EnQueue(int(opValues[i][0].(float64)))
		case "deQueue", "DeQueue":
			res = obj.DeQueue()
		case "front", "Front":
			res = obj.Front()
		case "rear", "Rear":
			res = obj.Rear()
		case "isEmpty", "IsEmpty":
			res = obj.IsEmpty()
		case "isFull", "IsFull":
			res = obj.IsFull()
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
