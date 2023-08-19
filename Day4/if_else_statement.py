''' Input-(for cli)It is a function thet we can use in python to take input form users through 
terminal(yo terminal mai kam garxa)

'''
#userage=input('What is your age')# hamile string matra rakhna milxa input ma[=variable(username)le data(input())]lai assign gari raxa .yesle terminal ma input magi rako hunxa
#variable ko kam chai data ko location tha pauni ho
#print(username)
#user_name=int(userage)
#print(type(user_name)) 
a=10
b=5.4
c=a+b
d=int(b)
#print(type(username))

#print(d)
#print(type(b))
#print(c)


#If elase statement= condition is true or false (comparison or variable operation yo condition ma boolean value hunxa
#yo program le variable  boolean value store gari raxa 
raining=True


if raining:
    print('take your umbrella')
else:
   print('donot take umbrela')

'''
#yo program le operation comparison garni kam gareko xa boolean value
a=4
b=2

if a>b:
       print
       
       ('a is greater than b')
elif a==b:    #yedi arko condition launu xa vani if else ko bich ma elif rakhdah hunxa
       print('A is equal to b') 
elif a<b:    
       print('b is greater than a')             
else:
       print('a is not greater than b')
'''
# hamile if double lekhna milxa
print('***************Calculator*****************')
print('select your operation')
a=int(input('enter your a number'))

b=int(input('enter your b number'))

if a>b:
    print('A is greater than B')
    if b<a:
     print(' B is greater than A')
    else:
       print('Those values might be equal')
       if a==b:
          print('They are equal')
