package golang

import (
	problem "leetCode/problems/problems_118"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "118", "problems", problem.Solve)
}
