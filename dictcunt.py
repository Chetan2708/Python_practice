# d =[11, 45, 8, 11, 23, 45, 23, 45, 89, 11, 89]

# dict={}
# for i in d:
#     if i in dict:
#         dict[i] +=1
#     else:
#         dict[i] = 1
# print(dict)



# dict = {0:1, "avas": 2}
# dict[0]=4
# print(dict)

def dictionairy():
    # Declare hash function
    key_value = {}
 
# Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
 
    print("Task 1:-\n")
 
    print("key_value", key_value)
 
    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i,n in sorted(key_value.items()):
                txt = "{}:{}"
                print(txt.format(i,n ) )
 
 
def main():
    # function calling
    dictionairy()
 
 
# Main function calling
if __name__ == "__main__":
    main()
