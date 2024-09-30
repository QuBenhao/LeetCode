package golang

import (
	problem "leetCode/problems/problems_983"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "983", "problems", problem.Solve)
}
