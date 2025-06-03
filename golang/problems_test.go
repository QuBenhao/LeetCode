package golang

import (
	"leetCode/problems/problems_LCR_114"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_114", "problems", problemLCR_114.Solve)
}
