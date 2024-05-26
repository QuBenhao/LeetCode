//
// Created by 曲本豪 on 2024/5/21.
//

#include <fstream>
#include <sstream>
#include "TestMain.h"
#include "cpp/common/Solution.h"
#include "tools/cpp/runfiles/runfiles.h"

using namespace std;
using json = nlohmann::json;
using bazel::tools::cpp::runfiles::Runfiles;

namespace LeetCode
{
    namespace qubh
    {

        vector<TestCase> LoadTestCases(const string &path)
        {
            string error;
            unique_ptr<Runfiles> runfiles(Runfiles::Create("LeetCode Solution Test", &error));

            if (runfiles == nullptr)
            {
                // error handling
                throw runtime_error("Could not open file: " + error);
            }

            string filePath = runfiles->Rlocation(path);
            ifstream fileStream(filePath);
            if (!fileStream)
            {
                throw runtime_error("Could not open file: " + filePath);
            }

            stringstream buffer;
            buffer << fileStream.rdbuf();

            string input = buffer.str();
            vector<string> splits;
            int pos = input.find("\n");
            while (pos != string::npos)
            {
                splits.push_back(input.substr(0, pos));
                input = input.substr(pos + 1);
                pos = input.find("\n");
            }
            splits.push_back(input);
            if (splits.size() != 2)
            {
                throw runtime_error("Invalid test case format");
            }
            vector<string> inputs = json::parse(splits[0]);
            vector<json> outputs = json::parse(splits[1]);
            vector<TestCase> testCases;
            for (int i = 0; i < inputs.size(); i++)
            {
                testCases.push_back(TestCase(inputs[i], outputs[i]));
            }
            return testCases;
        }

        class LeetCodeSuiteSet : public testing::Test
        {
        public:
            // All of these optional, just like in regular macro usage.
            static void SetUpTestSuite() {}
            static void TearDownTestSuite() {}
            void SetUp() override {}
            void TearDown() override {}
        };

        class LeetCodeTest : public LeetCodeSuiteSet
        {
        public:
            explicit LeetCodeTest(TestCase data) : data_(data) {}
            void TestBody() override
            {
                ASSERT_EQ(leetcode::qubh::Solve(data_.GetInput()), data_.GetExpected());
            }

        private:
            TestCase data_;
        };

        void RegisterMyTests(const vector<TestCase> &values)
        {
            for (int i = 0; i < values.size(); i++)
            {
                testing::RegisterTest(
                    "LeetCode Solution Test", ("Testcase" + to_string(i)).c_str(), nullptr,
                    "LeetCode::qubh::Testcase",
                    __FILE__, __LINE__,
                    // Important to use the fixture type as the return type here.
                    [=]() -> LeetCodeSuiteSet *
                    { return new LeetCodeTest(values[i]); });
            }
        }
    } // qubh
} // LeetCode

int main(int argc, char **argv)
{
    try
    {
        // Run the tests.
        vector<LeetCode::qubh::TestCase> testcases = LeetCode::qubh::LoadTestCases(argv[1]);
        testing::InitGoogleTest(&argc, argv);
        LeetCode::qubh::RegisterMyTests(testcases);
        return RUN_ALL_TESTS();
    }
    catch (const exception &e)
    {
        cerr << e.what() << endl;
        return 1;
    }
}