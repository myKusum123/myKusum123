#program need
'''make a list of user Name
ask user for their user name 
if user's username is in the list tell them login successfull
else tell them invalid username.

Use:
list data containing all username
if else statement
in operator
'''

user_name= ['magar', 'input']
login=input("enter your username")
if login in user_name:
    print('you are login successfully')
else:
    print('invalid username')