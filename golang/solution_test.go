package golang

import (
	problem "leetCode/problems/problems_721"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "721", "problems", problem.Solve)
}
