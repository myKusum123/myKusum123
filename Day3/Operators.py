'''# Arithmetic Operators
 -mathmatical operators(+,-,*,/,%,) like :addition ,subtraction ,division
#Assignment Operators
# Comparision Operators
 #Logical Operators
-And: if both statement is true then then the result will be true  
-Or: if the one statement is true then the result will be true
-Not: if the statement is true then the result eill be false(reverse)
#Membership Operators
# Identity Operators
#Bitwise Operators
'''

#===================================================================================
# 1. Arithmetic Arithmetic Operators
   #addition operators(we can add same data type) but we cannot add different types
   #  of bracket, string and integer or we can add up to tuple not set
   #concatenate= add two string using +
a=6
b=9
c=2.5
#print(a+b+c)
a='2.5'
b='3'
#print(a+b)
a= 'hello'
b='world'
#print(a+b)
a='hello'
b='2'
#print(a+b)

c=['hello',2,3]
d=['2',3,4]
#print(c+d)
# Subtraction Arithmetic Operator( we can use integer and float data type)
a=20
b=30
#print(a-b)

# Multiplication Arithmetic Operator
# we can multiply string and number not an string* string but we can multiply float and integer
a=23
b=36
#print(a*b)
a='23'
b=5
#print(a*b)#we  can use string for duplication(2323232323)

#Division Arithmetic Operator(we can divide float and integer)
a=10
b=2
c=a/b
#print(a/b)
#print(type(c))
a=10.2
b=3
#print(a/b)

#Foor Arithmetic Operator( we use //)decimal vandah aagadi ko value matra aauxa or decimal bahek aru number return garxa
a=10
b=2
#print(a//b)

#Exponential Arithmetic Operator(power of something)we use**
a=3
b=4
#print(a**b)

#Modulus Operator(we use %) divide ko reminder nikalxa
a=20
b=3
#print(a%b)

# 2.Assignment operator( a variable le hello data assign gari raxa) (= [equal to]means assignment operator variable lai data assign garnu nai)
''' = is a assignment operator, assigs data yto variable   
 why we need assignment operator-because kahile kahi hami snga dherae data huna sakxa tyo
#data lai chai feri feri use garnu parxa so tyo thulo data lai lekhi rakhnu vanda baru 
variable ma store garni ra recall garni feri'''
a='Hello'
#print(a)

 #Add assignment operator(add only variable or variable vari... matra kam garxa)
a=10
b=20
# a and b vlaue lai add garera naya value banau nu xa
c=a+b
a+=b#(if you want to add old and new variable then you can use+= ani yo  aagadi ko left pati variable chai ma store hunxa)
#print(a)
#print(c)

#subtract assignment operator
a=20
b=30
#a=60(yesle over ride gari raxa pahila ko a lai)
print(a-b)
a-=b
b-=a
#print(b)
#print(a)
 # MUltiply assignment Operator
a=20
b=30
#print(a*b)
a*=b
#print(a)
 
#Division assignment Operator
a=20
b=30
print(a/b)
a/=b
#print(a)

#Floor Assignment Operator
a=20
b=30
a//=b
#print(a)

#Exponential Assignment Operator
a=20
b=30
a**=b
#print(a)

# Modulus Assignment Operator
a=20
b=30
a%=b
#print(a)

#3.Comaprision Operator(compare the two data)
# Greater than
a=6
b=3
#print(a>b)#(a is bigger than b)

# Less Than
a=2
b=3
#print(a<b)#(a is smaller than b)

#is equal
a=3
b=3
#print(a==b)

#not  is equal
a=5
b=3
#print(a!=b)

# Greater than or equal to
a=5
b=4
print(a>=b)
a=4
a=4
#print(a>=b)

#less than or equal To
a=8
b=6
#print(a>=b)
a=4
a=4
#print(a>=b)

#4. LOgical Operators
#a. And Operator
a=8
b=6
c=10
d=9
e= a>b and c>d
 #print(e)
f=a<b and c<d#(And operators check whether the two operations is true , if one of them operation is false
#if one of them operation is false 
# it returns false and if both are operation is true then it returns true)
#print(f)

#b.Or gate
a=8
b=6
c=10
d=9
e= a>b or c>d #( or operaters  check whether one of two operations is true,
#if true then it returns true , else if two operation is false it returns false)

print(e)
f=a<b or c>d or c<a
#print(f)

#c.not gate
a=8
b=6
c=10
d=9
e= not (a>b and c>d)# reverse gardinxa value ya data lai
#print(e)

#5. Membership Operators (euta data chai arko data ko part ho ki nai vanera chaeck garxa)
# we can use string, set, list and dictionary()
# group of data sanga matra use huni vayo in le integer sanga use hunna
# 1. In Operator
'''a= 'kusum'
b='m'
e="kusum Magar"
f="magar"
g=e in f
c=a in b
d=b in a
print(c)
print(d)# true because m ma kusum include hunxa
print (g)#false because f ma kusum include xaina
iteration - group of data ma euta euta jani ho . for example here is [abcd] then it goes ['a','b']'''
a=4.5
b=['hello',1,2,4.5]# we can use string, set, list and dictionary()
c=a in b
#print (c)

d='a'#(value check hunna key  sanga matra check hunxa in dictitonary)'
e={'a':'hello','b':'world'}
f=d in e
#print(f)

g='hello world'#(string is a group  character ho tesaile check hunxa )
h='hello'
i=h in g
#print(i)

j=4
k=(4,5,6)
l=j in k
#print(l)

#2. Not in operator
a='hello'
b='hello world'
c=a not in  b
#print (c) false it is oposite of in
a='hi'
b='hello world'
c=a not in  b
#print(c) true 

#6. Identity operator( idenity check garxa duitai eutai ho ki nai vanera)
#Is Operator
a='hello'
b='hello '
c=a is b# ora==b
print (c)

#is not operator
a='hello'
b='hello '
c=a is not b# or a !=b( != yesle chai data sanga kam garxa) and (is not le chai binary level ma pni check garxa)
print(c)

#7. Bitwise Operator -(binary level ma kam garxa)-(use & this symbol)
# And bitwise operator
a=7
b=6
c= a & b
#print(c)
'''1 2 4 8 (yesma chai 1 ra 0 aayo vani 0 return hunxa)
1 1 1   
0 1 1
-----
0 1 1=6
'''

#Or bitwise operator(| use this symbol)
'''
1 2 4 8 (yesma chai 1 ra 0 aayo vani pni 1 return garxa)
0 1 1   
1 1 0
-----
1 1 1=7
'''

a=6
b=3
c= a | b
#print(c)

# Invert bit wise operator -~ use this symbol
'''
-1-6 = -7(yesle -1 garni kam garxa ra - add garxa)
'''
a=~6
print(a)

#Shift right bit wise operator
a= 8
c=a>>8 #(yesle chai two step uta lani garxa data lai)
print (c)

#Shift left bit wise operator
a= 5
c=a<<5
print(c)

# XOR bit wise Operator
a=3
b=2
c=a^b
print(c)
'''
421
011
010
===
 01
'''
