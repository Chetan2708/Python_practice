#include <iostream> 
using namespace std; 
class A { 
public: 
    int number; 
    
    A() // constructor 
    { 
         number = 10; 
    } 
};  
class B : public virtual A {};  
class C : public virtual A {};  
class D : public B, public C{}; 
int main() 
{ 
    D object; // object is created for class d 
    cout << "number = " << object.number << endl; 
    return 0; 
}