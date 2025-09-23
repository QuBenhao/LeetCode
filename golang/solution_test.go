package golang

import (
	problem "leetCode/problems/problems_166"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "166", "problems", problem.Solve)
}
