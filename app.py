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

import random


class BankAccount:
    acc_name=''
    acc_num=0
    balance=0
    def generateAccountNum(self):
      accountnum=[]
      x=0
      for i in range (6):
          testnum=random.randint(1,9)
          accountnum.append(testnum)
      for i in range (len(accountnum)):
          x=x*10+accountnum[i]
      return x  
    def __init__(self,acc_name,balance,password):
        self.acc_name=acc_name
        self.acc_num=self.generateAccountNum()
        self.balance=balance
        self.password=password
    def __str__(self):
        return f'name is {self.acc_name} and the account number is {self.acc_num} and the belence is {self.balance}'
    def withdraw(self, amount):
       print ('you are about to withdraw.')
       passw=input('enter your password to confirme you withdraw operation : ')
     
       try:
            if(self.password==passw):
              if (self.balance)<int(amount):
                  return 'you do not have engough money'
              self.balance-=int(amount)
              return (f'your balance is {self.balance} and you withdraw {amount}')
            else :
                return('you enter wrong password')
       except ValueError:
              return 'you entered wrong value '
    def deposit (self, amount):
        print('you are about to deposite.')
        passw=input('enter your password to confirme your deposite operation : ')
        try:
           if(self.password==passw):
              self.balance+=int(amount)
              return (f'your balance is {self.balance} and you deposit {amount}')
           else :
                return('you enter wrong password')
        except ValueError:
            return 'you entered wrong value '
    def checkAccount(self):
        return f'your balance {self.balance}'
    def closeAccount (self):
        print('you are about to close your account.')
        passw=input('enter your password to confirme your closeing operation : ')
        print(self.withdraw(self.balance))
        self.acc_name='The account is closed'
        self.acc_num=0
        self.balance=0
        return f'The account is closed'
    def transaction(self,amount,num_accont):
        print ('You are about to make a transaction operation: ')
        passw=input('enter your password to confirme your closeing operation : ')
        try:
            if(self.password==passw):
              if (self.balance)<int(amount):
                  return 'you do not have engough money'
              self.balance-=int(amount)
              print(f'You transferred {amount} to account {num_accont.acc_num}')
              num_accont.balance +=int(amount)
              print(f"you'r balance is {self.balance}")
            else :
                print ('you entered wrong password ')  
        except ValueError:
              return 'you entered wrong value '      

        
        
accounts=[]
while True:
    print('*'*50)
    print('Welcome to our bank!')
    print('Do you have an account?')
    print('1.yes')
    print('2.no')
    choice = input('Enter your choice: ')
    if choice == '2':
      userName=input('enter your name :') 
      tryAndEx=True
      while tryAndEx:
        try:
          accbalance=int(input('enter the balance in your account :')) 
          tryAndEx=False
        except ValueError:
            print ('You enter wrong balance')  
      passwor=input('enter you password: ')      
      account1=BankAccount(userName,accbalance,passwor)
      for i in range (len (accounts)):
           account1=BankAccount(userName,accbalance,passwor)
      accounts.append (account1)
      print (account1)
    elif choice=='1':
         userName=input('enter your account number :') 
         passwor=input('enter you password: ')   
         for i in range (len(accounts)):
             if accounts[i].acc_num==int(userName) and accounts[i].password==passwor:
                  print ('1.Transfare money')
                  print('2.close account')
                  print('3.withdraw')
                  print('4.deposit')
                  print('5.check balance')
                  print('6.exit')
                  choice= input('enter your choice : ')
                  if choice=='1':
                        target_acc_num=input('Enter the number of account you want to transfer to it :')
                        amount=input('enter the amount of money you want to transfer :')
                        if accounts[i].acc_num == target_acc_num:
                          account1.transaction(target_acc_num,amount)
                  elif choice=='2':
                        print (accounts[i].closeAccount())
                  elif  (choice=='3'):  
                          amount=(input('enter the amount you want to withdraw: '))
                          print(accounts[i].withdraw(amount))     
                  elif(choice=='4'):     
                          amount=(input('enter the amount you want to deposit: '))
                          print (accounts[i].deposit(amount))
                  elif(choice=='5'):  
                    print(accounts[i].checkAccount())
                  elif(choice=='6'):
                      break 
          
