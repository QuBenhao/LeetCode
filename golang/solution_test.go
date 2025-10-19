package golang

import (
	problem "leetCode/problems/problems_2011"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "2011", "problems", problem.Solve)
}
