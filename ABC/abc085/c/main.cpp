#include <iostream>
using namespace std;

int main() {
    int N; cin >> N; // num of bills
    int Y; cin >> Y; // bills sum (yen)

    for (int n10k = 0; n10k <= N; ++n10k) {
        int rest5k1k = N - n10k;
        for (int n5k = 0; n5k <= rest5k1k; ++n5k) {
            int n1k = N - n10k - n5k;
            if (Y == 10000 * n10k + 5000 * n5k + 1000 * n1k) {
                cout << n10k << " " << n5k << " " << n1k << endl;
                return 0;
            }
        }
    }
    cout << "-1 -1 -1" << endl;
    return 0;
}
