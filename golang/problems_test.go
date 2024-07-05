package golang

import (
	"leetCode/problems/problems_3"
	"leetCode/problems/problems_73"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3", "problems", problem3.Solve)
	TestEach(t, "73", "problems", problem73.Solve)
}
