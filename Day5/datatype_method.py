# to define a certain type of data is called data type
#String(string data  sanga matra string data type ko method sanga kam grxa )immutable
# string are immutable 
# a='hello'
# b=a.capitalize()# first character uppercase . orginal data cannot be change and duplicate data will change
# d='HELLO'
# c=d.casefold()#lowercase
# print(d)
# e='hello,darling'
# f=e.count('l')#l kati ota xa count garxa
# print(f)
# g='I ma a girl i wamt chocolate'
# i=g.encode()# yele chai nabujini tarka le print gardinxa
# print(i)
# a="hi i am a boy and i want to be a football player"
# b=len(a)#(yesle kati ota words xa ani tesle space lai pni count garxa and yo chai aru data haru sanga pni kam garna milxa)
# print(b)
# d=['hello','3','3.5']
# e=len(d)
# print(e)

#List
# It is a mutable data and orginal data convert hunxa
# a=[1,2,2,2,3,'Hello']
#a.clear()sab clear garni garxa data list ko
# a.append('world')-yesle naya value ya word add garni kam garxa
# a.count(2)-kati ko ta string ya number xa teslai count garni kam garxa
# b=a.copy() jun method le return garxa teslai naya variable ma rakhnu parxa and copy le chai data lai duplicate garxa
# a.extend(b) arko list ya iterable(set tuple string aru data pni join garna milxa)
# lai pni jodni kam garxa
# a.remove(2) yesle remove garxa but dherae value xa vani first kun value xa teslai matra remove garxa
# a.reverse() yesle chai last bata reverse garni kam garxa
#print(a)
# b=a
# print(b)
#Set -orginal data convert hunna and it is unique(yesle same data lai terminal ma print gardae na )
# It is unique and mutable and math ko set jastai hunxa
a={1,2,3,3,4,5,'hello'}
b={4,5,6,7,1}
a.add('world')#add garna milxa kunai word ya number
#c=a.difference(b)-return garxa so new variable ma rakhnu parxa and jun jun value match garxa a ra b ma tyo print hunna  garxa and orginal set (a) ma jun jun value match gardae na teslai print garxa
#a.difference_update(b)yeslai naya variable ma rakhnu pardae na kina ki return xaina and orginal data lai nai change gardinxa ani jun jun match gardae na teslai set a mai rakhdinxa
#a ma jun jun naya data xa b ma xaina tyo print hunxa
#print(c)

#a.clear()-yesle clear garni kam garxa set ko data
#Tuple Methods-Immutable group of data, it is a constant data 
# a=(1,2,2,3,2,'hello')
#new data add garnu xa and tuple lai list ma lana milxa ni and list vaneko immutable data ho so kunai data change garnu xa vani typecasting garna milxa 
# b=list(a) -list ma change garni because it is immutable
# b.append('world)# list world add gareko
# a=tuple(b)-feri tuple ma lageko and worls add vayo finally hamile yestoh kina gareko vani tuple ma direct add garna mildaena
#print(a)
# b=a.count(2)- yesle chai count garni kam garxa word ya number
# c=a.index(3)-yesle kati number ma pareko xxa tha hunxa
# print(b)
# print(c)

#Dictionary-a group of keys and value
a={'a':'hello','b':'world'}
#b=a.keys()-keys haru return garxa
#b=a.items()-yesle chai key ra value lai tuple ma print gardinxa and typecasting tuple ma huni vayera
#d=a.get(f)-none return garxa ya print garxa kina kina ki f xaina ni tw data ma ya key ma 
#e=a.get(a)-yesko chai key ko value nikalxaz
#c=a.get(a)-yesle chai value lai return ya print garxa
#index and
#a='hello '-space ma pni character hunxa and print garda khali aauxa and  0 bata start hunxa yedi last bata ca
#start bata end point certain number chaheyo [0:3]0=h 1=e 2=1( hell aaunu parni ho but hel matra aako xa 0:3 gardah kinaki slicing gardah end point aaudae na starting point chai aauxa like 3 vandah aagadi aauxa )
# slicing-staring point will come and end point will not come 0:3= hel
#[1:3] el return hunxa
#positive index gardah aagadi bata count hudae janxa negative ma chai last bata return hunxa
#[-2]=o
#[-6:-1]=hello -count huda chai right hand bata hunxa negative hudah but slicing gardah chai first bata hunxa
# [-1:-6] = null aauxa 
#a[0]=1- yo chai 0 ko thau ma 1 xhange gareko
# List- group wise count like hi is 0
# a=['hi',1,8,9,'chocolate']
# b=(a[-5:-2])
# print(b)

# # String - yo chai character wise count hunxa
# a='Hello'
# b=(a[-5:-1])
# print(b)


# # Tuple
# a=(1,2,3,4,'hello','hi') 
# b=(a[:-1])
# print(b)

# Set-yesma chai index ra slicing hudae na
a={1,2,3,'hi'}
b=(a[:2])
print(b)

#Dictionary-yo chai key lekhepaxi matra index hunxa but slicing chai hudaena
a={'a':'hi',2:'two'}
b=(a[2])
print(b)




