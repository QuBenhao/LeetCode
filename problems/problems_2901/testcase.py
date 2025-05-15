from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['bab', 'dab', 'cab'], [1, 2, 2]], Output=['bab', 'cab']))
		self.testcases.append(case(Input=[['a', 'b', 'c', 'd'], [1, 2, 3, 4]], Output=['a', 'b', 'c', 'd']))
		self.testcases.append(case(Input=[["dee","bb"],[2,1]], Output=["bb"]))
		self.testcases.append(case(Input=[["aab","ca","cbd"],[3,3,2]], Output=["cbd"]))
		self.testcases.append(case(Input=[["cbb","db","bdd","bd"],[2,3,4,3]], Output=["bd"]))

	def get_testcases(self):
		return self.testcases
