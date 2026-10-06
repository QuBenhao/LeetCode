package problem1948

import (
	"encoding/json"
	"log"
	"strings"
)

type trieNode struct {
	son     map[string]*trieNode
	name    string // Folder name
	deleted bool   // Deletion flag
}

func deleteDuplicateFolder(paths [][]string) (ans [][]string) {
	root := &trieNode{}
	for _, path := range paths {
		// Insert path into the trie; see 208. Implement Trie
		cur := root
		for _, s := range path {
			if cur.son == nil {
				cur.son = map[string]*trieNode{}
			}
			if cur.son[s] == nil {
				cur.son[s] = &trieNode{}
			}
			cur = cur.son[s]
			cur.name = s
		}
	}

	exprToNode := map[string]*trieNode{} // Parenthesized subtree expression -> subtree root
	var genExpr func(*trieNode) string
	genExpr = func(node *trieNode) string {
		if node.son == nil { // Leaf
			return node.name // The expression is just the folder name
		}

		expr := make([]string, 0, len(node.son)) // Preallocate space
		for _, son := range node.son {
			// Wrap each subtree expression in parentheses
			expr = append(expr, "("+genExpr(son)+")")
		}
		slices.Sort(expr)

		subTreeExpr := strings.Join(expr, "") // Concatenate all subtree expressions in lexicographic order
		n := exprToNode[subTreeExpr]
		if n != nil { // An existing subTreeExpr in the map indicates duplicate folders
			n.deleted = true    // Mark the node recorded in the map for deletion
			node.deleted = true // Mark the current node for deletion
		} else {
			exprToNode[subTreeExpr] = node
		}

		return node.name + subTreeExpr
	}
	for _, son := range root.son {
		genExpr(son)
	}

	// Backtrack through the trie, visiting only undeleted nodes and recording their paths in the answer
	// Similar to 257. Binary Tree Paths
	path := []string{}
	var dfs func(*trieNode)
	dfs = func(node *trieNode) {
		if node.deleted {
			return
		}
		path = append(path, node.name)
		ans = append(ans, slices.Clone(path))
		for _, son := range node.son {
			dfs(son)
		}
		path = path[:len(path)-1] // Restore the previous state
	}
	for _, son := range root.son {
		dfs(son)
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var paths [][]string

	if err := json.Unmarshal([]byte(inputValues[0]), &paths); err != nil {
		log.Fatal(err)
	}

	return deleteDuplicateFolder(paths)
}
