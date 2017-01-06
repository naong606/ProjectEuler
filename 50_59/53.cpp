#include <iostream>
using namespace std;

int cnt = 0;
int comb[101][101];
int main(void) {
	for (int i = 0; i <= 100; i++)
		comb[i][0] = comb[i][i] = 1;

	for (int i = 2; i <= 100; i++) {
		for (int j = 1; j < i; j++) {
			comb[i][j] = comb[i-1][j-1] + comb[i-1][j];
			if (comb[i][j] > 1000000) {
				comb[i][j] = 1000001;
				cnt++;
			}
		}
	}
	cout << cnt << endl;
	return 0;
}
