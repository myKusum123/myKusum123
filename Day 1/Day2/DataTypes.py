'''
#Datatype
The type of data we use in program for various operation or work

 #Datatype in Python
*string
*Integer
*Float
*List
*Set
*Tuple
*Dictionary
*Boolean
*None

#String 
-  double ya single quatation vitra symbol ,number ra name  hunu paryo string ma
*Text Data
a= "Hello World" 
a= variable and "hello world"= string
print (type(a)) - kun data type ho thapauni
print(a)- a lai print garni
print (a [0])- 0 ma kun word parxa vanera tha pauni
example
a= 'Hello world  25468*((25485))'
a="Hello World"
a= "Hello World's"#if we want to use this (')  in string then  we use double quatation
a= 'Hello World"s'# if we want to use this (")  in string then  we use single quatation
 
#Integer
- it is a number
Product_price= 123456
Quantity= 10
 print('Product_price*Quantity)

 # Float
 - we use decimal number
 decimal_number= 2.6
 print (decimal_number)

 
 #list - Mutable
 - we use square bracket[]
 - in square bracket we put group of data like string float integer etc
 - we can put duplicate data in list eg: a=['apple' 'apple', 2,2,3,4] here apple
   cames two time and number 2 is also comming 2 times
 -we can change the define data in list 
  Product_list=["hello world" ,2 , 2.5]- here we are using string, float ,integer etc 
  so we called list because here is group of other data

  #Set
  -It is  unique group of data which is use in {}
  - We use curle bracket{}
  -in curle bracket we put only integer and float
  - number and float should be unique
   
  a={2,3,2.5}
  print(a)

 # Tuple - Immutable
 - we 
 
   small bracket()
 -in small bracket we put group of other data like string float integer etc
 - we use unique data
 -we cannot change the define data in Tuple
 data means small bracket vitra vako-('apple',2,3,5.6) 
Product_list=('apple',2,3,5.6)- only unique number and name has came we cannot repeat it

#Dictionary
-It is a group of data of  value and key
-we use curle bracket{}
-key should be in unique
a= {'a':'rama'} here 'a' is a key and we have to put :(column) and then 
    we use that key value 'rama' in curle bracket

#Boolean
- we use in true or false
- we used in operations
- define fact 

#NoneType
-yesko kam chai kali xa yeso kunai data hudae na
-hamile variable banauna man lageko xa but variable vitra kunai data rakhna 
mn xaina ahile paxi rakhnni ho vani hamile none use garna sakxau
- hamile k he operation garna mildae na
a= none

# Why we use data types in python
kina ki data types anusar kam hunxa program and every data types have different nature
according to it behave 
example: string vaneko euta text data ho ra text data anusar behave garxa
       : integer vaneko euta number data ho ra number data anusar behave garxa
#type()
-type() vaneko function  kina ki yesma group of words ma paranthesis use vako xa
 like bracket ,comma or paranthesis diyera word lai call garnu nai function ho  
- if we dont know the what type of data then we use type() 
example: a=(type(a)) j pni huna sakxa data like string, float etc
'''
# String Example
e= "Hello World"
print (type(e))
print(e)
print (e [0])
f= 'Hello world  25468*((25485))'
print (f)

g= ''' Hello World's 
"name" '''# if we want to use single and double quatation then we use triple quatation and triple quatation can use for comment also and multiple or new line
print(g)
h= "Hello World's"#if we want to use this (')  in string then  we use double quatation
print(h)
i= 'Hello World"s'# if we want to use this (")  in string then  we use single quatation
print(i)
 
 #Integer Example
Product_price= 123456
Quantity= 10
print(' Multiplication of Product_price and Quantity:', Product_price * Quantity)

#Float Example
decimal_number= 2.6
print (decimal_number)

#list Example
Product_data=["hello world" ,2 , 2.5]
print (Product_data)
Product_data=["hello world","hello world" ,2 , 2, 2.5]

#Set Example
a={2,3,2.5}
print(a)

# Tuple
Product_list=('apple',2,3,5.6)
print(Product_list)

# Dictionary
b= {'a':'rama','b':'cow','c':'10'}
print (b)

#Boolean
c=True
print(c)

#None type
d=None
print(d)

# Type Function= type()
print(type(d))
print(type(['2']))