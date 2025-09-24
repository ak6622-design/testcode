def number():   #Input a number from User
    num = int(input("Enter a number: "))
    print(num)

def odd_even():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print(n, "Is an Even number")
    else:
        print(n, "is an Odd Number")

def check():  #check if odd even or zero
    number = int(input("Enter a number: "))
    if number > 0:
        print("It is positive")
    elif number < 0:
        print("It is negative")
    else:
        print("Zero")

def square():
    number = int(input("Enter a number: "))
    print(number ** 2)

def cube():
    number = int(input("Enter a number: "))
    print(number ** 3)

# ---- main function ----
def main():
    number()
    odd_even()
    check()
    square()
    cube()

# ---- run program ----
if __name__ == "__main__":
    main()
