package golang

import (
	"leetCode/problems/problems_Interview_02__03"
	"leetCode/problems/problems_Interview_17__04"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "Interview_02__03", "problems", problemInterview_02__03.Solve)
	TestEach(t, "Interview_17__04", "problems", problemInterview_17__04.Solve)
}
