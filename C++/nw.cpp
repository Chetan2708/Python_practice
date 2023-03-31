#include <iostream>
using namespace std;
class BaseClass{
   public:
      virtual void display(int y) {
         cout << "Displaying from Base Class\n";
      }
};
class DerivedClass : public BaseClass{
   public:
      void display(int x) override{
         cout << "Displaying from Derived Class\n";
      }
};
main() {
   BaseClass *b_ptr;
   b_ptr = new DerivedClass();
   b_ptr->display(5);
}