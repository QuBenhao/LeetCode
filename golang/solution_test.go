package golang

import (
	problem "leetCode/problems/problems_857"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "857", "problems", problem.Solve)
}
