package golang

import (
	problem "leetCode/problems/problems_853"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "853", "problems", problem.Solve)
}
