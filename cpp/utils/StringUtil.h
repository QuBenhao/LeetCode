#include <string>
#include <vector>

using namespace std;

vector<string> Split(string& s, const string& delim) {
    vector<string> res;
    int pos = s.find(delim);
    while (pos != string::npos) {
        res.push_back(s.substr(0, pos));
        s = s.substr(pos + delim.size());
        pos = s.find(delim);
    }
    res.push_back(s);
    return res;
}