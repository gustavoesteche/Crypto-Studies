#include <iostream>
#include <random>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int random_number(int min, int max) {
    std::random_device rd;
    std::uniform_int_distribution<int> dist(min, max);
    return dist(rd);
}

int sample_r(int rho) {
    return random_number(-std::pow(2, rho), std::pow(2, rho));
}

int sample_q(int gamma, int eta) {
    return random_number(0, std::pow(2, gamma - eta));
}

int sample_agcd(int gamma, int rho, int p) {
    int eta = (int)std::log2(p);
    int q = sample_q(gamma, eta);
    int r = sample_r(rho);
    return p * q + r;
}
