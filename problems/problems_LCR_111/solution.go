package problemLCR_111

import (
	"encoding/json"
	"log"
	"strings"
)

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
    // 给方程组中的每个变量编号
    id := map[string]int{}
    for _, eq := range equations {
        a, b := eq[0], eq[1]
        if _, has := id[a]; !has {
            id[a] = len(id)
        }
        if _, has := id[b]; !has {
            id[b] = len(id)
        }
    }

    // 建图
    type edge struct {
        to     int
        weight float64
    }
    graph := make([][]edge, len(id))
    for i, eq := range equations {
        v, w := id[eq[0]], id[eq[1]]
        graph[v] = append(graph[v], edge{w, values[i]})
        graph[w] = append(graph[w], edge{v, 1 / values[i]})
    }

    bfs := func(start, end int) float64 {
        ratios := make([]float64, len(graph))
        ratios[start] = 1
        queue := []int{start}
        for len(queue) > 0 {
            v := queue[0]
            queue = queue[1:]
            if v == end {
                return ratios[v]
            }
            for _, e := range graph[v] {
                if w := e.to; ratios[w] == 0 {
                    ratios[w] = ratios[v] * e.weight
                    queue = append(queue, w)
                }
            }
        }
        return -1
    }

    ans := make([]float64, len(queries))
    for i, q := range queries {
        start, hasS := id[q[0]]
        end, hasE := id[q[1]]
        if !hasS || !hasE {
            ans[i] = -1
        } else {
            ans[i] = bfs(start, end)
        }
    }
    return ans
}


func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var equations [][]string
	var values []float64
	var queries [][]string

	if err := json.Unmarshal([]byte(inputValues[0]), &equations); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &values); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &queries); err != nil {
		log.Fatal(err)
	}

	return calcEquation(equations, values, queries)
}
