my_set = {3,4,5}
print('My set: ', my_set)


my_set2 = {'Hola',23.3,False,True}
print('My set2: ', my_set2)

my_set3 = {3,2,2}
print('My set3: ', my_set3)

#Error a set can't contains dinamic structures 
#my_set4 = {[3,4,5], 4}
#print('My set4: ', my_set4)

#######################
## CASTING WITH SETS
my_list = [1,1,2,3,4,4,5]
my_set = set(my_list)
print(my_set)

my_tuple = ('Hola', 'Hola', 'Hola', 3)
my_set = set(my_tuple)
print(my_set)

#######################
### EDIT ELEMENTS TO SET

# One element
my_set = {1,2,3}
my_set.add(4)
print(my_set)

# Multiple elements
my_set.update([1,2,5])
print(my_set)

my_set.update({6,8},(1,7,2))
print(my_set)

# Delete elements
my_set.discard(1)
print(my_set)

my_set.remove(2)
print(my_set)

# Delete random element
my_set.pop()
print(my_set)

# Clear set
my_set.clear()

#######################
### OPERATIONS WITH SETS

#UNION  
my_set1 = {3,4,5}
my_set2 = {5,6,7}
setA = my_set1
setB = my_set2
my_set3 = my_set1 | my_set2
setA.union(setB)
print(my_set3)

#INTERSECTION\
setA.intersection(setB)
my_set3 = my_set1 & my_set2
print(my_set3)

#DIFERENCE\
setA.difference(setB)
my_set4 = my_set1 - my_set2
print(my_set4)

# SYMMETRIC DIFERENCE
setA.symmetric_difference(setB)
my_set5 = my_set1 ^ my_set2
print(my_set5)
