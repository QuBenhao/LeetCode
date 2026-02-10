package golang

import (
	problem "leetCode/problems/problems_3721"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3721", "problems", problem.Solve)
}
