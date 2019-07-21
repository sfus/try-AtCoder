#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    bool isEven = a * b % 2 == 0;
    cout << (isEven ? "Even" : "Odd") << endl;
}