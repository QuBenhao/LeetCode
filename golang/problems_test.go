package golang

import (
	"leetCode/problems/problems_1"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_071", "problems", problem1.Solve)
}
