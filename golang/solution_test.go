package golang

import (
	problem "leetCode/problems/problems_891"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "891", "problems", problem.Solve)
}
