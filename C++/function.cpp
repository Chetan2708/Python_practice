#include<iostream>
using namespace std;
int swap(int &x,int &y); // function declare

int main()
{ 
    int a,b;
  cout<<"Enter two numbers you want to swap";
   cin>> a  >> b;

swap(a, b);
cout<<"Swapped"  << " " ;
cout << a << " " << b << endl;

  return 0 ;
}
int swap(int &x , int &y ) //  function define
{ int z;
return ( 
  z =x, 
x= y, 
y = z);
}