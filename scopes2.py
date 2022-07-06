 
from tkinter import X


def print_list(some_list):
    for element in some_list:
        print(element)

element = 'q'
print(element)
print_list([1,2,3,4,5])
print(element)


a = 10 #global
print #built-in
def hello(): #global
    a = "Hello world" #local
    print(a, 'local inside at func')


hello()
print(a, 'global')

x = 'global'
print(x)

def enclosed():
    x = 'enclosed'
    def local():
        x = 'local'
        print(x) 
print(X)
local()
print(X)

enclosed()
print(x)