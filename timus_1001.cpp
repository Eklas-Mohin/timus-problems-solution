#include <bits/stdc++.h>
using namespace std;

int main() {
    long double x;
    stack<long double> st;

    while (cin >> x) {
        st.push(sqrt(x));
    }

    while (!st.empty()) {
        long double k = st.top();
        cout << fixed << setprecision(4) << k << endl;
        st.pop();
    }

    return 0;
}
