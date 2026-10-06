//go:build ignore
#include <queue>

#include "cpp/common/Solution.h"
#include "cpp/models/NodeNeighbors.h"

using namespace std;
using json = nlohmann::json;

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
  Node *cloneGraph(Node *node) {
    if (node == nullptr) {
      return node;
    }

    unordered_map<Node *, Node *> visited;

    // Add the given node to the queue
    queue<Node *> Q;
    Q.push(node);
    // Clone the first node and store it in the hash table
    visited[node] = new Node(node->val);

    // Breadth-first search
    while (!Q.empty()) {
      // Remove the node at the front of the queue
      auto n = Q.front();
      Q.pop();
      // Traverse this node's neighbors
      for (auto &neighbor : n->neighbors) {
        if (visited.find(neighbor) == visited.end()) {
          // If unvisited, clone it and store it in the hash table
          visited[neighbor] = new Node(neighbor->val);
          // Add the neighboring node to the queue
          Q.push(neighbor);
        }
        // Update the current node's neighbor list
        visited[n]->neighbors.emplace_back(visited[neighbor]);
      }
    }

    return visited[node];
  }
};

json leetcode::qubh::Solve(string input_json_values) {
  vector<string> inputArray;
  size_t pos = input_json_values.find('\n');
  while (pos != string::npos) {
    inputArray.push_back(input_json_values.substr(0, pos));
    input_json_values = input_json_values.substr(pos + 1);
    pos = input_json_values.find('\n');
  }
  inputArray.push_back(input_json_values);

  Solution solution;
  vector<vector<int>> node_arrays = json::parse(inputArray.at(0));
  Node *node = JsonArrayToNodeNeighbors(node_arrays);
  Node *res_ptr = solution.cloneGraph(node);
  json final_ans = NodeNeighborsToJsonArray(res_ptr);
  DeleteGraph(node);    // Delete the graph to prevent memory leak
  DeleteGraph(res_ptr); // Delete the graph to prevent memory leak
  return final_ans;
}
