#include <iostream>
#include <string>
using namespace std;

int main() {
    int number;
    cin >> number;
    int inputs[number];

    for (int i = 0; i < number; ++i) {
        cin >> inputs[i];
    }

    int result = 0;
    while (true) {
        for (int i = 0; i < number; ++i) {
            bool odd = inputs[i] % 2 != 0;
            if (odd) {
                goto loopend;
            }
            inputs[i] = inputs[i] / 2;
        }
        ++result;
    }
    loopend:

    std::cout << result << endl;
}