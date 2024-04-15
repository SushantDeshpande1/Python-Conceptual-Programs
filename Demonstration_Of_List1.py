
#MyList1

print("MyList1....")

MyList1 = [ 10 , 20 , 30 , 40 , 50 ]               #List 1

print("Printing Elements in the list...")

print(MyList1)

print(type(MyList1))                   # < class ' list ' >

print("Type Of Element : ",type(MyList1[0]))       # < class 'int' >

print("MyList1 -1 :",MyList1[-1])                 #50

print("MyList1 -2 :",MyList1[-2])                 #40

print("MyList1 [:3]", MyList1[:3])        # 10 20 30

print("MyList1 [3:]", MyList1[3:])        # 40 50



#MyList2

print("MyList2....")

MyList2 = [ 11 , 21 , 51 , 101 , 111]             #List 2

print("Printing Elements using while Loop...")
i = 0
while(i < len(MyList2)):
    print(MyList2[i])
    i += 1

print("Priting Elements Using For loop...")

for num in range(0 , len(MyList2) , 1):
    print(MyList2[num])


#We can also create List Of List

MegaList = [MyList1 , MyList2]

print(MegaList)