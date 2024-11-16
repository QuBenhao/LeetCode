package golang

import (
	problem "leetCode/problems/problems_825"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "825", "problems", problem.Solve)
}
