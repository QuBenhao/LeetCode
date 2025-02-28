package golang

import (
	problem "leetCode/problems/problems_131"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "131", "problems", problem.Solve)
}
