package golang

import (
	"leetCode/problems/problems_LCR_096"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_096", "problems", problemLCR_096.Solve)
}
