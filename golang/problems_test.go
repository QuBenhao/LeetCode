package golang

import (
	"leetCode/problems/problems_104"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "104", "problems", problem104.Solve)
}
