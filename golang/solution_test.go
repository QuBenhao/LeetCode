package golang

import (
	problem "leetCode/problems/problems_807"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "807", "problems", problem.Solve)
}
