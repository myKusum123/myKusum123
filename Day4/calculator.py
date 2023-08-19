#program need
#Take number from users as input
#Take operation from users to perform with those numbers
# Perform the operation described by the users
#making CLI hami sanga Ui xaina so
number_1=int(input('Give me a number '))
number_2=int(input('Give me another number '))

user_operation=input('Give me the operation you want to perform')

if user_operation == 'add':
    print(number_1 + number_2)
elif user_operation == 'subtract': 
      print(number_1 - number_2)
elif user_operation == 'Multiply': 
      print(number_1 * number_2)      
elif user_operation == 'Division': 
      print(number_1 / number_2)
else:
      print('The operation you provided is currently not available')