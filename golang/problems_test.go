package golang

import (
	problem3674 "leetCode/problems/problems_3674"
	problem3675 "leetCode/problems/problems_3675"
	problem3676 "leetCode/problems/problems_3676"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3674", "problems", problem3674.Solve)
	TestEach(t, "3675", "problems", problem3675.Solve)
	TestEach(t, "3676", "problems", problem3676.Solve)
}
