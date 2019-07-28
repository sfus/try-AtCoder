#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string words[] = {"dream", "dreamer", "erase", "eraser"};
int nWords = sizeof(words) / sizeof(words[0]);

int main() {
    string S; cin >> S;
    reverse(S.begin(), S.end());
    for (int i = 0; i < nWords; ++i) {
        reverse(words[i].begin(), words[i].end());
    }

    for (int i = 0, max = S.size(); i < max; ) {
        bool found = false;
        for (int j = 0; j < nWords; ++j) {
            string word = words[j];
            if (S.substr(i, word.size()) == word) {
                i += word.size();
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
}
