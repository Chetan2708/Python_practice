from webbrowser import get


class op:
    name = ""
    id_num = 0
    def get_details(self):
             self.name = input("Enter your name: ")
             self.id_num = int(input("Id : "))
        
    def print_details(self):
            print(f" name : {self.name}, id_num : {self.id_num}")
ob =[int(input("Enter your number of employees: "))]

for i in ob:
    ob[i] = op()
    