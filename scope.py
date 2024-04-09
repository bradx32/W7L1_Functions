# scope - global and local

fname = "Pat" # Global scope
lname = "Cummins" # Global scope

def greet():
    fname = "Steven" # local scope
    lname = "Smith" # local scope
    print("Inside the function")
    print(fname)
    print(lname)

greet()

print("Outside the function")
print(fname)
print(lname)