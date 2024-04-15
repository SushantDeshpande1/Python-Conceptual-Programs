
print("---Demonstration Of Dictionary---")

Menu = {"Tea":20, "Coffee":25, "Milk":40 , "Cold Drink": 30 }

print(Menu)

print(type(Menu))

print(len(Menu))

print(Menu["Coffee"])

print("--1--")

for i in Menu:
    print(i)

print("--2--")

for i in Menu:
    print(Menu[i])

print("--3--")

for i in Menu:
    print(i , Menu[i])