#include<iostream>
using namespace std;


class A{
int num;
public:
A(int x){
    num = x;
}
friend void operator ++(A &c);
friend void operator ++(A &t , int not_used);
void display(){
    cout << "num: " << num << endl;}
};
void operator++(A &c) {
    ++c.num;
}
void operator++(A &t , int not_used) {
    t.num++;
    }
 

int main()
{  A obj(5);
obj.display();
  ++obj;
    obj.display();
    obj++;
    obj.display();
    return 0;
}