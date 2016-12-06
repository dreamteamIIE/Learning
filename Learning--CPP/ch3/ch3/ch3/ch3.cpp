// ch3.cpp : 定义控制台应用程序的入口点。
//Ctrl+F5  debug

#include "stdafx.h"


#include <iostream>
#include <string>
#include <cctype>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::istream;

int main()
{
	vector<string> v;
	string i;
	//while (cin >> i)
	while (getline(cin, i))
	{
	//if (i == "\n") break;
	if (i.empty()) break; 
		v.push_back(i);
	}
	for(auto str:v){
	cout << str<< endl;}
	cout << v.size() << endl;
	//system("pause");
	return 0;
}

