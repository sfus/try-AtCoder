#include <iostream>
#include <string>
using namespace std;

int sumCols(int val) {
    int sum = 0;
    int next = val;
    while (next > 0) {
        sum += next % 10;
        next /= 10;
    }
    return sum;
}

int main() {
    int N, A, B;
    cin >> N >> A >> B;
    int ret = 0;

    for (int i = 0; i <= N; i++) {
        int sum = sumCols(i);
        if (A <= sum && sum <= B) {
            ret += i;
        }
    }

    cout << ret << endl;
}
