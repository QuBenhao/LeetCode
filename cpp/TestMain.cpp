//
// Created by 曲本豪 on 2024/5/21.
//

#include "TestMain.h"
#include <fstream>
#include <sstream>
#include <utility>
#include <memory>
#include <vector>
#include "cpp/common/Solution.h"
#include "tools/cpp/runfiles/runfiles.h"


using std::string;
using std::ifstream;
using std::stringstream;
using std::runtime_error;
using std::vector;
using std::size_t;
using std::endl;
using std::cerr;
using json = nlohmann::json;
using bazel::tools::cpp::runfiles::Runfiles;

namespace LeetCode {
namespace qubh {

vector<TestCase> LoadTestCases(const string &path) {
  string error;
  unique_ptr<Runfiles> runfiles(
      Runfiles::Create("LeetCode Solution Test", &error));

  if (runfiles == nullptr) {
    // error handling
    throw runtime_error("Could not open file: " + error);
  }

  string filePath = runfiles->Rlocation(path);
  ifstream fileStream(filePath);
  if (!fileStream) {
    throw runtime_error("Could not open file: " + filePath);
  }

  stringstream buffer;
  buffer << fileStream.rdbuf();

  string input = buffer.str();
  vector<string> splits;
  size_t pos = input.find('\n');
  while (pos != string::npos) {
    splits.push_back(input.substr(0, pos));
    input = input.substr(pos + 1);
    pos = input.find('\n');
  }
  splits.push_back(input);
  if (splits.size() != 2) {
    throw runtime_error("Invalid test case format");
  }
  vector<string> inputs = json::parse(splits[0]);
  vector<json> outputs = json::parse(splits[1]);
  vector<TestCase> testCases;
  for (size_t i = 0; i < inputs.size(); i++) {
    testCases.push_back(TestCase(inputs[i], outputs[i]));
  }
  return testCases;
}

class LeetCodeSuiteSet : public testing::Test {
 public:
  // All of these optional, just like in regular macro usage.
  static void SetUpTestSuite() {}

  static void TearDownTestSuite() {}

  void SetUp() {}

  void TearDown() {}
};

class LeetCodeTest : public LeetCodeSuiteSet {
 public:
  explicit LeetCodeTest(TestCase data) : data_(std::move(data)) {}

  void TestBody() override {
        bool isEqual = false;
        int retries = 0;
        const int maxRetries = 1e5;  // Set the maximum number of retries
        auto output = leetcode::qubh::Solve(data_.GetInput());
        while (!isEqual && retries < maxRetries) {
            if (data_.GetExpected().is_number_float()) {
                isEqual = std::abs(output.get<double>() - data_.GetExpected().get<double>()) < 1e-6;
            } else if (output.is_array() && !data_.GetExpected().is_array()) {
                isEqual = (output[0] == data_.GetExpected());
            } else {
                isEqual = (output == data_.GetExpected());
            }

            if (!isEqual) {
                auto secondOutput = leetcode::qubh::Solve(data_.GetInput());
                if (retries == 0 && secondOutput == output) {
                    break;
                }
                output = secondOutput;
                retries++;
            }
        }

        if (data_.GetExpected().is_number_float()) {
            ASSERT_DOUBLE_EQ(output.get<double>(), data_.GetExpected().get<double>());
        } else {
            if (output.is_array() && !data_.GetExpected().is_array()) {
                ASSERT_EQ(output[0], data_.GetExpected());
            } else {
                ASSERT_EQ(output, data_.GetExpected());
            }
        }
  }

 private:
  TestCase data_;
};

void RegisterMyTests(const vector<TestCase> &values) {
  for (size_t i = 0; i < values.size(); i++) {
    testing::RegisterTest(
        "LeetCode Solution Test", ("Testcase" + to_string(i)).c_str(), nullptr,
        "LeetCode::qubh::Testcase", __FILE__, __LINE__,
        // Important to use the fixture type as the return type here.
        [=]() -> LeetCodeSuiteSet * { return new LeetCodeTest(values[i]); });
  }
}
}  // namespace qubh
}  // namespace LeetCode

int main(int argc, char **argv) {
  try {
    // Run the tests.
    vector<LeetCode::qubh::TestCase> testcases =
        LeetCode::qubh::LoadTestCases(argv[1]);
    testing::InitGoogleTest(&argc, argv);
    LeetCode::qubh::RegisterMyTests(testcases);
    return RUN_ALL_TESTS();
  } catch (const exception &e) {
    cerr << e.what() << endl;
    return 1;
  }
}