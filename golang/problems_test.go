package golang

import (
	"leetCode/problems/problems_11"
	"leetCode/problems/problems_54"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "11", "problems", problem11.Solve)
	TestEach(t, "54", "problems", problem54.Solve)
}
