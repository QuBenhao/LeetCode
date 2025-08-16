//
// Created by BenHao on 2024/5/21.
//
#include <fstream>
#include <iostream>
#include <memory>
#include <sstream>
#include <utility>
#include <vector>

#include "TestMain.h"
#include "cpp/common/Solution.h"
#ifndef BUILD_CMAKE
#include "tools/cpp/runfiles/runfiles.h"
#else
#include <cstdlib> // 用于 getenv
#endif

using std::cerr;
using std::cout;
using std::endl;
using std::ifstream;
using std::runtime_error;
using std::size_t;
using std::string;
using std::stringstream;
using std::vector;
using json = nlohmann::json;
#ifndef BUILD_CMAKE
using bazel::tools::cpp::runfiles::Runfiles;
#endif

namespace LeetCode {
namespace qubh {

vector<TestCase> LoadTestCases(const string &path) {
#ifndef BUILD_CMAKE
  string error;
  unique_ptr<Runfiles> runfiles(
      Runfiles::Create("LeetCode Solution Test", &error));

  if (runfiles == nullptr) {
    // error handling
    throw runtime_error("Could not open file: " + error);
  }

  string filePath = runfiles->Rlocation(path);
#else
  string filePath = path;
#endif
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
    cout << "Input: " << data_.GetInput() << endl;
    cout << "Expected: " << data_.GetExpected() << endl;
    auto output = leetcode::qubh::Solve(data_.GetInput());
    while (!isEqual && retries < maxRetries) {
      if (data_.GetExpected().is_number_float()) {
        isEqual = std::abs(output.get<double>() -
                           data_.GetExpected().get<double>()) < 1e-5;
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
      ASSERT_LE(std::abs(output.get<double>() - data_.GetExpected().get<double>()), 1e-5);
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
  if (values.empty()) {
    FAIL() << "Empty testcases!";
  }
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
        // 检查是否提供了测试用例路径
        string testcasePath;
        if (argc >= 2) {
            testcasePath = argv[1];
        } else {
            // 尝试从环境变量获取路径
            const char* env_path = std::getenv("TESTCASE_FILE");
            if (env_path) {
                testcasePath = env_path;
            } else {
                cerr << "Error: Testcase path not provided and TESTCASE_FILE environment variable not set." << endl;
                cerr << "Usage: " << argv[0] << " <testcase_path>" << endl;
                return 1;
            }
        }

        cout << "Loading testcases from: " << testcasePath << endl;

        // 加载测试用例
        vector<LeetCode::qubh::TestCase> testcases =
                LeetCode::qubh::LoadTestCases(testcasePath);

        // 初始化并运行测试
        testing::InitGoogleTest(&argc, argv);
        LeetCode::qubh::RegisterMyTests(testcases);
        return RUN_ALL_TESTS();
    } catch (const std::exception &e) {
        cerr << "Error: " << e.what() << endl;
        return 1;
    }
}