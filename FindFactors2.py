
def FindFactors(Value):

    for i in range(1,Value,1):
        if(Value % i == 0):
            print(i)
        
def main():
    No1 = int(input("Enter a Number to Find it's Factors : "))

    FindFactors(No1)

if __name__ == "__main__":
    main()
