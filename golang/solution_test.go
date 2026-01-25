package golang

import (
	problem "leetCode/problems/problems_1200"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1200", "problems", problem.Solve)
}
