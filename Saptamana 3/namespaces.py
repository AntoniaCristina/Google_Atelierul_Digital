def my_function():
    global msg
    msg = "Hello"
    # print(msg)
    return None #functiile returneaza by default none

my_function()
print(msg)
# print(my_function())