package golang

import (
	problem "leetCode/problems/problems_326"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "326", "problems", problem.Solve)
}
