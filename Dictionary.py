
# student = {} # creates empty Dictionaries

student = {'Name': 'Jin Mori', 'Age': '19', 'Skills': ['Re-Taekwondo', 'Moonlight-Sword-Style '] } # Name , age and skills are "KEYS" of dictionary

print(student)

print(student['Name'])  # Can access individual keys through key name(string) 

print(student['Skills'])

student1 = {1: 'Naruto', 2: '19', 3: ['Rasengan', 'Shadow-Clone-Jutsu '] }   # keys name can be integer too

print(student1) 

print(student1[2])  # Can access individual keys through key number(integer)

 # print(student['Phone']) # if we try to search and access Key that does not exist it gives "KEYERROR"

# The best way to search and access dictionary is to use .get()

print(student.get('Name'))

print(student1.get(4))    # It returns 'none ' if the key does not exist

print(student.get('Phone', 'Not Found'))  # WE can write the message we want to see if the key is not found 

student['Phone'] = '5555-5555-55'  # can add key to dictionary

student1[1] = 'Naruto Uzumaki'  # can update keys in dictionray 

print(student)

print(student1)

# To update multiple keys at once use 'update'

student1.update({1 : 'Uzumaki Naruto', 4: 'Hinata' })
print(student1)


# To delete a key from dictionary

del student['Age']   
print(student)

Age = student1.pop(2)
print('Age is', Age)

print(len(student))

print(student1.keys())

print(student.values())

print(student.items())
print(student1.items())

for key in student1:   # only prints the name of keys 
 print(key)

for key, value in student.items(): # items() method is used for gettig value and key name simultaneously
 print(key, value)  