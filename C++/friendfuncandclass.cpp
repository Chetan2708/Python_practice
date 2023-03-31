// #include<iostream>
// using namespace std;

// class A
// {
// private:
//     int x;
// public:
//  A(): x(5) {}
//  friend class B;
// };

// class B{
//     int y;
//     public:
//     B(): y(10) {}
//     int add (A a)
//    {
//         return a.x + y;
//     }
// };
// int main()
// {
//     B obj;
//     A  a1;
//   cout<< obj.add(a1);
//     return 0;
// }












#include<iostream>
using namespace std;
class B;
class A
{
private:
    int x;
    friend int add(A a , B b);
public:
    A():x(10){};
};
class B{
    int y;
    friend int add(A a , B b);
    public:
    B():y(14){};

};
int add(A a ,   B b){

    return (a.x+b.y);
}
int main()
{
    A a1;
    B b1;
   cout<< add(a1,b1);
   return 0;
}       x