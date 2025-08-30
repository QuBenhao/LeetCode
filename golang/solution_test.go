package golang

import (
	problem "leetCode/problems/problems_37"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "37", "problems", problem.Solve)
}
