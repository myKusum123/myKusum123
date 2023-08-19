a=True
username_Info={'ram':'123','hari':'456','kusum':147}
while a:
 user_choice=input('Do you want to login or register ?')
if user_choice == 'login' :
 print(username_Info)
 username=input('enter your username : ')

 if username in username_Info:# in le chai left hand ko data type right hand ma xa ki nai check garxa
    password_Info=username_Info.get(username)# user_username  ma jun username aako xa tesko value dinxa
    password=input('enter your password')
    if password==password_Info:
        print('login successfully!')

 else:
    ('invalid password')
elif user_choice == 'register' :
 username=input('enter username :')
 password=input('enter password :')
 username_Info[username]==password
else:
  print('choice invalid !')

 