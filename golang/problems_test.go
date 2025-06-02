package golang

import (
	"leetCode/problems/problems_62"
	"leetCode/problems/problems_LCR_114"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "62", "problems", problem62.Solve)
	TestEach(t, "LCR_114", "problems", problemLCR_114.Solve)
}
