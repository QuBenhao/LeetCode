package golang

import (
	problem "leetCode/problems/problems_2016"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "2016", "problems", problem.Solve)
}
