package golang

import (
	"leetCode/problems/problems_32"
	"leetCode/problems/problems_51"
	"leetCode/problems/problems_LCR_049"
	"leetCode/problems/problems_LCR_093"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_049", "problems", problemLCR_049.Solve)
	TestEach(t, "LCR_093", "problems", problemLCR_093.Solve)
	TestEach(t, "51", "problems", problem51.Solve)
	TestEach(t, "32", "problems", problem32.Solve)
}
