# my_list = ['Ursache', 'Parascuta','Misu']
# print (my_list[1])
# my_list.pop(0)
# list = my_list[1:]
# print(list)

# dict = {}
# i = 0
# for x in my_list:
#     dict[x] = i
#     i += 1

#palin = 'capac'
#print(palin[::] == palin[::-1])

# def func2(str):
#     j = len(str) - 1
#     for i in range(len(str)):
#         while str[i] != str[j]:
#             return False
#         j -= 1
#     return True

# def func(z):
#     i = 0
#     j = len(z) - 1
#     while (z[i] == z[j]):
#         i += 1
#         j -= 1
#         if (i == len(z) or j == 0):
#             return True
#     return False
# print(func(palin))
# print(func2(palin))

tester = 'abcdef'
for x in range(len(tester)):
    #print(x)   # 0, 1, 2, 3, 4
    #print("....,")
    pass
    #print(tester[x]) # a, b, c, d, e, f

for idx, item in enumerate(tester):
    #print(idx, item)
    pass

# def odd(z):
#     aux2 = str(z)
#     for x in range(len(aux2)):
#         if int(aux2[x])%2==0:
#             print('%s is even' % aux2[x])
#         else:
#             print('%s is odd' % aux2[x])       
# odd(aux)

aux = 15624
def count(z):
    aux2 = str(z)
    print(len(aux2))
    
count(aux)

def count2(z):
    c = 0 
    while z != 0:
        z = z // 10
        c += 1
    print(c) 

count2(aux)

class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name
    
        
class Employee(Person):
    def __init__(self, first_name, last_name, employer):
        super().__init__(first_name, last_name)
        self.employer = employer
    def show(self):
        print(f'I am {self.first} {self.last} and I work at {self.employer}.')
    
V = Employee('Vlad', 'Ursache', 'Vitesco')
V.show()