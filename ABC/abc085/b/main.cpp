#include <iostream>
using namespace std;

// use array bucket
int main() {
    const int MAX = 100;
    int bucket[MAX + 1] = {}; // for max bucket[100]

    int N; cin >> N;
    for (int i = 0; i < N; ++i) {
        int digit;
        cin >> digit;
        bucket[digit] = 1; // 1 <= digit <= 100
    }

    int ret = 0;
    for (int i = 1; i <= MAX; ++i) { // bucket[0] is not used.
        if (bucket[i] == 1) ++ret;
    }

    cout << ret << endl;
    return 0;
}
