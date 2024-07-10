package golang

import (
	"leetCode/problems/problems_46"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "46", "problems", problem46.Solve)
}
