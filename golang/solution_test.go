package golang

import (
	problem "leetCode/problems/problems_768"
	"testing"
)

func TestSolution(t *testing.T) {
	TestEach(t, "768", "problems", problem.Solve)
}
