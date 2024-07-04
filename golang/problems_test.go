package golang

import (
	"leetCode/problems/problems_283"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "283", "problems", problem283.Solve)
}
