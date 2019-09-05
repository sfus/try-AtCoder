#include <iostream>
#include <string>
using namespace std;

int main() {
    string s, t;
    cin >> t >> s;

    int count = 0;
    for (int i = 0; i < 3; ++i) {
        if (s[i] == t[i]) {
            ++count;
        }
    }
    cout << count;
}
