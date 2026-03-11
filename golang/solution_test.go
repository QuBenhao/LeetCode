package golang

import (
	problem "leetCode/problems/problems_3600"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3600", "problems", problem.Solve)
}
