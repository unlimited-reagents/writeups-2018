#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("card.txt", "r", stdin);
  while(1) {
    string r;
    cin >> r;
    int check = r.back() - '0';

    int ans = 0;
    string s(r.begin(), r.begin() + r.size() - 1);
    reverse(s.begin(), s.end());

    for (int i = 0; i < s.size(); i++) {
      int x = s[i] - '0';
      if (i % 2 == 0)
        x *= 2;

      if (x > 9) x -= 9;
      ans += x;
    }

    if ((ans + check) % 10){
      cout << r << "\n";
      exit(0);
    }
  }
}


