#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sstream>
#include<windows.h>,
#include <conio.h>
#include <cstdlib>
#include "Windows.h"
#include "winuser.h"
#include <cmath>
#include <iostream>
#include <iomanip>
#include <complex>
#include <string>


void toClipboard(HWND hwnd, const std::string &s){
	OpenClipboard(hwnd);
	EmptyClipboard();
	HGLOBAL hg=GlobalAlloc(GMEM_MOVEABLE,s.size()+1);
	if (!hg){
		CloseClipboard();
		return;
	}
	memcpy(GlobalLock(hg),s.c_str(),s.size()+1);
	GlobalUnlock(hg);
	SetClipboardData(CF_TEXT,hg);
	CloseClipboard();
	GlobalFree(hg);
}


// AthenaApps - Open Source 

using namespace std;
int main(void)
{
	string clipboardItems = "", stringg;
	stringstream stringstream;
	cout <<"18-Word Phrase Generator for Cold Wallets by AthenApps" << endl << "Wait for 5 seconds.." << endl;
	sleep(5);
    FILE *fp = fopen("words.txt", "r");
    if (fp == NULL) {
        cout << endl << "Text File not found, don't forget to export 'words.txt' from .zip file!";
        system("PAUSE");
    }
    char word[100];
    long wc = 0;
    while (fgets(word, sizeof word, fp) != NULL) {
        ++wc;
    }
    char words[18][100];
    srand((unsigned) time(NULL));
    for (size_t i = 0; i < 18; i++) {
        rewind(fp);
        int sel = rand() % wc + 1;
        for (int j = 0; j < sel; j++) {
            if (fgets(word, sizeof word, fp) == NULL) {
                cout<<"Error in fgets()";
            }
        }
        strcpy(words[i], word);
    }
    if (fclose(fp) != 0) {
        cout << "ERROR !";
    }
    for (size_t i = 0; i < 18; i++) {
        cout << words[i];
        stringstream << words[i];
        stringstream >> stringg;
        clipboardItems += stringg + " ";
        if(i==17)
        	cout << endl << "--- Copied to the clipboard. Paste them on your wallet.";
    }
    HWND hwnd = GetDesktopWindow();
	toClipboard(hwnd, clipboardItems);
    cout << endl << "--- AthenaApps" << endl;
    system("PAUSE");
    // It already returns void.
}