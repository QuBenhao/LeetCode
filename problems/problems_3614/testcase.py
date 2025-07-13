from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['a#b%*', 1], Output="a"))
		self.testcases.append(case(Input=['cd%#*#', 3], Output="d"))
		self.testcases.append(case(Input=['z*#', 0], Output="."))
		self.testcases.append(case(Input=["%edx#n#lkc####uom##qg#%#b#ek%##%%ocr#m%#fv%i%%#n#u%%#n#q%v#rwvd##t###%#%%%o*##r#gr*gz#dm%ez",4780], Output="d"))
		self.testcases.append(case(Input=["*##h#py",3], Output="y"))

	def get_testcases(self):
		return self.testcases
