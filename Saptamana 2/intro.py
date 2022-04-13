#print("Mesaj")

# while True:
#         print("Da")
#         break

# for i in range(10):
#         print(f'Set instructiuni [{i + 1}]')

# for i in range(5):
#         if i == 3:
#                 continue
#         print(i)
#
def my_function(param_1, param_2, *args, **kwargs):
        print(param_1)
        print(param_2)
        print(args)
        print(kwargs)

my_function(2, 5, d=22, c=7, a=2, b=-3)
