from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['avokado', 'dabar'], ['brazil']], Output=False))
		self.testcases.append(case(Input=[['ananas', 'atlas', 'banana'], ['albatros', 'cikla', 'nogomet']], Output=True))
		self.testcases.append(case(Input=[['hrvatska', 'zastava'], ['bijeli', 'galeb']], Output=True))

	def get_testcases(self):
		return self.testcases
