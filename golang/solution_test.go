package golang

import (
	problem "leetCode/problems/problems_75"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "75", "problems", problem.Solve)
}
