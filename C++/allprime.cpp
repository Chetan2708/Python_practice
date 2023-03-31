#include<iostream>
#include<cmath>
using namespace std;

bool print( int n ){
    for (int i = 2; i < n; i++)
    {
        if (n%i==0)
        {
            return false;
        }
        
    }
    return true;

    
}
int main(){
int a , b;
cin>>a>>b;
for (int i = a; i <=b; i++)
 {
    if(  print(i) )
    {cout<<i<<endl;}   /* code */
}

return 0;



}