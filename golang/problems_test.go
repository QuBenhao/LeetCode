package golang

import (
	problem3622 "leetCode/problems/problems_3622"
	problem3623 "leetCode/problems/problems_3623"
	problem3624 "leetCode/problems/problems_3624"
	problem3625 "leetCode/problems/problems_3625"
	"testing"
)

func TestSolutions(t *testing.T) {
	TestEach(t, "3622", "problems", problem3622.Solve)
	TestEach(t, "3623", "problems", problem3623.Solve)
	TestEach(t, "3624", "problems", problem3624.Solve)
	TestEach(t, "3625", "problems", problem3625.Solve)
}
