from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
    def __init__(self):
        self.testcases = []
        self.testcases.append(case(
            Input=[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
                   ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]],
            Output=[["Table", "Beef Burrito", "Ceviche", "Fried Chicken", "Water"], ["3", "0", "2", "1", "0"],
                    ["5", "0", "1", "0", "1"], ["10", "1", "0", "0", "0"]]))
        self.testcases.append(case(Input=[["James", "12", "Fried Chicken"], ["Ratesh", "12", "Fried Chicken"],
                                          ["Amadeus", "12", "Fried Chicken"], ["Adam", "1", "Canadian Waffles"],
                                          ["Brianna", "1", "Canadian Waffles"]],
                                   Output=[["Table", "Canadian Waffles", "Fried Chicken"], ["1", "2", "0"],
                                           ["12", "0", "3"]]))
        self.testcases.append(
            case(Input=[["Laura", "2", "Bean Burrito"], ["Jhon", "2", "Beef Burrito"], ["Melissa", "2", "Soda"]],
                 Output=[["Table", "Bean Burrito", "Beef Burrito", "Soda"], ["2", "1", "1", "1"]]))

    def get_testcases(self):
        return self.testcases
