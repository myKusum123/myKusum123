'''CLI(Command Line Interface)= terminal ma matra kam garni , input lini, interact garni etc 
print ma print lekhxau ani paranthesis dinxau ani tyo vitra data lekhxau ani output dinxa terminal ma
 function vaneko word lekhera parathesis
input() vaneko euta function ho yo pni same print jastai hunxa yesle input linxa terminal bata
input le chai data linxa user bata and the input()function  delays execution of a program
to allow the user to ytpe the input from the keyboard 

'''

#print("Hello welcome to our program!")
a= input('Enter a number: ')# ctrl + / highlighted code will be commented
b=int(a)
print(b+2)

# Type conversion (string lai chai conversion garna milxa  number ko text ko hoinaa)
a='5000'
b=int(a)#  ( integer data type conversion)
#print(type(b))
#print(b+500)
a=2.5
b=int(a)
#print(b+'hello')

a=5000
b=str(a)
#print(b+'hello')

a=['hello','1',2]
b=str(a)
(b+'hello')

a=True
b=str(a)#(string data type conversion)
#print(b+'hello')

# List conversion 
a=('hello',2,1)
b=list(a)
#print(b) 

a='hello' 
b=list(a)
#print(b) 
# dictionary conversion
 
a={'a':'hello'} 
b=list(a)
#print(b) - key sanga matra deal hunxa value hidden hunxa

#tuple conversion
a=['hello',2,3 ]
b=tuple(a)
#print(b) 

#set conversion
a=['hello',1,1.5]
b=set(a)
#print(b)

# Dictionary type conversion
#a=['hello',1,1.5] dictionary ma chai type conversion garna ali garo hunxa yedi garnu paryo vani see down
c=(('a','hello')),(('b','hi'))
b=dict(c)
#print(b)

