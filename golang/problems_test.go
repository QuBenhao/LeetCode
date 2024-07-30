package golang

import (
	"leetCode/problems/problems_5"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "5", "problems", problem5.Solve)
}
