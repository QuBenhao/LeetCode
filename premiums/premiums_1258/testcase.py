from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[['happy', 'joy'], ['sad', 'sorrow'], ['joy', 'cheerful']], 'I am happy today but was sad yesterday'], Output=['I am cheerful today but was sad yesterday', 'I am cheerful today but wassorrow yesterday', 'I am happy today but was sad yesterday', 'I am happy todaybut was sorrow yesterday', 'I am joy today but was sad yesterday', 'I am joytoday but was sorrow yesterday']))
		self.testcases.append(case(Input=[[['happy', 'joy'], ['cheerful', 'glad']], 'I am happy today but was sad yesterday'], Output=['I am happy today but was sad yesterday', 'I am joy today but was sadyesterday']))

	def get_testcases(self):
		return self.testcases
