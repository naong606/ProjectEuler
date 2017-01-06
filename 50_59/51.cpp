#include <iostream>
#include <vector>
#include <cstring>
#include <cmath>
#define MAX 1000000

using namespace std;

bool isPrime[MAX];
inline int min(int a, int b) {return a<b?a:b;}
inline int pow10(int n) {return n==0?1:(10*pow10(n-1));}

int main(void) {
	memset(isPrime, true, sizeof(isPrime));
	isPrime[0] = isPrime[1] = false;
	for (int i = 2; i*i <= MAX; i++) {
		if (isPrime[i])
			for (int j = 2*i; j <= MAX; j += i)
				isPrime[j] = false;
	}

	int ans = 1987654321;
	for (int numdigit = 4; numdigit <= 6; numdigit++) {
		int astr[3] = {0, 1, 2};

		bool end = false;
		bool astrFront = false;
		while (!end) {
			vector<int> digitpos;
			int offset = 0;

			for (int i = 0; i < 3; i++)
				offset += pow10(astr[i]);
			for (int i = 0, pastr = 0; i < numdigit; i++) {
				if (pastr < 3 && astr[pastr] == i)
					pastr++;
				else
					digitpos.push_back(i);
			}

			int iterFrom = astrFront ? 0 : pow10(numdigit-4);
			int iterTo = pow10(numdigit-3);
			for (int i = iterFrom; i < iterTo; i++) {
				int ibuf = i;
				int n = 0, p = 0;
				while (ibuf) {
					n += pow10(digitpos[p++])*(ibuf%10);
					ibuf /= 10;
				}

				int cnt = 0, cand = -1;
				n += (astrFront ? offset : 0);
				for (int j = (astrFront ? 1 : 0); j < 10; j++) {
					if (isPrime[n]) {
						cnt++;
						if (cand == -1) cand = n;
						if (cand == 121313)
							cout << n << endl;
					}
					n += offset;
				}
				if (cnt == 8)
					ans = min(ans, cand);
			}

			end = true;
			for (int i = 2; i >= 0; i--)
				if (astr[i] != numdigit-3+i) {
					astr[i]++;
					for (int j = i+1; j < 3; j++)
						astr[j] = astr[i] + (j-i);
					end = false;
					astrFront = astr[2] == numdigit-1;
					break;
				}
		}
	}
	cout << ans << endl;
	return 0;
}
