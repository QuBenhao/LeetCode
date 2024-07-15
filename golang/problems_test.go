package golang

import (
	"leetCode/problems/problems_64"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "64", "problems", problem64.Solve)
}
