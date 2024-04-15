def FindFactors(Number):
    
    TestNumber = 1
    while(TestNumber <= Number):
        if(Number % TestNumber == 0):
            print(TestNumber)
        TestNumber = TestNumber + 1
        
def main():

    print("Welcome to Find Factor Application...")

    No = int(input("Enter a Number to Find it's Factors : "))
     
    FindFactors(No)

    print("Above are the factors of Number : ",No)

if __name__ == "__main__":
    main()