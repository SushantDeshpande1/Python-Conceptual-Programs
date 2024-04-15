
print("---Demonstration Of Tuple---")

Prices = (1500 , 2000 , 2500 ,5000)
print(Prices)
print("Length Of Tuple : ",len(Prices))

print(Prices[0])
print(Prices[1])
print(Prices[-1])
print(Prices[1:])
print(Prices[:2])
print(Prices[1:3])


#Prices[1] = 1200   NA to change the contents

print(20 in Prices)        #False checks (like Search)

#Prices.append(67)    NA


for value in Prices:
    print(value)

for i in range(len(Prices)):
    print(Prices[i])


del Prices
