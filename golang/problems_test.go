package golang

import (
	"leetCode/problems/problems_LCR_107"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_107", "problems", problemLCR_107.Solve)
}
