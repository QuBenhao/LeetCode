package golang

import (
	problem "leetCode/problems/problems_416"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "416", "problems", problem.Solve)
}
