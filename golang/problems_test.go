package golang

import (
	"leetCode/problems/problems_22"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "22", "problems", problem22.Solve)
}
