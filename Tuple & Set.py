

## Lists are Mutable i.e. can be changed

print("""      

         LIST   

                """) 
list_1 = ['Alberto', 'Tiger', 'Affan', "Saffan", 'Raffan']
list_2 = list_1

print(list_1)
print(list_2) 

list_1[0] = 'Rio'

print(list_1)   # First item in the list 1 got change so change occur in both the lists 
print(list_2) 


### Tuple are Immutable i.e. cannot be changed 
 
print("""      

         TUPLE   

                """) 
tuple_1 = ('Alberto', 'Tiger', 'Affan', 'Saffan', 'Raffan')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

 # tuple_1[0] = 'Kaali'  gives error as tuple cannot be modidfied 

# print(tuple_1)
# print(tuple_2)

######## 

print("""

         SET

              """) 

# cs_courses = {'History', 'Math', 'Phyics', 'Compsci', 'Math' } # Sets get rid of duplicate value and print only one value of repeated items 
# print(cs_courses)                # Sets does not have fixed order and print values at random order which changes everytime


cs_courses = {'History', 'Phyics', 'Compsci', 'Math'}

art_courses = {'Civics', 'Art', 'Design', 'Phyics'}

print(cs_courses)
print(art_courses)

print(cs_courses.intersection(art_courses)) # Shows the item common in both sets 

print(cs_courses.difference(art_courses))  # Shows the difference that art courses do not have

print(cs_courses.union(art_courses))  # Shows all courses combined

# Empty List
empty_list = []  # OR
empty_list = list()

# Empty tuple
empty_tuple = ()  # OR
empty_tuple = tuple()
    
# Empty set
empty_set = {} # it is wrong and it does not create empty set but create dictionary 

# Correct way to create empty set
empty_set = set()



