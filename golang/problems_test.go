package golang

import (
	"leetCode/problems/problems_124"
	"leetCode/problems/problems_146"
	"leetCode/problems/problems_LCR_009"
	"leetCode/problems/problems_LCR_016"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_009", "problems", problemLCR_009.Solve)
	TestEach(t, "LCR_016", "problems", problemLCR_016.Solve)
	TestEach(t, "146", "problems", problem146.Solve)
	TestEach(t, "124", "problems", problem124.Solve)
}
