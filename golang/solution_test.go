package golang

import (
	problem "leetCode/problems/problems_688"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "688", "problems", problem.Solve)
}
