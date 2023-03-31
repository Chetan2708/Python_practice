
#include <iostream>

using namespace std;
void fun(int n)

{
    if (n == 0)
    {
        return ;
    }  
    cout << n << endl;
    fun(n - 1);
  
}
void wao(int n)

{
    if (n == 0)
    {
        return ;
    }    wao(n - 1);
    cout << n << endl;
  
  
}
int main()

{

    int n;
    cin >> n;
    fun(n);
    wao(n);

    return 0;
}
