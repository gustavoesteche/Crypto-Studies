#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <boost/multiprecision/cpp_int.hpp>

namespace mp = boost::multiprecision;

using namespace std;

template <typename T>
T modpow(T base, T exp, T modulus) {
  base %= modulus;
  T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}


int random_number(int min, int max) {
    random_device rd;
    uniform_int_distribution<int> dist(min, max);
    return dist(rd);
}

int fermats_test(int p, int s) {
    int ola;
    cin >> ola;
    for (int i = 0; i < s; ++i){
        int x = (int)(modpow(random_number(2,p-2),p-1,p));
        if (x != 1) {
            return 0; // certainly false
        }
    }
    return 1; // probably true
}

int nextPrime(int n) {
    if (n <= 1) return 2;
    if (n == 2) return 3;
    int prime = n;
    bool found = false;
    while (!found) {
        prime += 2;        
        if (fermats_test(prime, (int)(0.2*prime))) {
            found = true;
        }
    }
    return prime;
}

int remove_small_factors(long int a, int num_fact){
    int q = 2;
    for(int i=0;i<num_fact;i++){
        while(a % q == 0){
            a /= q;
        }
        q = nextPrime(q);
    }
    return a;
}

long int gcd(long int a, long int b) {
    while (b != 0) {
        long int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

long int gcd_attack(int gamma, int eta, int rho, vector<long int> list_samples, int n){
    long int x = list_samples[0];

    mp::cpp_int mult_p = 1;
    long int limite_r = pow(2,rho);
    long int limite_total = pow(2,gamma) -1;
    long int ai;
    for(long int r = -limite_r;r <= limite_r;r++){ 
        mult_p = mult_p *(x - r);
        mult_p %= limite_total;
    }

    //mult_p = remove_small_factors(mult_p, 1000);
    //cout << mult_p << endl;
    
    for(int xi= 1; xi<n;xi ++){
        mp::cpp_int mi = 1;
        for(long int r = - limite_r;r <= limite_r;r++){
            mi *=  list_samples[xi] - r;        
            mi %= limite_total;
        }
        cout << mi << endl;
        mult_p = gcd(mult_p, mi);
        if(pow(2,eta) >= (long int)mult_p && (long int)mult_p >= pow(2,eta-1)){
            break;
        }
    }
    return (long int)mult_p;   
}


int main(){
    vector<long int> v = {618, 90178660, 25165034, 222298938,116392301, 135267368, 358615007, 36699982, 
                    376442052, 69206973, 556, 190842532, 419433191, 503319187, 415238963};
    cout << gcd_attack(30,20,10, v, 15) << endl;
} 