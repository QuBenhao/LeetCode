package golang

import (
	problem "leetCode/problems/problems_20"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "20", "problems", problem.Solve)
}
