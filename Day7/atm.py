'''
# program requirement
# create a relation data between debit card and the amount in it
# ask user for debit card no if exists tell his/her amount in debit card 
# if doesnot exits ask to register debit card no and ask yo deposit
# Note : We have to use while loop in this program
'''
existing_debit_card = {1:2300,2:2400,3:3000}
a = True
while a:
    choice = input('Do you have a debit card?(Yes/No): ')
    if choice == 'Yes':
        b = int(input('Enter your debit card no: '))
        if b in existing_debit_card:
         c = existing_debit_card.get(b)
         print('Total amount:',c)
        else:
          print('Debit card not found.')
    elif choice == 'No':
       debit_card_no = int(input('Enter your debit card no: '))
       amount = int(input('Enter the amount to be depoisted: '))
       existing_debit_card[debit_card_no] = amount
       print('Your registered Debit Card No: ',debit_card_no)
       print('Your depoisted amount: ',amount)
       print(existing_debit_card)
    else:
       print('Invalid choice')