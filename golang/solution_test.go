package golang

import (
	problem "leetCode/problems/problems_11"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "11", "problems", problem.Solve)
}
