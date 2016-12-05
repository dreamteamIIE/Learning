#include <iostream>
using namespace std;


//const仅限于当前文件, 必须初始化, 预处理时替换掉
const int bufsize = 1024;

//文件间共享
extern const int bufsize2 = 1024; //定义
//其他文件要引用这个变量, 也需要加上extern进行声明extern const int bufsize2;

int main()
{
	double a = 3.44;
	const double *p = &a;
	double *const p1 = &a;
	*p = 100;
	return 0;
}
