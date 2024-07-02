package golang

import (
	"leetCode/problems/problems_1"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "1", "problems", problem1.Solve)
}
