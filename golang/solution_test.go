package golang

import (
	problem "leetCode/problems/problems_350"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "350", "problems", problem.Solve)
}
