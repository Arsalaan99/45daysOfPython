
courses = ['History', "Math", 'Science', 'CompSci']  # List

courses2 = ['Dance', 'Acting', 'Literature']

num = [9, 10, 1, 7, 3, 33]

print(courses)   # Print all the content of List

print(len(courses))

print(courses[0])  # Print the content of Specified index

print(courses[-1]) # Always Prints the content of last index

print(courses[0:2])

courses.append("Art")  # Adds value to the End of the list

print(courses)

courses.insert(3, 'Drawing')  # Adds value at specified location

print(courses)

#courses.insert(0,courses2)  # Adds list within list But the added list is considered as single entity and takes a single index and cannot be access individually

#print(courses)   same goes for append

courses.extend(courses2)  # Adds a list to the end of the main list and each content have separate index

print(courses) 

courses.remove('Art')  # Removes specified value

print(courses)

popped = courses.pop() # removes last value if no index is mentioned

print(popped)

removed = courses.pop(3) # removes the value at specified index

print(removed)

courses.reverse() # reverse the list

print(courses)

courses.sort() # sort the list alphabetically

print(courses)

num.sort() #sort the list in ascending order

print(num)

num.sort(reverse = True)

print(num)

sorted_list = sorted(courses)  # method to return sorted list

print(sorted_list)


print(min(num))

print(max(num))

print(sum(num))

print(courses.index('Dance'))  # return the index of specified content

#print(courses.index('EXtC'))

print('#########')

print('Extc' in courses)  # to search if a value exists in a list

print('Dance' in courses)

for course in courses:   # List all item in new line
  print(course)

for index, course in enumerate(courses):  # List all item with index value
  print( index, course)

for index, course in enumerate(courses, start = 1):  # List all item 1 as starting number
  print( index, course)

course_str = ", ".join(courses)   # join the all value in list as a single string   
print(course_str)               # Converts LIST into STRING

new_str =course_str.split(', ')  # seperate the string values as list
print(new_str)                   # converts STRING back to list

print(type(course_str))

print(type(courses))




