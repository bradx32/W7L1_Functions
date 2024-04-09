# if a number is a prime or not

def is_prime(number): # is_prime is the function
    for i in range(2, number): # 2 to 9 - 2, 3, 4, 5, ..., 9
        if (number % i == 0): # 10 % 2 = 0 == 0
            print("Not a prime")
            break
    else:
        print("Prime")

is_prime(10)
is_prime(5)