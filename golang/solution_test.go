package golang

import (
	problem "leetCode/problems/problems_913"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "913", "problems", problem.Solve)
}
