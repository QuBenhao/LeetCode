package golang

import (
	problem3683 "leetCode/problems/problems_3683"
	problem3684 "leetCode/problems/problems_3684"
	problem3685 "leetCode/problems/problems_3685"
	problem3686 "leetCode/problems/problems_3686"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3683", "problems", problem3683.Solve)
	TestEach(t, "3684", "problems", problem3684.Solve)
	TestEach(t, "3685", "problems", problem3685.Solve)
	TestEach(t, "3686", "problems", problem3686.Solve)
}
