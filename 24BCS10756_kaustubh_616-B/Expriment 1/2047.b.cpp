#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin >> t;
    for(int test = 0; test < t; test++) {
        int n;
        string s;
        cin >> n >> s;
        
        map<char, int> freq;
        for(char c : s) {
            freq[c]++;
        }
        
        char maxc = s[0], minc = s[0];
        for(auto& p : freq) {
            if(p.second > freq[maxc]) maxc = p.first;
            if(p.second < freq[minc]) minc = p.first;
        }
        
        for(int i = 0; i < n; i++) {
            if(s[i] == minc) {
                s[i] = maxc;
                break;
            }
        }
        
        cout << s << '\n';
    }
    return 0;
}
