package golang

import (
	"leetCode/problems/problems_Interview_02__01"
	"leetCode/problems/problems_Interview_10__01"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "Interview_02__01", "problems", problemInterview_02__01.Solve)
	TestEach(t, "Interview_10__01", "problems", problemInterview_10__01.Solve)
}
