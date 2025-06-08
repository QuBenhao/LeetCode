package golang

import (
	problem "leetCode/problems/problems_440"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "440", "problems", problem.Solve)
}
