package golang

import (
	"leetCode/problems/problems_138"
	"leetCode/problems/problems_152"
	"leetCode/problems/problems_LCR_080"
	"leetCode/problems/problems_LCR_089"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_089", "problems", problemLCR_089.Solve)
	TestEach(t, "LCR_080", "problems", problemLCR_080.Solve)
	TestEach(t, "152", "problems", problem152.Solve)
	TestEach(t, "138", "problems", problem138.Solve)
}
