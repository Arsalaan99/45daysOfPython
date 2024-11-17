message1 = 'Hello World'

message2 = "Dad's car"

print(message1.lower()) # prints message 1

print(message2.upper()) # prints message 2

print(len(message1)) # gives length of 1st string

print(len(message2)) # gives length of 2nd string

print(message1[5:])   # To access 1st message character individually --1st character starts at index 0

print(message2[8]) #  To acceess 2nd messages last character

print(message1.count('o'))

print(message1.find('World'))

message3 = message2.replace('car','Universe')

print(message3)

message4 = message1 + '. ' + message2 + ' = ' + message3 # concateated string

print(message4)

message = '{}. {} = {}!'.format(message1,message2,message3) # formated string

print(message)

message5 = f'{message1}. {message2} = {message3}!' # fstrings

print(message5)

print(dir(message))

print(help(str))

print(help(str.lower))

