package golang

import (
	problem "leetCode/problems/problems_2999"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "2999", "problems", problem.Solve)
}
