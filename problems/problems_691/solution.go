package problem691

import (
	"encoding/json"
	"log"
	"strings"
)

func minStickers(stickers []string, target string) int {
    targetSet := map[rune]bool{}
    for _, r := range target {
        targetSet[r] = true
    }
    available := []map[rune]int{}
    for _, s := range stickers {
        if c := getCounter(s, targetSet); c != nil {
            available = append(available, c)
        }
    }
    queue, explored := []string{target}, map[string]int{target:0}
    for len(queue) > 0 {
        cur := queue[0]
        queue = queue[1:]
        for _, avl := range available {
            if avl[rune(cur[0])] > 0 {
                nxt := transfer(cur, avl)
                if len(nxt) == 0 {
                    return explored[cur] + 1
                }
                if _, ok := explored[nxt]; !ok {
                    queue = append(queue, nxt)
                    explored[nxt] = explored[cur] + 1
                }
            }
        }
    }
    return -1
}

func getCounter(s string, chars map[rune]bool) map[rune]int {
    res := map[rune]int{}
    for _, r := range s {
        if chars[r] {
            res[r]++
        }
    }
    if len(res) == 0 {
        return nil
    }
    return res
}

func transfer(s string, mp map[rune]int) string {
    for k, v := range mp {
        s = strings.Replace(s, string(k), "", v)
    }
    return s
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var stickers []string
	var target string

	if err := json.Unmarshal([]byte(inputValues[0]), &stickers); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}

	return minStickers(stickers, target)
}
