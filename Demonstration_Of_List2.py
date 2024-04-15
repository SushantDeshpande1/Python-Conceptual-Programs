
#taking input from user to store in a list

def main():
    print("Demonstration of storing user input elements in a list...")

    Length = int(input("Enter Number of Elements You Want to Store in the List : "))
    
    Arr = list()

    print("Enter the Elements : ")

    for i in range(Length):
        Value = int(input())
        Arr.append(Value)

    print("Elements from the List are : ")

    for i in range(len(Arr)):              # for i in range(Length)
        print(Arr[i])

if __name__ == "__main__":
    main()