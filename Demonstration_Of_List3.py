
# Manipulation On List

Brands = ["Samsung" , "Apple" , "Oppo" , "Redmi"]

print("Elements in the list : ",Brands)


print("Adding New Element in the List...")
Brands.append("OnePlus")                      #append
print(Brands)

print("Adding New Element in the List at a specific index...")
Brands.insert(1 , "Nokia")                    #insert
print(Brands)

print("Removing an Element from the List...")
Brands.remove("Redmi")                        #remove
print(Brands)


print("Remove Last Element in the List...")  
Brands.pop()                    #pop last elem removed
print(Brands)

print("Remove index Element in the List...")  
Brands.pop(2)                    #pop  elem removed at index 2
print(Brands)

print("Delete Elements in the List...")  
del Brands[1:]                #del Elements deleted from index 1
print(Brands)

print("Extend Elements in the List...")  
Brands.extend(["Haier" , "Motorolla" , "Dell" , "HP"])       #extend 
print(Brands)

print("Sorts Element in the List...")  
Brands.sort()                    #sort 
print(Brands)
