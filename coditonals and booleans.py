
# Comparisons :

# Equal:               ==
# Not Equal:           !=
# Greater Than:        >
# Lesser  Than:        <
# Greater or Equal:    >=
# Lesser or Equal:     <=
# Object Identity:     is


# Logic : 

# and  true and true = true
# or   if either value is true , result is true
# not  complemts the valuw


print('''

          if statement

                       ''')

language = 'Python'

if language == 'Python':
   print('Condition is True')

# if language != 'Python':  # Doesnot print false statement; If value is false it does enter the loop
# 	print('False')


print('''

          if-else statement

                            ''')

lang = 'Java'

if lang == 'C++':
	print('Language is C++')      # To check if it is a match or not and return the result

else:
    print('No Match') 	


print('''

          elif statement

                          ''')

lan ='C++'

if lan == 'Python':
	print('Language is Python')         # To check if the desired value matches one of the many option

elif lan == 'Java':
	print('Language is Java')	 

elif  lan == 'C++':
	print('Language is C++')

else:
    print('No Match')

print('''    
             And
         ''')

user = 'Admin'
logged_in = True

if user == 'Admin'and logged_in :
    print('Welcome Admin')

else:
    print('Bad Creds') 


user1 = 'Admin'
logged__in = False

if user1 == 'Admin'and logged__in :
    print('Welcome Admin')

else:
    print('Bad Creds')        


print('''    
             Or
         ''')

face_recog = 1
password =  False

if face_recog == 1 or password :
    print('Welcome User')

else:
    print('Bad Creds')


print('''    
             Not     
         ''')
                               # It takes  not 0 as 1 as not(0) = 1 ; Thus gives answer as true  
user2 = 'Arsalaan'

log_in = 0

if not log_in: 
  print('Welcome User')

else:
    print('Bad Creds')     

print('''     
             object identity "is"
	''' )

a = [1, 2, 3]     
b = [1, 2, 3]    

print(a)
print(b)

print(a == b) # contents are same so true    ---True     
print(a is b) # identity of both are different ---False  

print(id(a))   # 29487560
print(id(b))   # 29513064 


d = [7, 8, 10, 33]
x = d 

print(d)
print(x)

print(d == x)  # contents are same, because 'd' and 'x' are same    ---True 
print(d is x) 

print(id(d))    # 50951368
print(id(x))    # 50951368








# all these values are cosidered as false value 

# False
# None
# Zero of any numeric type
# Any empty sequence. For example, 'string', [list], (tuple) 
# Any empty mapping (dictionary), for example , {} 


condition = False         # None, 0, '', [], (), {}  all will have same answer

if condition:
	print('Evaluated to True')

else:
   print('Evaluated to False')	# result -- Evaluated to False

# Every thing else except above will be true even if there are any random value in string, list, tuple and dictionary

condition1 = ' xyz'
 
if condition1 :
	print('Evaluated to True')

else:
   print('Evaluated to False')  # result --  Evaluated to True