package node_neighbours

type Node struct {
	Val       int
	Neighbors []*Node
}

func ArrayRelationToNodeNeighbour(arr [][]int) *Node {
	if arr == nil || len(arr) == 0 {
		return nil
	}
	var nodes []*Node
	for i := 1; i <= len(arr); i++ {
		node := &Node{Val: i}
		nodes = append(nodes, node)
	}
	for i, vals := range arr {
		for _, val := range vals {
			nodes[i].Neighbors = append(nodes[i].Neighbors, nodes[val-1])
		}
	}
	return nodes[0]
}

func NodeNeighbourToArrayRelation(head *Node) (ans []any) {
	if head == nil {
		return []any{}
	}

	explored := map[int]any{head.Val: nil}
	var dfs func(cur *Node)
	dfs = func(cur *Node) {
		if len(ans) < cur.Val {
			for i := len(ans); i < cur.Val; i++ {
				ans = append(ans, []any{})
			}
			for _, nd := range cur.Neighbors {
				ans[len(ans)-1] = append(ans[len(ans)-1].([]any), nd.Val)
			}
		} else {
			for _, nd := range cur.Neighbors {
				ans[cur.Val-1] = append(ans[cur.Val-1].([]any), nd.Val)
			}
		}
		for _, nd := range cur.Neighbors {
			if _, ok := explored[nd.Val]; !ok {
				explored[nd.Val] = nil
				dfs(nd)
			}
		}
	}
	dfs(head)
	return
}
