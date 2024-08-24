package golang

import (
	"leetCode/problems/problems_105"
	"leetCode/problems/problems_42"
	"leetCode/problems/problems_LCR_001"
	"leetCode/problems/problems_LCR_031"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "LCR_001", "problems", problemLCR_001.Solve)
	TestEach(t, "LCR_031", "problems", problemLCR_031.Solve)
	TestEach(t, "105", "problems", problem105.Solve)
	TestEach(t, "42", "problems", problem42.Solve)
}
