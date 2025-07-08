package golang

import (
	problem "leetCode/problems/problems_777"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "777", "problems", problem.Solve)
}
