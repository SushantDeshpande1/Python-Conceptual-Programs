#Searching in Set

Currency = {10 , 500 , 200 , 100}

print("Enter the value that you want to search in Set")
No = int(input())

for value in Currency:
    if(No == value):
        print("Element is present")
        break