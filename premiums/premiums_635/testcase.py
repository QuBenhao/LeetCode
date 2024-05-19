from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['LogSystem', 'put', 'put', 'put', 'retrieve', 'retrieve'], [[], [1, '2017:01:01:23:59:59'], [2, '2017:01:01:22:59:59'], [3, '2016:01:01:00:00:00'], ['2016:01:01:01:01:01', '2017:01:01:23:00:00', 'Year'], ['2016:01:01:01:01:01', '2017:01:01:23:00:00', 'Hour']]], Output=[None, None, None, None, [3, 2, 1], [2, 1]]))

	def get_testcases(self):
		return self.testcases
