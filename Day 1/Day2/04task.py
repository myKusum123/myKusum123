# # make a program with your intro to print type of that you make a program
# name='Kusum'
# age=28
# height=5.3
# address='Kalanki'
# marriage=False
# print(f'''My name is{name}
#           I am {age}  years old
#           I live in {address}
#           I am married {marriage}
#            ''')
# print (f'''{type(name)} 
#            {type(age)}  
#            {type(height)}  
#            {type(address)}  
#            {type(marriage)}  
#            ''' )
# print (type(age))
# print (type(height))
# print (type(address))
# print (type(marriage))
# e= "Hello World"
# print (type(e))
# print(e)
# print (e [5])
# print(e[::-1])
# f= 'Hello world  25468*((25485))'
# print (f)
#we can change in tuple  in list and set but cant change in dictionary


# my_tuple=('kusum' , 2,5.2)
# list_name=list(my_tuple)
# print(list_name)
# list_name[1]='Magar'
# my_tuple=tuple(list_name)
# print(my_tuple)


# my_set={'kusum',5,2,2.5}
# my_list=list(my_set)
# print(my_list)
# my_list[3]=2.6
# my_set=set(my_list)
# print(my_set)


# a=('kusum',5,2,3,4)
# list_a=list(a)
# print(list_a)
# list_a[2]='magar'
# print(list_a)
# a=tuple(list_a)
# print(a)

#operation
#Add
# a=10
# b=14
# #c=a+b
# a+=b
# print(b)
# a='6'
# b='8'
# c='kusum'
# print(a+b+c)

# a=('kusum',2,2.5) add ma chai up to tuple add hunxa but set disvtionary hudae na
# b=('magar',3,3.5)
# print(a+b)

#subtraction we cansubtract integer and float
# a=20
# b=10
# c=a-b
# a-=b
# print(a)

#multiplication-we cant multiply string and string but we can multiply string and float 
# a=10
# b=10
# a*=b
# print(a)
#Divide-only integer and float
# a=10
# b=2
# a/=b
# print(a)

#floor- point vandah aagadi ko number matra nikalxa
# a=10
# b=2
# a//=b
# print(a)

#Exponential-it works for the power of 
# a=10
# b=2
# a**=b
# print(a)

#modulus- reminder
# a=10
# b=2
# a%=b
# print(a)

#Comparision
#Greater than
# a=10
# b=2
# print(a>b)

# #Smaller than
# a=2
# b=3
# print(a<b)

#equal to
# a=1
# b=1
# print(a==b)

#not equal
# a=10
# b=20
# print(a!=b)

# And euta pni false vayo vani false hunxa
# a=10
# b=20
# c=30
# d=10
# c=a<b and c>d # true beacuse both variable are true
#c= a>b and c<d(false because both are false if one also false then it will false )
# print(c)

#Or euta matra true vayo vani true hunxa
# a=10
# b=20
# c=30
# d=10
# e=a<b or c<d
# print(e)

#not
# a=10
# b=20
# c=30
# d=10
# e=not(a<b and c>d)
# print(e)

#Membership

# a='kusum'
# b='k'
# print(b in a)
# #Membership tuple
# a=('kusum')
# b=('kusum',2,3)
# print(a in b)

# #Membership set is not allowed
# a={'kusum'}
# b={'kusum',2,3}
# print(a in b)

# #Membership Dictionary key matra ralhni
#in
# # a='k'
# # b={'m':'gar','r':'rai','k':'kus'}
# # c=a in b
# # print(c)

# #not in
# a='m'
# b='magar'
# print(a not in b)

# #identifier = is
# # is not
# a='kusum'
# b='m' 
# print(a is not b)

# is
# a='kusum'
# b='kusum'
# print(a is b)

# Bitwise Operator
#and Bitwise
# a=10
# b=20
# print (a&b)

#or bitwise
# a=20
# b=5
# c=a|b
# print(c)

# invert bitwise

a=~20
print(a)

#left shift bitwise

a=20
b=a<<2
print(b)

#right shift bitwise
a=30
b=a>>3
print(b)



















