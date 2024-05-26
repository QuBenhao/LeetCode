#pragma once
#include <string>
#include <nlohmann/json.hpp>

using json = nlohmann::json;
using namespace std;

namespace leetcode {
    namespace qubh {
        json Solve(string input);
    }
}