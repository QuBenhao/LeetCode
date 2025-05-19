package problem2353

import (
	"container/heap"
	"encoding/json"
	"log"
	"strings"
)

type pair struct {
	rating int
	s      string
}

type FoodRatings struct {
	foodMap    map[string]pair
	cuisineMap map[string]*hp
}

func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
	foodMap := map[string]pair{}
	cuisineMap := map[string]*hp{}
	for i, food := range foods {
		rating, cuisine := ratings[i], cuisines[i]
		foodMap[food] = pair{rating, cuisine}
		if cuisineMap[cuisine] == nil {
			cuisineMap[cuisine] = &hp{}
		}
		heap.Push(cuisineMap[cuisine], pair{rating, food})
	}
	return FoodRatings{foodMap, cuisineMap}
}

func (fr *FoodRatings) ChangeRating(food string, newRating int) {
	p := fr.foodMap[food]
	// 直接添加新数据，后面查询时再删除旧的
	heap.Push(fr.cuisineMap[p.s], pair{newRating, food})
	p.rating = newRating
	fr.foodMap[food] = p
}

func (fr *FoodRatings) HighestRated(cuisine string) string {
	h := fr.cuisineMap[cuisine]
	// 懒删除
	for h.Len() > 0 && (*h)[0].rating != fr.foodMap[(*h)[0].s].rating {
		heap.Pop(h)
	}
	return (*h)[0].s
}

type hp []pair

func (h hp) Len() int { return len(h) }
func (h hp) Less(i, j int) bool {
	a, b := h[i], h[j]
	return a.rating > b.rating || (a.rating == b.rating && a.s < b.s)
}
func (h hp) Swap(i, j int) { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)   { *h = append(*h, v.(pair)) }
func (h *hp) Pop() any     { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

/**
 * Your FoodRatings object will be instantiated and called as such:
 * obj := Constructor(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * param_2 := obj.HighestRated(cuisine);
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
	var foodsArr []string
	if v, ok := opValues[0][0].([]string); ok {
		foodsArr = v
	} else {
		for _, vi := range opValues[0][0].([]interface{}) {
			foodsArr = append(foodsArr, vi.(string))
		}
	}
	var cuisinesArr []string
	if v, ok := opValues[0][1].([]string); ok {
		cuisinesArr = v
	} else {
		for _, vi := range opValues[0][1].([]interface{}) {
			cuisinesArr = append(cuisinesArr, vi.(string))
		}
	}
	var ratingsArr []int
	if v, ok := opValues[0][2].([]int); ok {
		ratingsArr = v
	} else {
		for _, vi := range opValues[0][2].([]interface{}) {
			ratingsArr = append(ratingsArr, int(vi.(float64)))
		}
	}
	obj := Constructor(foodsArr, cuisinesArr, ratingsArr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "changeRating", "ChangeRating":
			res = nil
			obj.ChangeRating(opValues[i][0].(string), int(opValues[i][1].(float64)))
		case "highestRated", "HighestRated":
			res = obj.HighestRated(opValues[i][0].(string))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
