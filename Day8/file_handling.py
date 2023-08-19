#it is a program based which is helpful in command line interface(CLI) and
# when we do filehandeling by we can open certain file from program and read
# the content and also we can add data in certain file we can make like data 
#base in CLI or we can put permanent data in cli then it is the best

# f=open('Day8\hello.txt','r')# open= location khojni and r=read ......opening file in read mode to read the contents forlogin
# a=f.read() # using read method which returns contents fromthe file
# print(a)
# f.close()
# write mode ma chai aba kunai location declare gareko xaina vani pni hamile open ma gayera new file banauna milxa
f=open('Day8\hello.txt','w') 
f.write('hello')# hello chai hello.txt print hunxa and write must be in string
#list_user=a.split('-') # while register every user data has symbol to seperate one data from another, using that symbol in split method  which splits every data have. and returns  a list  with seperated 

f.close()


# import modules or packages
# datetime=module
# #aru le banako function lai import garera aafno program ma implement garnu nai import modules vanxa
# import datetime 
# print(datetime.date. today())
# #or
# from datetime import date
# print(datetime.date. today())