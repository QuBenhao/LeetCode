package golang

import (
	problem "leetCode/problems/problems_2014"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "2014", "problems", problem.Solve)
}
