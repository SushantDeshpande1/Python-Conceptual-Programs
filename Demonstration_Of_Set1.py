
print("---Demonstration of Set---") 

SampleSet = {11 , 999 , "Ram" , 50.11 ,"Python"} 

print(SampleSet) 

#print(SampleSet[1])    is NA

for Value in SampleSet:
    print(Value)

print("Length :",len(SampleSet)) 

SampleSet.remove(11) 
print(SampleSet)

SampleSet.discard(999) 
print(SampleSet) 

SampleSet.add("Hello") 
print(SampleSet) 
 
