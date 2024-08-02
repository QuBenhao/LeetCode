package golang

import (
	"leetCode/problems/problems_108"
	"leetCode/problems/problems_21"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "108", "problems", problem108.Solve)
	TestEach(t, "21", "problems", problem21.Solve)
}
