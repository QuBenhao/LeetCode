//
// Created by BenHao on 2024/5/21.
//

#ifndef LEETCODECPP_TESTMAIN_H
#define LEETCODECPP_TESTMAIN_H

#include <string>
#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

namespace LeetCode
{
    namespace qubh
    {

        class TestCase
        {
        public:
            TestCase(string input, json expected) : Input(std::move(input)), Expected(std::move(expected)) {}

            string GetInput() const
            {
                return Input;
            }

            json GetExpected() const
            {
                return Expected;
            }
        private:
            string Input;
            json Expected;
        };

    } // qubh
} // LeetCode

#endif // LEETCODECPP_TESTMAIN_H
