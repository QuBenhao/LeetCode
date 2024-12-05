package golang

import (
	problem "leetCode/problems/problems_999"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "999", "problems", problem.Solve)
}
