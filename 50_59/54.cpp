#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <utility>

using namespace std;

int cnt = 0;
string cards[2][5];
int ranks[2];

int char2int(char c) {
	if (c >= '2' && c <= '9') return c-'2';
	if (c == 'T') return 8;
	if (c == 'J') return 9;
	if (c == 'Q') return 10;
	if (c == 'K') return 11;
	if (c == 'A') return 12;
}

int main(void) {
	ifstream input("p054_poker.txt");
	for (int c = 0; c < 1000; c++) {
		cout << "Game #" << c << endl;
		pair<int, int> cntCards[2][13];
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 13; j++)
				cntCards[i][j].second = j;
			for (int j = 0; j < 5; j++) {
				input >> cards[i][j];
				char cardnum = cards[i][j][0];
				cntCards[i][char2int(cardnum)].first++;
			}
			sort(cntCards[i], cntCards[i]+13);

			for (int j = 0; j < 5; j++) 
				cout << cards[i][j] << ' ';
			cout << endl;

			for (int j = 0; j < 13; j++)
				cout << cntCards[i][j].first << ':' << cntCards[i][j].second << ' ';
			cout << endl;

			bool samesuit = true;
			for (int j = 1; j < 5; j++) {
				if (cards[i][j][1] != cards[i][0][1]) {
					samesuit = false;
					break;
				}
			}
			
			
			ranks[i] = 1;
			
			bool isStr = true;
			for (int j = 1; j < 5; j++)
				if (cntCards[i][8+j].second != (cntCards[i][8].second+j)%13) {
					isStr = false;
					break;
				}

			if (samesuit) {
				ranks[i] = 6;
				if (isStr) {
					if (cntCards[i][8].second == 8) ranks[i] = 10;
					else ranks[i] = 9;
				}
			}
			else if (cntCards[i][12].first == 4) 
				ranks[i] = 8;
			else if (cntCards[i][12].first == 3) {
				if (cntCards[i][11].first == 2)
					ranks[i] = 7;
				else ranks[i] = 4;
			}
			else if (cntCards[i][12].first == 2) {
				if (cntCards[i][11].first == 2) ranks[i] = 3;
				else ranks[i] = 2;
			}
			else {
				if (isStr) ranks[i] = 5;
				else ranks[i] = 1;
			}
		}

		cout << endl << ranks[0] << ' ' << ranks[1] << endl;

		if (ranks[0] > ranks[1]) cnt++;
		else if (ranks[0] < ranks[1]) continue;
		else {
			for (int i = 12; i >= 0; i--) {
				if (cntCards[0][i].second > cntCards[1][i].second) {
					cnt++; break;
				}
				else if (cntCards[0][i].second < cntCards[1][i].second) break;
			}
		}
	}

	cout << cnt << endl;
	return 0;
}
