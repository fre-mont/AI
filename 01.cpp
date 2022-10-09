/*
1. Caesar cipher
- integer number as a key
- string as a plain text => length of  the input string must be 8
- reference : https://en.wikipedia.org/wiki/Caesar_cipher
*/

#include <iostream>
#include <string>
using namespace std;

int main(){

    int num;
    string text;

    cout << "Input string: ";
    cin >> text;

    cout << "Input key: ";
    cin >> num;

    text[0] += num;
    text[1] += num;
    text[2] += num;
    text[3] += num;
    text[4] += num;
    text[5] += num;
    text[6] += num;
    text[7] += num;

    cout << "Cipher string: " << text;
    return 0;
    
}