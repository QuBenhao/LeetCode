package golang

import (
	problem "leetCode/problems/problems_3145"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "3145", "problems", problem.Solve)
}
