package golang

import (
	"leetCode/problems/problems_LCR_018"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_018", "problems", problemLCR_018.Solve)
}
