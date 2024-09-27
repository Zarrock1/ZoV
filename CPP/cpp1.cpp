#include <iostream>
#include <tuple>

using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

tuple<int, int, int> find_lcm(int a, int b) {
    int lcm = (a * b) / gcd(a, b);
    int c1 = lcm / a;
    int c2 = lcm / b;
    return {lcm, c1, c2};
}

tuple<int, int> reduce(int m, int n) {
    int g = gcd(m, n);
    m /= g;
    n /= g;
    if (n < 0) {
        m = -m;
        n = -n;
    }
    return {m, n};
}

int main() {
    int m1, n1, m2, n2;
    char _;

    std::cin >> m1 >> _ >> n1 >> m2 >> _ >> n2;

    std::tie(m1, n1) = reduce(m1, n1);
    std::tie(m2, n2) = reduce(m2, n2);

    auto [lcm, c1, c2] = find_lcm(n1, n2);
    auto [m, n] = reduce(m1 * c1 + m2 * c2, lcm);

    std::cout << m << '/' << n << std::endl;
}
