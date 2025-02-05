package golang

import (
	problem "leetCode/problems/problems_47"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "47", "problems", problem.Solve)
}
