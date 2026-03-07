package golang

import (
	problem "leetCode/problems/problems_1980"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "1980", "problems", problem.Solve)
}
