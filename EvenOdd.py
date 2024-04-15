
def Check_EvenOdd(iNo):
    if (iNo  == 0):
        print("The Number is Zero")
    elif (iNo % 2 == 0):
        print("{} is a Even Number.".format(iNo))   
    elif (iNo % 2 != 0):
        print("{} is an Odd Number.".format(iNo))
    else :
        print("Invalid Input.")
    
def main():
    print("----Check Even or Odd Number----")

    Value = int(input("Enter a Number : "))

    Check_EvenOdd(Value)

if __name__ == "__main__":
    main()