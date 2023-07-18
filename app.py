#num1 =5.5
#print (type(num1))
# learn about complex numbers 
## complex number are specified as <real part><imaginary part>j
#compNum=5+6j
#print(type(compNum))
#print(compNum)
#str1="name"
#print(str1)
#quiz :
#person1={'name':'sarah','age':21,'address':'Irbid','phone number':'0789642365','email':'sarah@gmail.com'}
#print (person1['name'])
#print(person1['email'])
#person2={'name':'seedra','age':16,'address':'Irbid','phone number':'078964288','email':'seedra@gmail.com'}
#print (person2['name'])
#print(person2['email'])
#person3={'name':'marah','age':28,'address':'Irbid','phone number':'0789642365','email':'marah@gmail.com'}
#print (person3['name'])
#print(person3['email'])
#person4={'name':'morshed','age':25,'address':'Irbid','phone number':'0789642365','email':'morshed@gmail.com'}
#print (person4['name'])
#print(person4['email'])
#person5={'name':'mazin','age':60,'address':'Irbid','phone number':'0789642365','email':'mazin@gmail.com'}
#print (person5['name'])
#print(person5['email'])
#person1['age']=22
#person2['age']=18
#person3['age']=29
#person4['age']=26
#person5['age']=61
#print(person1['age'])
#print(person2['age'])
#print(person3['age'])
#print(person4['age'])
#print(person5['age'])
# check if the number you entered is odd or even
#num =int(input('enter the number '))
#if (num % 2)==0:
 #   print("the number is odd")
#else:
 #   print ("the number is even")     
    
#name ='sarah mazin'
#print (name[3:9])

#name1='loai'
#name1='*'+name1[1:]
#print(name1)
name2='salem'
#name2=name2[0:2]+'*'+name2[3:]
#print(name2)

#creat a for loop to replace all the 'l' with '*'
#for i in range(len(name2)):
 #   if name2[i]=='l':
 #      name2=name2[0:i]+'*'+name2[i+1:]
#print(name2)

#use replace function 
#for i in range(len(name2)):
  # if name2[i]=='l':
     # name2=name2.replace('l','*')
#print(name2)

#odd or even 
#num=int(input('enter the number: '))
#if (num%2)==0:
 #   print('the number ia even')
#else :
 #   print('the number is odd') 

# prime or not        
#prime=int(input('enter the number : '))
#for i in range (2,prime):
 #   if (prime%i)==0:
  #      print ('not prime')
   #     break
#else :
#     print('prime')   
        
# functions 
#def function name ()

#def printName (name):
 #   print('my name is  : '+ name)

#printName('sarah')  

#num1=int (input('enter first number: '))
#num2=int (input('enter second number: '))
#def sumAndMulty(first ,second):
 #   sumation=first+second
  #  mult=first*second
   # return('the sumis :'+str(sumation)+' and the multy is :'+str(mult))

#print (sumAndMulty(num1,num2))



def animalNameAndType(type ,name):
    print ('I have a '+type)
    print('My '+type+'s'+ ' name is '+name)

print('Hello ,enter your animals nam and type \n')   
animalType=input('enter your animal type: ')
animalName=input('enter your animal name: ')
animalNameAndType(animalType,animalName)
print('Do you want to enter a new animal?')
newANimal=(input(' YES or NO:'))
while newANimal!='yes' and newANimal!='no':
    print ('wrong input')
    newANimal=(input(' YES or NO:'))
while newANimal=='yes':
  if newANimal=='yes':
    animalType=input('enter your animal type: ')
    animalName=input('enter your animal name: ')
    animalNameAndType(animalType,animalName)
    print('Do you want to enter a new animal?')
    newANimal=(input(' YES or NO:'))
    while newANimal!='yes' and newANimal!='no':
      print ('wrong input')
      newANimal=(input(' YES or NO:'))
       
else:
  print ('Thank you !')
  