#include <iostream>
#include <set>
using namespace std;

// use std::set
int main() {
    int N; cin >> N;
    set<int> values;
    for (int i = 0; i < N; ++i) {
        int digit;
        cin >> digit;
        values.insert(digit);
    }

    cout << values.size() << endl;
    return 0;
}
