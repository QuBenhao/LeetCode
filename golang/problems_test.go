package golang

import (
	"leetCode/problems/problems_LCR_082"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_082", "problems", problemLCR_082.Solve)
}
