from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[0, 1], [1, 2]], '010', '100'], Output=[0]))
		self.testcases.append(case(Input=[7, [[0, 1], [1, 2], [2, 3], [3, 4], [3, 5], [1, 6]], '0011000', '0010001'], Output=[1, 2, 5]))
		self.testcases.append(case(Input=[2, [[0, 1]], '00', '01'], Output=[-1]))

	def get_testcases(self):
		return self.testcases
