package golang

import (
	problem "leetCode/problems/problems_699"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "699", "problems", problem.Solve)
}
