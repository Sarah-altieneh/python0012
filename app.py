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
#name2='salem'
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



#def animalNameAndType(type ,name):
 #   print ('I have a '+type)
  #  print('My '+type+'s'+ ' name is '+name)

#print('Hello ,enter your animals nam and type \n')   
#animalType=input('enter your animal type: ')
#animalName=input('enter your animal name: ')
#animalNameAndType(animalType,animalName)
#print('Do you want to enter a new animal?')
#newANimal=(input(' YES or NO:'))
#while newANimal!='yes' and newANimal!='no':
 #   print ('wrong input')
  #  newANimal=(input(' YES or NO:'))
#while newANimal=='yes':
 # if newANimal=='yes':
  #  animalType=input('enter your animal type: ')
   # animalName=input('enter your animal name: ')
    #animalNameAndType(animalType,animalName)
    #print('Do you want to enter a new animal?')
    #newANimal=(input(' YES or NO:'))
   # while newANimal!='yes' and newANimal!='no':
    #  print ('wrong input')
     # newANimal=(input(' YES or NO:'))
       
#else:
 # print ('Thank you !')
#list1=[1,3,6,8,'a','9',10,13,9,20]
#sumation=0
#for i in list1:
 #   try:
  #    sumation+=int(i)  
   # except ValueError:
    #   print ('wrong input')
#print(sumation)    

#dectinary
person={
    'name':'sarah',
    'age': 21,
    'city':'Irbid',
}
person['job']='developer '
person['skills']=['c++','c#','java ']
person['parents']={
    'father':'mazen',
    'mother': 'asam'
}
#for i in person:
 #   print(i+' : '+str(person[i]))
#clear method 
#person.clear()
#print(person)

# copy 
#decNew ={}
#decNew=person.copy()
#print (decNew)

#items 
#print(person.items())

#keys
#print(person.keys())

#values
#print(person.values())

#classRoom={
 #   'sarah':{
  #    'name':'sarah',
   #   'age':21  ,
    #  'city':'irbid'
   # },
    #'mazen':{
     # 'name':'mazen',
      #'age':25,
      #'city':'amman'  
    #},
    #'marah':{
     #   'name':'marah',
      #  'age':23,
       # 'city':'irbid'
    #},
    #'seedra':{
     #   'name':'seedra',
     #   'age':18,
      #  'city':'amman'
    #}
#}
#for i in classRoom:
 #   print(classRoom[i])
  #  print('----------------------------------')

#student ={}
#inserstTime=int(input('how many keys do you want to add: '))
#for i in range (inserstTime):
 # stkey=input('Enter the key: ')
 # keytype=int(input('enter the type of the key 1 for str 2 for int 3 for list 4 for dic: '))
 # if (int(keytype)==1):
  #   student[stkey]=input('enter the value of '+stkey+': ')
  #elif(int(keytype)==2):   
   #         tryAndEX=True
    #        while tryAndEX:
     #         try:
      #            student[i]=int(input('enter your age : '))
       #           tryAndEX=False
        #      except ValueError:
         #       print('not number ') 
  #elif(int(keytype)==3):
     
   #  skillsElements = int(input("Enter the number of "+stkey+"skills you have : "))
    # student[stkey]=[]
    # for i in range(skillsElements):
     #   student[stkey].append(input('enter the'+stkey+': '))
  #elif(int(keytype)==4):                     
   # time=int(input('enter number of dectionary you want to add: '))
    #for i in range(time):             
     # newDec =input('enter new key :')
      #student[newDec]={}
     # time1=int(input('enter number of '+ newDec +' you want to add: '))
      #for j in range (time1):
       # newSubKey=input ('enter '+newDec+'number '+str(j+1)+': ')
        #student[newDec][newSubKey]=input('enter the value : ')
#print (student)

# import random


# class BankAccount:
#     acc_name=''
#     acc_num=0
#     balance=0
#     def generateAccountNum(self):
#       accountnum=[]
#       x=0
#       for i in range (6):
#           testnum=random.randint(1,9)
#           accountnum.append(testnum)
#       for i in range (len(accountnum)):
#           x=x*10+accountnum[i]
#       return x  
#     def __init__(self,acc_name,balance,password):
#         self.acc_name=acc_name
#         self.acc_num=self.generateAccountNum()
#         self.balance=balance
#         self.password=password
#     def __str__(self):
#         return f'name is {self.acc_name} and the account number is {self.acc_num} and the belence is {self.balance}'
#     def withdraw(self, amount):
#        print ('you are about to withdraw.')
#        passw=input('enter your password to confirme you withdraw operation : ')
     
#        try:
#             if(self.password==passw):
#               if (self.balance)<int(amount):
#                   return 'you do not have engough money'
#               self.balance-=int(amount)
#               return (f'your balance is {self.balance} and you withdraw {amount}')
#             else :
#                 return('you enter wrong password')
#        except ValueError:
#               return 'you entered wrong value '
#     def deposit (self, amount):
#         print('you are about to deposite.')
#         passw=input('enter your password to confirme your deposite operation : ')
#         try:
#            if(self.password==passw):
#               self.balance+=int(amount)
#               return (f'your balance is {self.balance} and you deposit {amount}')
#            else :
#                 return('you enter wrong password')
#         except ValueError:
#             return 'you entered wrong value '
#     def checkAccount(self):
#         return f'your balance {self.balance}'
#     def closeAccount (self):
#         print('you are about to close your account.')
#         passw=input('enter your password to confirme your closeing operation : ')
#         print(self.withdraw(self.balance))
#         self.acc_name='The account is closed'
#         self.acc_num=0
#         self.balance=0
#         return f'The account is closed'
#     def transaction(self,amount,num_accont):
#         print ('You are about to make a transaction operation: ')
#         passw=input('enter your password to confirme your closeing operation : ')
#         try:
#             if(self.password==passw):
#               if (self.balance)<int(amount):
#                   return 'you do not have engough money'
#               self.balance-=int(amount)
#               print(f'You transferred {amount} to account {num_accont.acc_num}')
#               num_accont.balance +=int(amount)
#               print(f"you'r balance is {self.balance}")
#             else :
#                 print ('you entered wrong password ')  
#         except ValueError:
#               return 'you entered wrong value '      

        
        
# accounts=[]
# while True:
#     print('*'*50)
#     print('Welcome to our bank!')
#     print('Do you have an account?')
#     print('1.yes')
#     print('2.no')
#     choice = input('Enter your choice: ')
#     if choice == '2':
#       userName=input('enter your name :') 
#       tryAndEx=True
#       while tryAndEx:
#         try:
#           accbalance=int(input('enter the balance in your account :')) 
#           tryAndEx=False
#         except ValueError:
#             print ('You enter wrong balance')  
#       passwor=input('enter you password: ')      
#       account1=BankAccount(userName,accbalance,passwor)
#       for i in range (len (accounts)):
#            account1=BankAccount(userName,accbalance,passwor)
#       accounts.append (account1)
#       print (account1)
#     elif choice=='1':
#          userName=input('enter your account number :') 
#          passwor=input('enter you password: ')   
#          for i in range (len(accounts)):
#              if accounts[i].acc_num==int(userName) and accounts[i].password==passwor:
#                   print ('1.Transfare money')
#                   print('2.close account')
#                   print('3.withdraw')
#                   print('4.deposit')
#                   print('5.check balance')
#                   print('6.exit')
#                   choice= input('enter your choice : ')
#                   if choice=='1':
#                         target_acc_num=input('Enter the number of account you want to transfer to it :')
#                         amount=input('enter the amount of money you want to transfer :')
#                         if accounts[i].acc_num == target_acc_num:
#                           account1.transaction(target_acc_num,amount)
#                   elif choice=='2':
#                         print (accounts[i].closeAccount())
#                   elif  (choice=='3'):  
#                           amount=(input('enter the amount you want to withdraw: '))
#                           print(accounts[i].withdraw(amount))     
#                   elif(choice=='4'):     
#                           amount=(input('enter the amount you want to deposit: '))
#                           print (accounts[i].deposit(amount))
#                   elif(choice=='5'):  
#                     print(accounts[i].checkAccount())
#                   elif(choice=='6'):
#                       break 
          
# # num1 = 5.5
# # print(type(num1))

# #  lear about complex numbers
# # complex numbers are specified as <real part>+<imaginary part>j

# # compNum=  5+7J
# # print(compNum)


# # str1="""name
# # mohasmm
# # msos"""
# # print(str1)

# #  data type  IN PYTHON
# # 1.  int
# # 2.  float
# # 3.  complex
# # 4.  String

# # 5.  Boolean
# # what is boolean
# # 0 = false
# # 1 = true
# # bool1 = True
# # print(bool1)

# # 6.  List
# # what is list
# # list is a collection of items in a particular order
# # nameOfList = [item1, item2, item3, item4]
# # can access item by index and can accept any type of data

# # lis1 = ['asdsad', 2.6, 3+6j, [4,'jdsjds'], 5, 6, 7, 8, 9]
# # index[0,         1,   2,     3,          4, 5, 6, 7, 8]
# # index : represent the position of item in list
# # index start from 0
# # print(lis1[3][1])
# # lis1[3][1] = 'changed'
# # print(lis1[3][1])
# # 7.  Tuple

# # what is tuple
# # tuple is a collection of items in a particular order
# # nameOfTuple = (item1, item2, item3, item4)
# # can access item by index and can accept any type of data
# # tuple is immutable

# # tupl1= ('asdsad', 2.6, 3+6j, [4,'jdsjds'], 5, 6, 7, 8, 9)
# # print(tupl1[3][1])
# # tupl1[0] = 'changed'
# # print(tupl1[0])

# # 8. dectionary
# # what is dictionary
# # dictionary is a collection of key value pairs
# # nameOfDictionary = {key1:value1, key2:value2, key3:value3}
# # person = {'name': 'mohammad', 'age': 28, 'address': 'irbid'}

# # print(person['age'])

# # quiz : create a dictionary that contains your name, age, address, phone number, and email
# # also print your name and email
# # then change your age and print it again



# # name= input('enter your name: ')
# # x = len(name)
# # finalString = ''
# # # for i in range(x) :
# # #     if name[i] == 'l':
# # #         finalString = '*'


# # print(name)
# # print(finalString)




# # name= 'sallem'

# # name= name[0:2]+'*'+ name[3:]
# # print(name)

# # name = input('enter your name: ')
# # # create for loop to replace all 'l' with '*'

# # for i in range(len(name)):
# #     if name[i] == 'l':
# #         name = name[0:i] + '*' + name[i+1:]
# # print(name)

# # # use replace function to replace all 'l' with '*'

# # for i in range(len(name)):
# #     if name[i] == 'l':
# #         name = name.replace('l', '*')
# # print(name)


# #  if statement
# #  elif statement
# #  else

# # num1 = int(input('enter first number: '))

# # if num1 > 0:
# #     print('positive')
# # elif num1 < 0:
# #     print('negative')
# # else:
# #     print('wrong input ')

# # what is loop in python

# # while num1 > 0:
# #     print(num1)
# #     num1 -= 1

# # odd or even number

# # oddOrOven = int(input('enter number: '))
# # if oddOrOven % 2 == 0:
# #     print('even')
# # else:
# #     print('odd')


# # prime or not
# # primeOrNot = int(input('enter number: '))


# # for i in range(2, primeOrNot):
# #     if primeOrNot % i == 0:
# #         print('not prime')
# #         break

# # else:
# #     print('prime')

# #  take 3  input from the user As astring and check if this string have l or u or both and
# # replace it with * and print the new string

# #  3 checks fro prime or odd or even for each
# #  and all the task must be inside while loop

# #Q1
# # x=0
# # while x<3:
# #     checkString=input ('enter a string: ')
# #     for i in range(len(checkString)):
# #          if ((checkString[i]=='l') or checkString[i]=='u'):
# #               checkString= checkString[0:i]+'*'+checkString[i+1:]
# #         # replace method in python
# #                 checkString=checkString.replace('l','*')

# #     print(checkString)


# #     num=int(input('enter the number: '))
# #     if (num%2)==0:
# #         print('the number ia even')
# #     else :
# #         print('the number is odd')

# #     prime=int(input('enter the number : '))
# #     for i in range (2,prime):
# #         if (prime%i)==0:
# #             print ('not prime')
# #             break
# #     else :
# #         print('prime')
# #     x = x+1

# # function in python
# # what is function
# # function is a block of code that can be called by its name and can be used again and again

# # we also send data to function as parameters

# # def functionName(parameter1, parameter2, parameter3):
# #    # code
# #   # return value

# # call function
# # functionName(argument1, argument2, argument3)

# # def printName(name):
# #     # print('hello ' + name)
# #     return ('hello ' + name)

# # print(printName('mohammad'))


# # num1= int(input('enter first number: '))
# # num2 = int(input('enter second number: '))

# # def sumAndMultiply(first,second):
# #     sumation = first + second
# #     multy = first * second
# #     return ('sumation is: ' + str(sumation) + ' and multy is: ' + str(multy))

# # print(sumAndMultiply(num1,num2))

# #  I have a hamster.
# #    My hamster's name is Harry.
# # answer = 'yes'
# # while answer != 'no':
# #     animalType = input('enter animal type: ')
# #     animalName = input('enter animal name: ')

# #     def printAnimal(type, name):
# #         return ('I have a ' + type + '.\nMy ' + type + "'s name is " + name + '.')
# #     print(printAnimal(animalType, animalName))

# #     print('do you want to continue?')
# #     answer = input('enter yes or no: ')


# #     while answer != 'yes' and answer != 'no':
# #         print('wrong input')
# #         answer = input('enter yes or no: ')

# # print('thank you')

# ## create 2 funiction iside while loop
# ## 3 input from the user as father name and mother name username
# ##  print greating for the user
# # print if the user mother or father name is longer or shorter than the username


# # list1 = ['mohammad', 'ahmad', 'sallem', 'mohammad', 'ahmad', 'sallem']
# # print(list1[2:5])

# # function : block of code that we can creat it and declare it and call it
# # method : block of code that we can use it without creat it or declare it
# # range : range(start, end, step)
# # variable : container for data
# # counter = 0
# # for i in list1:
# #     print(i == 'mohammad')
# #     if i == 'mohammad':
# #         list1[counter] = 'changed'
# #     counter += 1
# # print(list1)

# # list1= list1 + ['changed']
# # print(list1)

# # append : add item to the end of the list
# # list1.append('changed')

# # print(list1)

# # list1 = list1[0:2] + ['changed'] + list1[2:]
# # print(list1)


# # list1.insert(2 , 'changed')
# # print(list1)
# # list2 = [1,2,3,4,5]
# # # list1= list1 + list2
# # # print(list1)

# # # extend : add list to the end of the list
# # list1.extend(list2)
# # # print(list1)
# # list3 = [ -1,2,3,4,5,6,7,8,9,100,10,2,6,3]
# # sumation = 0
# # for i in list3:
# #     sumation += i
# # print(sumation)
# # print(sum(list3))

# # # for i in list3:
# # #     if i == 10:
# # #         sumation += 1
# # # print(sumation)

# # # count : count the number of times the item is repeated in the list

# # print(list3.count(10))

# # # len : return the length of the list

# # len(list3)

# # # index : return the index of the item in the list

# # print(list3.index(10))
# # maxValue = list3[0]
# # minValue = list3[0]

# # for i in list3:
# #     if i > maxValue:
# #         maxValue = i

# #     if i < minValue:
# #         minValue = i

# # print(maxValue)
# # print(minValue)
# # list3 =  list3[-1:]
# # print(list3)
# # counters = -1
# # list4 =[]
# # for i in range(len(list3)):
# #     print(i)
# #     list4.append(list3[counters])
# #     counters -= 1
# # print(list4)
# # list3.reverse()
# # print(list3)
# # sort : sort the list

# # list3.sort(reverse=True)
# # print(list3)

# # pop : remove item from the list using index
# # list3.pop(7)
# # print(list3)

# # remove : remove item from the list using value

# # list3.remove(100)
# # print(list3)

# # create a list of 10 numbers and print the sum of these numbers but the list should
# # have 2 numbers as string and the rest as numbers also int and float
# # avarage of the list
# # max and min of the list
# # print the index of the max and min of the list
# #

# # list2 = [1,2,3,4,5,'a',7,'8',9,10]
# # sumation = 0
# # for i in list2:
# #     try :

# #         sumation += int(i)
# #     except ValueError:
# #         print('wrong value')


# # print( sumation)

# # dectionary : collection of key value pairs



# #  -----------------------

# # ------------

# # person = {
# #     'name' : 'mohammad',
# #     'age' : 28,
# #     'city' : 'irbid',
# # }

# # person['job'] = 'developer'
# # person['skills']= ['java', 'python']
# # person['parents']= {
# #     'father':'ahmad',
# #     'mom':'lina',
# #     'son':{
# #         'name':'ali',
# #         'age':16

# #     }
# # }
# # print(person)


# # for loob : print the key and the value of the dec

# # for i in person:
# # print(i + ' : ' + str(person[i]))


# # methods in dectonary :

# # clear :

# # person.clear()
# # print(person)

# # copy : copy one list to anouther

# # decNew = {}
# # decNew=person.copy()
# # print(decNew)

# # items : get all items in the dec
# # print(person.items())

# # keys : print all keys in the dec

# # print(person.keys())

# # Valus : to print all valus in the list
# # print(person.values())

# # pop : remove for item inside the dec

# # person.pop('job')
# # print(person)
# # print(person['parents']['son']['name'])

# # print(person['skills'][0:3])

# # popitem
# # print(person)
# # person.popitem()
# # print(person)

# # update

# # person.update({"city": "amman"})
# # person['city']= 'amman'
# # print(person)


# # home work

# # create claSSROOM DEC
# # user input
# # 1 ask the useer to enter the name of the student
# # ask the user to enter the age of the student
# # cuity, job ,parents(dec),age,skils(list)
# # at nthe end ask the user if he want to add new student or not
# # print all the students in the class
# #       mohammad
# # age:  28

# # # home work of dec
# # def getStudentInformation():
# #     studentName= input('Enter the student name: ')
# #     studentAge =int(input('Enter the student age :'))
# #     studentCity=input('Enter the city  where the student live : ')
# #     studentJob=input ('Enter the job of the student : ')
# #     print ('Enter the parent information')
# #     fatherName =input('Enter name of the student father : ')
# #     motherName =input('Enter name of the student mother : ')
# #     parents={'mother':motherName,'father':fatherName}
# #     skillsElements = int(input("Enter the number of skills you have : "))
# #     skills = []
# #     for i in range(skillsElements):
# #         user_input = input("Enter the skill: ")
# #         skills.append(user_input)
# #     return{
# #         'name':studentName,
# #         'age':studentAge,
# #         'city':studentCity,
# #         'job':studentJob,
# #         'Parents':parents,
# #         'skills':skills
# #     }
# # classRoom={}
# # newStudent='yes'
# # whileCondition = True
# # while whileCondition:
# #     if newStudent=='yes':
# #         print ('\n Enter the student information ')
# #         studentInformation = getStudentInformation()
# #         classRoom[studentInformation['name']] =studentInformation
# #         newStudent= input("Do you want to add more students? (yes/no): ")
# #     elif newStudent=='no' :
# #         whileCondition = False
# #         print("\nClassroom Dictionary:")
# #         for student_name, student_info in classRoom.items():
# #                         print(f"Name: {student_info['name']}")
# #                         print(f"Age: {student_info['age']}")
# #                         print(f"City: {student_info['city']}")
# #                         print(f"Job: {student_info['job']}")
# #                         print("Parents:")
# #                         print(f"\tmother : {student_info['Parents']['mother']}")
# #                         print(f"\tfather: {student_info['Parents']['father']}")
# #                         print("Skills:", ", ".join(student_info['skills']))
# #                         print('-----------------------------------')


# #  classes : is a blue print for creating objects

# # class Student:

# class Student:


#     def __init__(self, name ='sam', age=20, job='student',location='irbid'):
#         self.name = name
#         self.age = age
#         self.job = job
#         self.location = location

#     def printName(self):
#         print("my name is "+self.name)

#     def __str__(self):
#         return f'name : {self.name} , age : {str(self.age)} , job : {self.job}, location : {self.location}'


# #  send job name age to the class in unordered way
# obj3 = Student()
# obj1 = Student('dev', 28, 'mohammad')
# obj2 = {'name':'ali', 'age':16, 'job':'student'}
# print(obj3)

# # # class Clinet:
# # #     name = 'mohammed'
# # #     age = 27
# # #     city = 'riyadh'

# # # client1= Clinet()
# # # print(client1.name)

# # # #  class has attributes and methods
# # # # what is the difference between attributes and methods
# # # # attributes are variables
# # # # methods are functions



# # #  cars
# # #  models> color> power >company> year> price> type>
# # print('*'*70)
# # print('welcome to our car show room')
# # print('my app is about cars')
# # print('you can add a car by entering the model, color, power, company, year, price and type')
# # print('*'*70)
# # cars=[]
# # while True:
# #     car={}
# #     car['model'] = input('enter the model:')
# #     car['color'] = input('enter the color:')
# #     car['power'] = input('enter the power:')
# #     car['company'] = input('enter the company:')
# #     car['year'] = int(input('enter the year:'))
# #     car['price'] = int(input('enter the price:'))
# #     car['type'] = input('enter the type:')
# #     cars.append(car)
# #     if input('do you want to add an other car?') == 'no':
# #         break
# # for i in range(len(cars)):
# #     print('*'*70)
# #     print('car number', i+1)
# #     for j in cars[i]:
# #         print(j, ':', cars[i][j])


# # #  pationts
# # #  name> medican> doctor>insurance >hospital>age


# # # computers
# # #  storage> ram> cpu> company> price> type> color> year

# # #  trasportation mode
# # #  mode > travil time> fule consumption> amustions> cost> repare cost

# class BankAcount:



#     def __init__(self, name ='', num= 0, balance = 0,password=''):
#         self.acc_name = name
#         self.acc_num = num
#         self.acc_balance = balance
#         self.password = password

#     def __str__(self):
#         return f'name is {self.acc_name} and number is {self.acc_num} and balance is {self.acc_balance}'

#     def withdraw(self,amount ):
#         passw= input('enter your password:')
#         if passw == self.password:

#             try:
#                 if self.acc_balance < int(amount):
#                     print('you do not have enough money')
#                     return 'you do not have enough money'
#                 self.acc_balance -= int(amount)
#                 print(f'your balance is {self.acc_balance} and you withdraw {amount}')
#                 return f'your balance is {self.acc_balance} and you withdraw {amount}'
#             except ValueError:
#                 print('you should enter a number')
#                 return 'you should enter a number'
#         else:
#             print('wrong password')
#             return 'wrong password'

#     def deposit(self,amount):
#         try:

#             self.acc_balance += int(amount)
#             print(f'your balance is {self.acc_balance} and you Deposit {amount}')
#             return f'your balance is {self.acc_balance} and you Deposit {amount}'
#         except ValueError:
#             print('you should enter a number')
#             return 'you should enter a number'
#     def checkBalance(self):
#         print(f'your balance is {self.acc_balance}')
#         return f'your balance is {self.acc_balance}'
#     def closeAccount(self):
#         print('you are about to close your account')
#         passw= input('enter your password:')
#         if passw == self.password:
#             self.acc_name = 'closed account'
#             self.acc_num = 0
#             self.withdraw(self.acc_balance)
#             self.acc_balance = 0
#             print('your account is closed')
#             return 'your account is closed'
#         else:
#             print('wrong password')
#             return 'wrong password'


# account2= BankAcount('ahmad', 123456, 1000,'2333')
# print(account2)
# account2.withdraw('200')
# # # account2.deposit('500')
# # account2.checkBalance()
# account2.closeAccount()
# print(account2)
#  random method to generate a random number
# import random

# # print(testNum1)

# class BankAccount:
#     acc_name=''
#     acc_num=0
#     balance=0
#     def generateAccountNumber(self):
#         accountNumber =[]
#         for i in range(6):
#             testNum =random.randint(1,9)
#             accountNumber.append(testNum)
#         x =0
#         for i in range(len(accountNumber)):
#             x = x*10 + accountNumber[i]
#         return x
#     def __init__(self,acc_name,balance,password):
#         self.acc_name=acc_name
#         self.acc_num=self.generateAccountNumber()
#         self.balance=balance
#         self.password=password
#     def __str__(self):
#         return f'name is {self.acc_name} and the account number is {self.acc_num} and the belence is {self.balance}'
#     def withdraw(self, amount):
#        print ('you are about to withdraw.')
#        passw=input('enter your password to confirme you withdraw operation : ')

#        try:
#             if(self.password==passw):
#               if (self.balance)<int(amount):
#                   return 'you do not have engough money'
#               self.balance-=int(amount)
#               return (f'your balance is {self.balance} and you withdraw {amount}')
#             else :
#                 return('you enter wrong password')
#        except ValueError:
#               return 'you entered wrong value '
#     def deposit (self, amount):
#         print('you are about to deposite.')
#         passw=input('enter your password to confirme your deposite operation : ')
#         try:
#            if(self.password==passw):
#               self.balance+=int(amount)
#               return (f'your balance is {self.balance} and you deposit {amount}')
#            else :
#                 return('you enter wrong password')
#         except ValueError:
#             return 'you entered wrong value '
#     def checkAccount(self,sender,amount):
#          return f'your balance {self.balance}'
        
#     def closeAccount (self):
#         print('you are about to close your account.')
#         passw=input('enter your password to confirme your closeing operation : ')
#         print(self.withdraw(self.balance))
#         self.acc_name='The account is closed'
#         self.acc_num=0
#         self.balance=0
#         return f'your account is closed '
#     def transfare(self):
#         print('you are about to transfare.')
#         try:
#             while True:
#                 passw=input('enter your password to confirme your transfare operation : ')

#                 if(self.password==passw):
#                     reciver=input('enter the account number of the reciver : ')
#                     for i in range(len(accounts)):
#                         if accounts[i].acc_num==int(reciver):
#                             print('1- transfare all your money')
#                             print('2- transfare a specific amount of money')
#                             choice=input('enter your choice : ')
#                             if choice=='1':
#                                 pass
#                             elif choice=='2':
#                                 print('you are about to transfare a specific amount of money.')
#                                 amount=input('enter the amount you want to transfare : ')
#                                 self.balance-=int(amount)
#                                 accounts[i].balance+=int(amount)
#                                 print(f'your balance is {self.balance} and you transfare {amount} to {accounts[i].acc_name}')
#                                 return f'your balance is {self.balance} and you transfare {amount} to {accounts[i].acc_name}'

#                 else :
#                     return('you enter wrong password')
#         except ValueError:
#             return 'you entered wrong value '


# accounts=[]
# while True:

#     print('*'*50)
#     print('welcome to our bank')
#     print('do you have an account with us?')
#     print('1- yes')
#     print('2- no')
#     choice=input('enter your choice: ')
#     if choice=='2':
#         userName=input('enter your name :')
#         accbalance=int(input('enter the balance in your account :'))
#         passwor=input('enter you password: ')

#         account1=BankAccount(userName,accbalance,passwor)
#         for i in range(len(accounts)):
#             if account1.acc_num==accounts[i].acc_num:
#                         account1=BankAccount(userName,accbalance,passwor)
#         accounts.append(account1)
#         print(account1)

#     elif choice=='1':
#         username = input('enter your account number :')
#         password = input('enter your password :')
#         for i in range(len(accounts)):
#             if accounts[i].acc_num==int(username) and accounts[i].password==password:
#                 print('1- Transfer money')
#                 print('2- close account')
#                 print('3- withdraw')
#                 print('4- deposit')
#                 print('5- check balance')
#                 print('6- exit')
#                 choice=input('enter your choice: ')
#                 if choice=='1':
#                     accounts[i].transfare()
#                 elif choice=='2':
#                     print(accounts[i].closeAccount())
#                 elif choice=='3':
#                     amount=input('enter the amount you want to withdraw: ')
#                     print(accounts[i].withdraw(amount))
#                 elif choice=='4':
#                     amount=input('enter the amount you want to deposit: ')
#                     print (accounts[i].deposit(amount))
#                 elif choice=='5':
#                     print(accounts[i].checkAccount())
#                 elif choice=='6':
#                     break
#                 else:
#                     print('you entered wrong choice')
# class privetOrPublic:
#     def __init__(self,name, password):
#         self.name =name
#         self.__password=password
#     def __str__(self) :
#         return f'name is {self.name}' 
#     def getPassword(self):
#         return self.__password
#     def setPassword (self,newpasssword):
#         self.__password=newpasssword
#         return self.__password
# class childClass(privetOrPublic):
#     def __init__(self, age,city):
#         super().__init__('sarah','15987')
#         self.age=age
#         self.city=city
#     def __str__(self):
#         return f'password is {self.getPassword()} , age is {self.age} , and city is {self.city} , {super().__str__()}'     

# user1=privetOrPublic('sarah','12345')
# child1=childClass('21','irbid')
# print(user1)
# print(user1.setPassword(147899))       
# print(child1)

# # #  Course  an Teachers and students
# # #  course : id, name, code, credit hours, teacher, students
# # #  teacher : id, name, age, address, field, Courses, students
# # #  student : id, name, age, address, Courses, teachers, field

# # #  create 3 classes
class Collage:
    def __init__(self,name,address):
        self.name = name
        self.address = address
    def __str__(self):
        return f'name is {self.name} and address is {self.address}'

class Profile:
    def __init__(self,id,name,age,address,field):
        self.name = name
        self.age = age
        self.address = address
        self.field = field
        self.id = id
class Courses(Collage):

    def __init__(self, id, name, code, credit_hours,address,collageName):
        super().__init__(collageName, address)
        self.id = id
        self.name = name
        self.code = code
        self.credit_hours = credit_hours



    def __str__(self):
        return f'id is {self.id} , name is {self.name} , code is {self.code} , credit hours is {self.credit_hours} , {super().__str__()} '

class Teacher(Courses,Profile):
    def __init__(self,id,name,age,address,field,Courses,students):
        self.Courses = Courses
        self.students = students
        Profile.__init__(self,id,name,age,address,field)
    def __str__(self):
        return f'id is {self.id} , name is {self.name}  , address is {self.address} ,age is {self.age},field is {self.field}  , Courses is {self.Courses} , students is {self.students}'


class Student(Courses,Profile):

    def __init__(self,id, name, age, address, Courses, field,Teachers):

        self.Courses = Courses
        self.teachers=Teachers
        Profile.__init__(self,id,name,age,address,field)
        # self.teachers = teachers

    def __str__(self):
        return f'id is {self.id} , name is {self.name} , age is {self.age} , address is {self.address} , Courses is {self.Courses} , teachers is {self.teachers} , field is {self.field}'



courses =[]
while True:
    print('*'*50)
    print('welcome to our collage')
    print('1- add course')
    print('2- add teacher')
    print('3- add student')
    print('4- exit')
    choices = input('enter your choice: ')
    if choices == '1':
            print('you are about to add a course')
            id = input('enter the id of the course: ')
            name = input('enter the name of the course: ')
            if len(courses) == 0:
                    code = input('enter the code of the course: ')
                    credit_hours = input('enter the credit hours of the course: ')
                    address = input('enter the address of Collage: ')
                    collageName = input('enter the collage name : ')
                    course = Courses(id=id,name=name,code=code,credit_hours=credit_hours,address=address,collageName=collageName)
                    courses.append(course)
            else:
                keppGoing = False
                for i in courses:
                        if i.name==name or i.id==id:
                            print('this course is already exist')
                            keppGoing = False
                            break
                        else:
                            keppGoing = True
                if keppGoing == True:
                    code = input('enter the code of the course: ')
                    credit_hours = input('enter the credit hours of the course: ')
                    address = input('enter the address of Collage: ')
                    collageName = input('enter the collage name : ')
                    course = Courses(id=id,name=name,code=code,credit_hours=credit_hours,address=address,collageName=collageName)
                    courses.append(course)


    if choices == '2':
        pass
    if choices == '3':
        pass
    if choices == '4':
        break
    for i in courses:
        print('*'*50)
        print(i)
        