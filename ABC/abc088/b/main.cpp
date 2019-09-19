#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int N; cin >> N;
    int a[N];
    for (int i = 0; i < N; ++i)
        cin >> a[i];

    sort(a, a + N, greater<int>());

    int Alice, Bob = 0;
    for (int i = 0; i < N; ++i) {
        if (i % 2 == 0) {
            Alice += a[i];
        } else {
            Bob += a[i];
        }
    }
    int result = Alice - Bob;
    cout << result << endl;
}
