package golang

import (
	"leetCode/problems/problems_LCR_051"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_051", "problems", problemLCR_051.Solve)
}
