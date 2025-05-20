package problem706

import (
	"encoding/json"
	"log"
	"strings"
)

type MyHashMap struct {
	m map[int]int
}

func Constructor() MyHashMap {
	return MyHashMap{make(map[int]int)}
}

func (this *MyHashMap) Put(key int, value int) {
	this.m[key] = value
}

func (this *MyHashMap) Get(key int) int {
	if v, ok := this.m[key]; !ok {
		return -1
	} else {
		return v
	}
}

func (this *MyHashMap) Remove(key int) {
	delete(this.m, key)
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var opts []string
	var vals [][]any
	var ans []any
	if err := json.Unmarshal([]byte(values[0]), &opts); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(values[1]), &vals); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor()
	ans = append(ans, nil)
	for i := 1; i < len(opts); i++ {
		var res any
		switch opts[i] {
		case "put", "Put":
			res = nil
			obj.Put(int(vals[i][0].(float64)), int(vals[i][1].(float64)))
		case "get", "Get":
			res = obj.Get(int(vals[i][0].(float64)))
		case "remove", "Remove":
			res = nil
			obj.Remove(int(vals[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
